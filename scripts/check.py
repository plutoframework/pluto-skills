"""Check portable skill frontmatter, length and Markdown references."""
from pathlib import Path
import re
from urllib.parse import urlsplit, unquote

root = Path(__file__).resolve().parents[1]
paths = sorted((root / "skills").glob("*/SKILL.md"))
assert paths, "No skills found"
for path in paths:
    text = path.read_text()
    frontmatter, body = text.removeprefix("---\n").split("\n---\n", 1)
    name = re.search(r"^name: ([a-z0-9-]+)$", frontmatter, re.M)
    assert text.startswith("---\n") and name, path
    assert name[1] == path.parent.name and len(name[1]) < 64, path
    assert re.search(r"^description: .{20,}$", frontmatter, re.M), path
    assert len(body.split()) <= 400, f"Skill too long: {path}"
    documents = [path] + sorted((path.parent / "references").glob("*.md"))
    for document in documents:
        links = re.findall(r"\]\(([^)]+)\)", document.read_text())
        if document == path:
            assert links, f"Missing references: {document}"
        for link in links:
            url = urlsplit(link)
            assert url.path.endswith(".md"), (document, link)
            if url.scheme:
                assert url.scheme == "https" and url.netloc, (document, link)
            else:
                target = (document.parent / unquote(url.path)).resolve()
                assert target.is_relative_to(root.resolve()), (document, link)
                assert target.is_file(), f"Missing reference: {document}: {link}"
    print(f"{name[1]}: {len(body.split())} words")
print(f"PASS: {len(paths)} skills")
