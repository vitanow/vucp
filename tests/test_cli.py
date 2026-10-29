import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
CLI = REPO / "cli" / "vucp_cli_mvp.py"
PATTERNS = REPO / "templates" / "user" / "_cross_project_patterns"


def run(*args):
    return subprocess.run([sys.executable, str(CLI), *map(str, args)], capture_output=True, text=True)


def init_ws(tmp_path):
    ws = tmp_path / "ws"
    r = run("init", ws, "--project", "Test", "--owner", "Tester")
    assert r.returncode == 0, r.stderr
    return ws


def patterns_json(ws, tags):
    r = run("patterns", ws, "--patterns", PATTERNS, "--tags", tags, "--json")
    assert r.returncode == 0, r.stderr
    return json.loads(r.stdout)


# --- smoke tests ---

def test_init_lint_doctor_smoke(tmp_path):
    ws = init_ws(tmp_path)
    assert (ws / "CURRENT.md").exists() and (ws / "AUTOPILOT.md").exists()
    assert run("lint", ws).returncode == 0
    assert run("doctor", ws).returncode == 0


def test_init_refuses_nonempty(tmp_path):
    ws = init_ws(tmp_path)
    assert run("init", ws).returncode == 3


def test_lint_fails_on_missing_file(tmp_path):
    ws = init_ws(tmp_path)
    (ws / "CURRENT.md").unlink()
    r = run("lint", ws)
    assert r.returncode == 1 and "CURRENT.md" in r.stdout


def test_export_adapters(tmp_path):
    ws = init_ws(tmp_path)
    assert run("export", "claude-md", ws).returncode == 0
    assert run("export", "agents-md", ws).returncode == 0
    assert (ws / "_publish/adapters/claude/CLAUDE.md").exists()
    assert (ws / "_publish/adapters/AGENTS.generated.md").exists()


# --- bug 1: patterns --tags must filter ---

def test_patterns_nonsense_tags_return_nothing(tmp_path):
    ws = init_ws(tmp_path)
    assert patterns_json(ws, "zzz_nonsense")["count"] == 0
    r = run("patterns", ws, "--patterns", PATTERNS, "--tags", "zzz_nonsense")
    assert r.returncode == 0
    assert "No patterns match tags" in r.stdout


def test_patterns_tags_filter(tmp_path):
    ws = init_ws(tmp_path)
    titles = {p["title"] for p in patterns_json(ws, "deployment")["patterns"]}
    assert titles == {"rollback-first-deployment"}


def test_patterns_yaml_block_list_tags_are_read(tmp_path):
    ws = init_ws(tmp_path)
    titles = {p["title"] for p in patterns_json(ws, "cli")["patterns"]}
    assert "cli-help-contract" in titles
    assert "demo-before-pitch" not in titles


# --- bug 2: autopilot audit ---

def test_audit_ignores_template_example(tmp_path):
    ws = init_ws(tmp_path)
    data = json.loads(run("autopilot", "audit", ws, "--json").stdout)
    assert data["count"] == 0


def test_audit_reports_current_mode(tmp_path):
    ws = init_ws(tmp_path)
    assert run("autopilot", "set", ws, "--mode", "SILENT").returncode == 0
    data = json.loads(run("autopilot", "audit", ws, "--json").stdout)
    assert data["current_mode"] == "SILENT"


def test_audit_counts_real_entry(tmp_path):
    ws = init_ws(tmp_path)
    log = ws / "_delta/AUTOPILOT_LOG.md"
    log.write_text(log.read_text() + "\n---\ntype: autopilot_action\nactor: agent\nautopilot_mode: SURFACE\naction_class: write\nrisk_level: low\nhuman_approval: not_required\nsummary: \"Updated CURRENT.md\"\n---\n")
    data = json.loads(run("autopilot", "audit", ws, "--json").stdout)
    assert data["count"] == 1
    assert data["entries"][0]["summary"] == "Updated CURRENT.md"


# --- tag semantics (fixture library for deterministic results) ---

def make_library(tmp_path):
    lib = tmp_path / "lib"
    lib.mkdir()
    specs = {
        # name: (tags, confidence)
        "alpha": (["cli", "safety"], "0.50"),
        "beta": (["cli"], "0.99"),
        "gamma": (["safety"], "0.70"),
        "delta": (["design"], "0.90"),
    }
    for name, (tags, conf) in specs.items():
        body = "---\ntype: cross_project_pattern\nstatus: confirmed\nconfidence: " + conf + "\ntags:\n"
        body += "".join(f"  - {t}\n" for t in tags) + "---\n# " + name + "\n"
        (lib / f"{name}.md").write_text(body)
    return lib


