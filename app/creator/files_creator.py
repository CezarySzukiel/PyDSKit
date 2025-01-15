import os
import subprocess


def create_project_structure(project_name: str = "ds_project"):
    structure = {
        "data": ["raw", "processed", "external", "interim"],
        "notebooks": ["exploration", "modeling", "reporting"],
        "src": ["data", "features", "models", "visualization"],
        "reports": ["figures"],
        "tests": [],
    }

    files = {
        "README.md": "# Project description and usage instructions\n",
        "pyproject.toml":
"""
[project]
name = "PyDSKit"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "jupyterlab>=4.3.5",
    "matplotlib>=3.10.1",
    "numpy>=2.2.3",
    "openpyxl>=3.1.5",
    "pandas>=2.2.3",
    "python-magic>=0.4.27",
    "xlsxwriter>=3.2.2",
]
""",
        "environment.yml": "# Conda environment file (optional)\n",
        "reports/final_report.md": "# Final project report\n",
        ".gitignore": "# Ignore unnecessary files\n",
    }

    os.makedirs(project_name, exist_ok=True)

    for parent, subdirs in structure.items():
        parent_path = os.path.join(project_name, parent)
        os.makedirs(parent_path, exist_ok=True)
        for subdir in subdirs:
            os.makedirs(os.path.join(parent_path, subdir), exist_ok=True)

    for file, content in files.items():
        file_path = os.path.join(project_name, file)
        with open(file_path, "w") as f:
            f.write(content)

    print(f"Project '{project_name}' has been successfully created.")


def package_installer(project_name: str):
    try:
        result = subprocess.run(["uv", "sync"], check=True, capture_output=True, text=True, cwd=project_name)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error while running 'uv sync': {e.stderr}")

# todo dodać możliwość konfiguracji struktury projektu oraz początkowej zawartości plików poprzez plik settings.json
# todo zamiast najpierw tworzyć katalogi i pliki, zrób uv add zestaw paczek a później pliki i katalogi
# todo użyć uv build zamiast flita
