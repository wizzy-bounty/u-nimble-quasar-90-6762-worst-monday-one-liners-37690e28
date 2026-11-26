import os
from pathlib import Path

ENTRY = "I opened Monday's first email at 9:00; by 9:07 it had become a task force, a spreadsheet, and a recurring meeting."


def write_entry(output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


def resolve_output_dir():
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    write_entry(resolve_output_dir())


if __name__ == "__main__":
    main()
