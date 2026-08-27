from pathlib import Path
import shutil
import argparse


CATEGORIES = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".csv": "Documents",
    ".mp3": "Audio",
    ".wav": "Audio",
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".zip": "Archives",
    ".rar": "Archives",
}


def get_category(file_path):
    return CATEGORIES.get(file_path.suffix.lower(), "Others")


def unique_destination(destination):
    if not destination.exists():
        return destination

    counter = 1

    while True:
        new_name = f"{destination.stem}_{counter}{destination.suffix}"
        new_destination = destination.parent / new_name

        if not new_destination.exists():
            return new_destination

        counter += 1


def organize_folder(folder):
    folder = Path(folder)

    if not folder.exists():
        print(f"Error: Folder does not exist: {folder}")
        return False

    if not folder.is_dir():
        print(f"Error: Not a folder: {folder}")
        return False

    files = [item for item in folder.iterdir() if item.is_file()]

    if not files:
        print("No files found to organize.")
        return True

    moved = 0

    for file_path in files:
        category = get_category(file_path)
        category_folder = folder / category

        try:
            category_folder.mkdir(exist_ok=True)

            destination = unique_destination(
                category_folder / file_path.name
            )

            shutil.move(str(file_path), str(destination))

            print(f"Moved: {file_path.name} -> {category}/")
            moved += 1

        except PermissionError:
            print(f"Permission denied: {file_path.name}")

        except OSError as error:
            print(f"Could not move {file_path.name}: {error}")

    print(f"\nDone. Organized {moved} file(s).")
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Organize files in a folder by file type."
    )

    parser.add_argument(
        "folder",
        help="Path to the folder you want to organize"
    )

    args = parser.parse_args()

    organize_folder(args.folder)


if __name__ == "__main__":
    main()