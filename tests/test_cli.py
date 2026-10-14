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
