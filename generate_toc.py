from pathlib import Path
from urllib.parse import quote

import nbformat


TARGET_EXTS = {".ipynb", ".md", ".py"}
EXCLUDE_DIRS = {
    ".git",
    ".ipynb_checkpoints",
    ".venv",
    "venv",
    "__pycache__",
    "node_modules",
}


def extract_headers_from_ipynb(ipynb_path: Path):
    """노트북 파일에서 헤더를 추출하여 (level, title) 리스트 반환."""
    headers = []
    try:
        with ipynb_path.open("r", encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)
        for cell in nb.cells:
            if cell.get("cell_type") == "markdown":
                for line in str(cell.get("source", "")).splitlines():
                    if line.startswith("#"):
                        # '# ' 형태의 마크다운 헤더만 인정
                        space_idx = line.find(" ")
                        if space_idx == -1:
                            continue
                        level = line[:space_idx].count("#")
                        if level <= 0:
                            continue
                        title = line[space_idx + 1 :].strip()
                        if title:
                            headers.append((level, title))
    except Exception as e:
        print(f"Error reading {ipynb_path}: {e}")
    return headers


def extract_headers_from_md(md_path: Path):
    """마크다운 파일에서 헤더를 추출하여 (level, title) 리스트 반환."""
    headers = []
    try:
        with md_path.open("r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("#"):
                    space_idx = line.find(" ")
                    if space_idx == -1:
                        continue
                    level = line[:space_idx].count("#")
                    if level <= 0:
                        continue
                    title = line[space_idx + 1 :].strip()
                    if title:
                        headers.append((level, title))
    except Exception as e:
        print(f"Error reading {md_path}: {e}")
    return headers


def is_excluded(path: Path) -> bool:
    parts = set(path.parts)
    return any(d in parts for d in EXCLUDE_DIRS)


def github_link_for(rel_path: Path) -> str:
    # README 안의 상대 링크로 쓸 경로. GitHub에서 안전하게 열리도록 인코딩.
    return quote(rel_path.as_posix())


def scan_files(root: Path):
    """root 아래에서 대상 확장자를 재귀 탐색해 relative path 리스트 반환."""
    results = []
    for p in root.rglob("*"):
        if p.is_dir():
            continue
        if is_excluded(p):
            continue
        if p.suffix.lower() in TARGET_EXTS:
            # README 자신은 제외
            if p.name.lower() == "readme.md":
                continue
            results.append(p.relative_to(root))
    return sorted(results, key=lambda x: x.as_posix().lower())


def generate_readme(root: Path = Path(".")):
    content = ["# Project Contents", ""]

    files = scan_files(root)
    if not files:
        print("No target files found (.ipynb, .md, .py).")
        return

    # 폴더별로 묶고 싶으면 groupby로 나눌 수 있지만, 일단 전체 정렬 리스트로 출력
    for rel in files:
        url = github_link_for(rel)
        content.append(f"### [{rel.as_posix()}]({url})")

        abs_path = root / rel
        headers = []
        if abs_path.suffix.lower() == ".ipynb":
            headers = extract_headers_from_ipynb(abs_path)
        elif abs_path.suffix.lower() == ".md":
            headers = extract_headers_from_md(abs_path)

        # 원하면 최상위(#)를 빼고 싶을 때: level == 1 제외
        for level, title in headers:
            if level == 1:
                continue
            indent = "  " * (level - 2)  # level=2가 0칸, level=3이 1칸
            content.append(f"{indent}- {title}")

        content.append("")

    (root / "README.md").write_text(
        "\n".join(content).rstrip() + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    generate_readme()