def lib_patterns(tmp_path, tags):
    ws = init_ws(tmp_path)
    lib = make_library(tmp_path)
    r = run("patterns", ws, "--patterns", lib, "--tags", tags, "--json")
    assert r.returncode == 0, r.stderr
    return json.loads(r.stdout)


def titles(data):
    return [p["title"] for p in data["patterns"]]


def test_tags_case_insensitive(tmp_path):
    assert sorted(titles(lib_patterns(tmp_path, "CLI"))) == ["alpha", "beta"]


def test_tags_whitespace_trimmed(tmp_path):
    data = lib_patterns(tmp_path, " cli , safety ")
    assert data["tags"] == ["cli", "safety"]
    assert sorted(titles(data)) == ["alpha", "beta", "gamma"]


def test_tags_empty_entries_ignored(tmp_path):
    assert lib_patterns(tmp_path, "cli,,  ,")["tags"] == ["cli"]


def test_tags_or_union_ranked_by_matches(tmp_path):
    data = lib_patterns(tmp_path, "cli,safety")
    t = titles(data)
    assert set(t) == {"alpha", "beta", "gamma"}
    # alpha matches 2 tags, so it ranks first despite the lowest confidence
    assert t[0] == "alpha"
    assert data["patterns"][0]["matched_tags"] == 2
    assert all(p["matched_tags"] == 1 for p in data["patterns"][1:])


def test_tags_all_nonmatching_multi_returns_zero(tmp_path):
    assert lib_patterns(tmp_path, "foo,bar,baz")["count"] == 0


def test_tags_empty_string_means_no_filter(tmp_path):
    data = lib_patterns(tmp_path, "")
    assert data["tags"] == []
    assert sorted(titles(data)) == ["alpha", "beta", "delta", "gamma"]


# --- frontmatter parser hardening ---

def load_cli_module():
    import importlib.util
    spec = importlib.util.spec_from_file_location("vucp_cli_mvp", CLI)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["vucp_cli_mvp"] = mod
    spec.loader.exec_module(mod)
    return mod


def test_parser_ignores_list_items_under_unknown_key(tmp_path):
    mod = load_cli_module()
    f = tmp_path / "p.md"
    f.write_text(
        "---\ntags:\n  - design\nnotes: |\n  - cli\n  - deployment\n"
        "does_not_apply_to:\n  - production\n---\n# p\n"
    )
    fields = mod.extract_frontmatter_fields(f)
    assert fields["tags"] == "design"
    assert fields["notes"] == "|"
    assert fields["does_not_apply_to"] == "production"


# --- does_not_apply_to overrides positive matches ---

def excl_library(tmp_path):
    lib = tmp_path / "excl"
    lib.mkdir()
    (lib / "rollback.md").write_text(
        "---\nstatus: confirmed\nconfidence: 0.9\ntags:\n  - deployment\n"
        "does_not_apply_to:\n  - production\n---\n# rollback\n"
    )
    (lib / "other.md").write_text(
        "---\nstatus: confirmed\nconfidence: 0.5\ntags:\n  - deployment\n---\n# other\n"
    )
    return lib


def excl_titles(tmp_path, tags):
    ws = init_ws(tmp_path)
    r = run("patterns", ws, "--patterns", excl_library(tmp_path), "--tags", tags, "--json")
    assert r.returncode == 0, r.stderr
    return sorted(p["title"] for p in json.loads(r.stdout)["patterns"])


def test_does_not_apply_to_excludes_matching_pattern(tmp_path):
    assert excl_titles(tmp_path, "deployment") == ["other", "rollback"]
    assert excl_titles(tmp_path / "b", " PRODUCTION ") == []


def test_does_not_apply_to_wins_over_positive_match(tmp_path):
    assert excl_titles(tmp_path, "deployment,production") == ["other"]


# --- VUCP Lite ---

def init_lite(tmp_path):
    ws = tmp_path / "lite"
    r = run("init", ws, "--lite", "--project", "Demo", "--owner", "Tester")
    assert r.returncode == 0, r.stderr
    return ws


