import os


ENTRY_TEXT = "By Monday noon I'd fixed the outage, then learned the cause was a cron job I named 'temporary' in March."


def entry_text():
    return ENTRY_TEXT


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as entry_file:
        entry_file.write(entry_text())


if __name__ == "__main__":
    main()
