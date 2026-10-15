
from pathlib import Path
import argparse
import shutil


FILE_TYPES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"},
    "PDFs": {".pdf"},
    "Documents": {".doc", ".docx", ".odt", ".rtf"},
    "Spreadsheets": {".xls", ".xlsx", ".csv", ".ods"},
    "Text": {".txt"},
    "Archives": {".zip", ".tar", ".gz", ".7z"},
    "Audio": {".mp3", ".wav", ".ogg"},
    "Videos": {".mp4", ".mkv", ".mov", ".avi"},
}


def get_category(file_path):
    """Return the destination folder for a supported file."""
    extension = file_path.suffix.lower()

    for category, extensions in FILE_TYPES.items():
        if extension in extensions:
            return category

    return None


def get_unique_path(destination):
    """Avoid overwriting a file with the same name."""
    if not destination.exists():
        return destination

    counter = 1

    while True:
        candidate = (
            destination.parent
            / f"{destination.stem}_{counter}{destination.suffix}"
        )

        if not candidate.exists():
            return candidate

        counter += 1


def organize_directory(directory, apply=False):
    """Preview or organize supported files in one directory."""
    folder = Path(directory).expanduser().resolve()

    if not folder.exists() or not folder.is_dir():
        raise ValueError("Please provide an existing directory.")

    actions = []

    # Only inspect files directly inside the selected directory.
    for file_path in sorted(folder.iterdir()):
        if not file_path.is_file():
            continue

        category = get_category(file_path)

        # Leave unsupported file types untouched.
        if category is None:
            continue

        destination_folder = folder / category
        destination = get_unique_path(
            destination_folder / file_path.name
        )

        actions.append((file_path, destination))

        if apply:
            destination_folder.mkdir(exist_ok=True)
            shutil.move(str(file_path), str(destination))

    return actions


def main():
    parser = argparse.ArgumentParser(
        description="Organize files by their extensions."
    )
    parser.add_argument(
        "directory",
        help="Path to the directory you want to organize",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually move files; without this option, preview only",
    )

    args = parser.parse_args()

    try:
        actions = organize_directory(
            args.directory,
            apply=args.apply,
        )
    except (ValueError, OSError) as error:
        parser.error(str(error))

    if not actions:
        print("No supported files found.")
        return

    for source, destination in actions:
        print(f"{source.name} -> {destination.parent.name}/"
              f"{destination.name}")

    if args.apply:
        print(f"\nDone. Organized {len(actions)} file(s).")
    else:
        print(f"\nPreview only: {len(actions)} file(s) would be moved.")
        print("Run again with --apply to move the files.")


if __name__ == "__main__":
    main()