def test_lite_init_creates_exactly_three_files(tmp_path):
    ws = init_lite(tmp_path)
    found = sorted(str(p.relative_to(ws)) for p in ws.rglob("*") if p.is_file() or p.is_dir())
    assert found == ["AGENTS.md", "CURRENT.md", "LEARNINGS.md"]
    assert "vucp_mode: lite" in (ws / "AGENTS.md").read_text()
    assert "Demo" in (ws / "CURRENT.md").read_text()


def test_lite_lint_and_doctor_clean(tmp_path):
    ws = init_lite(tmp_path)
    lint = json.loads(run("lint", ws, "--json").stdout)
    assert lint["mode"] == "lite" and lint["errors"] == 0 and lint["warnings"] == 0
    doc = json.loads(run("doctor", ws, "--json").stdout)
    assert doc["mode"] == "lite" and doc["errors"] == 0 and doc["warnings"] == 0


def test_lite_lint_reports_missing_file(tmp_path):
    ws = init_lite(tmp_path)
    (ws / "LEARNINGS.md").unlink()
    r = run("lint", ws, "--json")
    data = json.loads(r.stdout)
    assert r.returncode == 1 and data["mode"] == "lite"
    assert [i["path"] for i in data["issues"]] == ["LEARNINGS.md"]


def test_lite_long_file_warning(tmp_path):
    ws = init_lite(tmp_path)
    with (ws / "LEARNINGS.md").open("a") as f:
        f.write("x" * 9000)
    data = json.loads(run("doctor", ws, "--json").stdout)
    assert "LITE_FILE_TOO_LONG" in [i["code"] for i in data["issues"]]


def test_lite_export(tmp_path):
    ws = init_lite(tmp_path)
    assert run("export", "claude-md", ws).returncode == 0
    assert run("export", "agents-md", ws).returncode == 0
    claude = (ws / "_publish/adapters/claude/CLAUDE.md").read_text()
    assert claude.startswith("# CLAUDE.md") and "## Learnings" in claude and "Demo" in claude
    assert "VUCP Lite" in (ws / "_publish/adapters/AGENTS.generated.md").read_text()


def test_lite_template_matches_cli(tmp_path):
    mod = load_cli_module()
    rendered = mod.lite_files("<PROJECT_NAME>", "<OWNER_NAME>", "<YYYY-MM-DD>")
    for name in ["AGENTS.md", "CURRENT.md", "LEARNINGS.md"]:
        assert rendered[name] == (REPO / "templates/lite" / name).read_text()


def test_lite_template_token_budget():
    # Rough budget: ~1500 tokens is about 1100 words; keep a wide margin.
    words = sum(len((REPO / "templates/lite" / n).read_text().split()) for n in ["AGENTS.md", "CURRENT.md", "LEARNINGS.md"])
    assert words < 600


def test_lite_upgrade_non_destructive(tmp_path):
    ws = init_lite(tmp_path)
    (ws / "CURRENT.md").write_text("# my state\n")
    (ws / "LEARNINGS.md").write_text("# my learnings\n")
    assert run("upgrade", ws, "--dry-run").returncode == 0
    assert not (ws / "MANIFEST.yaml").exists()
    assert run("upgrade", ws).returncode == 0
    assert (ws / "CURRENT.md").read_text() == "# my state\n"
    assert (ws / "LEARNINGS.md").read_text() == "# my learnings\n"
    assert (ws / "_delta/LEARNINGS.md").read_text() == "# my learnings\n"
    lint = json.loads(run("lint", ws, "--json").stdout)
    assert lint["mode"] == "full" and lint["errors"] == 0
    assert run("upgrade", ws).returncode == 1  # already full


def test_full_workspace_not_detected_as_lite(tmp_path):
    ws = init_ws(tmp_path)
    assert json.loads(run("lint", ws, "--json").stdout)["mode"] == "full"


# --- hardening 9.2 ---

def test_full_init_writes_safe_gitignore_and_is_doctor_clean(tmp_path):
    ws = init_ws(tmp_path)
    gi = (ws / ".gitignore").read_text(encoding="utf-8")
    for pat in ["USER_CORE.private.md", ".env", "*.key", ".vucp/tmp/"]:
        assert pat in gi
    r = run("doctor", ws, "--json")
    assert r.returncode == 0, r.stderr
    codes = [i["code"] for i in json.loads(r.stdout)["issues"]]
    assert "GITIGNORE_MISSING" not in codes
    assert not [i for i in json.loads(r.stdout)["issues"] if i["severity"] in ("error", "warning")]


def _assert_graceful(r, code=1):
    assert r.returncode == code, (r.stdout, r.stderr)
    assert "Traceback" not in r.stderr and "Traceback" not in r.stdout
    assert "ERROR" in r.stderr


