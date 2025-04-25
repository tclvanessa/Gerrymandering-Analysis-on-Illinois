import json
import sys
from pathlib import Path

def force_downgrade_notebook(notebook_path, target_version=4, target_minor=5):
    try:
        with open(notebook_path, "r", encoding="utf-8") as f:
            nb = json.load(f)

        current_version = nb.get('nbformat', 0)
        current_minor = nb.get('nbformat_minor', 0)

        if (current_version < target_version) or (current_version == target_version and current_minor <= target_minor):
            print(f"✔ Already compatible: {notebook_path} (nbformat {current_version}.{current_minor})")
            return

        # Forcefully set the nbformat version
        nb['nbformat'] = target_version
        nb['nbformat_minor'] = target_minor

        with open(notebook_path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=2)

        print(f"✔ Forcefully downgraded: {notebook_path}")
    except Exception as e:
        print(f"✘ Error processing {notebook_path}: {e}")

def process_path(path_str):
    path = Path(path_str)

    if not path.exists():
        print(f"Path not found: {path}")
        return

    if path.is_file() and path.suffix == ".ipynb":
        force_downgrade_notebook(path)

    elif path.is_dir():
        for nb_file in path.rglob("*.ipynb"):
            force_downgrade_notebook(nb_file)
    else:
        print("Please provide either a .ipynb file or a directory containing notebooks.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python force_downgrade_ipynb.py <file_or_folder_path>")
        sys.exit(1)

    process_path(sys.argv[1])
