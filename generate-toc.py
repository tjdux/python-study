import os
import nbformat

def extract_headers(ipynb_path):
    """노트북 파일에서 헤더를 추출하여 목차 리스트를 반환함."""
    headers = []
    try:
        with open(ipynb_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
            for cell in nb.cells:
                if cell.cell_type == 'markdown':
                    lines = cell.source.split('\n')
                    for line in lines:
                        if line.startswith('#'):
                            level = line.count('#', 0, line.find(' '))
                            title = line.strip('# ').strip()
                            if level > 0:
                                headers.append((level, title))
    except Exception as e:
        print(f"Error reading {ipynb_path}: {e}")
    return headers

def generate_readme():
    content = "# Project Contents\n\n"
    files = sorted([f for f in os.listdir('.') if f.endswith('.ipynb')])
    
    if not files:
        print("No jupyter notebook files found.")
        return

    for file in files:
        file_url = file.replace(" ", "%20")
        content += f"### [{file}]({file_url})\n"
        headers = extract_headers(file)
        for level, title in headers:
            # 대문자 헤더(#)는 제외하고 세부 목차만 표시 (선택 사항)
            indent = "  " * (level - 1)
            content += f"{indent}- {title}\n"
        content += "\n"

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    generate_readme()