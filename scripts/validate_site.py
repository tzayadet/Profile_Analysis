from pathlib import Path
import re
import subprocess
import tempfile

root = Path(__file__).resolve().parents[1]
html = (root / "index.html").read_text(encoding="utf-8")

scripts = re.findall(r"<script[^>]*>(.*?)</script>", html, re.IGNORECASE | re.DOTALL)
if len(scripts) != 1:
    raise SystemExit(f"Expected one inline application script, found {len(scripts)}")

if re.search(r"<script[^>]+src=[\"']https?://", html, re.IGNORECASE):
    raise SystemExit("Unexpected remote JavaScript dependency")

script = scripts[0]
questions_match = re.search(r"const QUESTIONS = \[(.*?)\];", script, re.DOTALL)
profiles_match = re.search(r"const PROFILES = \{(.*?)\n    \};", script, re.DOTALL)
if not questions_match or len(re.findall(r"\{t:", questions_match.group(1))) != 60:
    raise SystemExit("Expected exactly 60 question records")
if not profiles_match or len(re.findall(r"^\s{6}[A-Z]{4}:", profiles_match.group(1), re.MULTILINE)) != 16:
    raise SystemExit("Expected 16 profile descriptions")

for forbidden in ("fetch(", "XMLHttpRequest", "sendBeacon("):
    if forbidden in script:
        raise SystemExit(f"Unexpected network API in local-only assessment: {forbidden}")

if "localStorage.setItem" not in script or "localStorage.removeItem" not in script:
    raise SystemExit("Expected local save and delete behavior")

with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8", delete=False) as handle:
    handle.write(script)
    script_path = Path(handle.name)

try:
    subprocess.run(["node", "--check", str(script_path)], check=True)
finally:
    script_path.unlink(missing_ok=True)

print("Profile Analysis validation passed: 60 questions, 16 profiles, local-only storage.")