def test_autopilot_status_invalid_mode(tmp_path):
    ws = init_ws(tmp_path)
    (ws / "AUTOPILOT.md").write_text("---\nmode: TURBO\n---\n# broken\n", encoding="utf-8")
    _assert_graceful(run("autopilot", "status", ws))
    r = run("autopilot", "status", ws, "--json")
    _assert_graceful(r)
    data = json.loads(r.stdout)
    assert data["ok"] is False and data["mode"] == "INVALID"


def test_autopilot_status_binary_garbage(tmp_path):
    ws = init_ws(tmp_path)
    (ws / "AUTOPILOT.md").write_bytes(b"\xff\xfe\x00\x81garbage\x00")
    _assert_graceful(run("autopilot", "status", ws))


def test_autopilot_status_empty_file(tmp_path):
    ws = init_ws(tmp_path)
    (ws / "AUTOPILOT.md").write_text("", encoding="utf-8")
    _assert_graceful(run("autopilot", "status", ws))


def test_autopilot_status_is_directory(tmp_path):
    ws = init_ws(tmp_path)
    (ws / "AUTOPILOT.md").unlink()
    (ws / "AUTOPILOT.md").mkdir()
    _assert_graceful(run("autopilot", "status", ws))


def test_autopilot_status_valid_after_set(tmp_path):
    ws = init_ws(tmp_path)
    assert run("autopilot", "set", ws, "--mode", "GUIDED").returncode == 0
    r = run("autopilot", "status", ws, "--json")
    assert r.returncode == 0 and json.loads(r.stdout)["mode"] == "GUIDED"


def test_export_claude_md_has_key_sections(tmp_path):
    ws = init_ws(tmp_path)
    r = run("export", "claude-md", ws, "--json")
    assert r.returncode == 0, r.stderr
    text = Path(json.loads(r.stdout)["output"]).read_text(encoding="utf-8")
    assert text.startswith("# CLAUDE.md")
    for section in ["## Current State", "## Workspace", "## Agent Instructions", "## Safeguards", "## Next Action"]:
        assert section in text, section
    assert "Test" in text


def test_export_all_targets_nonempty_and_distinct_paths(tmp_path):
    ws = init_ws(tmp_path)
    outs = set()
    for target in ["agents-md", "codex", "claude-md", "cursor-rules", "windsurf-rules"]:
        r = run("export", target, ws, "--json")
        assert r.returncode == 0, (target, r.stderr)
        data = json.loads(r.stdout)
        assert data["bytes"] > 200
        out = Path(data["output"])
        assert "## Safeguards" in out.read_text(encoding="utf-8") or "Safeguard" in out.read_text(encoding="utf-8")
        outs.add(str(out))
    assert len(outs) == 5


def _lint_codes(ws):
    r = run("lint", ws, "--json")
    assert "Traceback" not in r.stderr
    return r, [i["code"] for i in json.loads(r.stdout)["issues"]]


def test_lint_invalid_risk_level(tmp_path):
    ws = init_ws(tmp_path)
    cf = ws / "stages" / "research" / "CONTEXT.md"
    cf.write_text(cf.read_text(encoding="utf-8").replace('risk_level: "low"', 'risk_level: "extreme"'), encoding="utf-8")
    _, codes = _lint_codes(ws)
    assert "CONTEXT_RISK_INVALID" in codes


def test_lint_missing_frontmatter_field(tmp_path):
    ws = init_ws(tmp_path)
    cf = ws / "stages" / "research" / "CONTEXT.md"
    cf.write_text(cf.read_text(encoding="utf-8").replace("review_required: true\n", ""), encoding="utf-8")
    _, codes = _lint_codes(ws)
    assert "CONTEXT_FRONTMATTER_FIELD_MISSING" in codes


def test_lint_missing_manifest_fails(tmp_path):
    ws = init_ws(tmp_path)
    (ws / "MANIFEST.yaml").unlink()
    r, codes = _lint_codes(ws)
    assert r.returncode != 0
    assert any(c in codes for c in ["MANIFEST_MISSING", "REQUIRED_FILE_MISSING"])


def test_generated_files_have_no_dashes_in_new_gitignore(tmp_path):
    ws = init_ws(tmp_path)
    gi = (ws / ".gitignore").read_text(encoding="utf-8")
    assert "\u2013" not in gi and "\u2014" not in gi
