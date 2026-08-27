
# File Organizer CLI

A simple Python command-line tool that organizes files into folders based on their file type.

## Features

- Organizes files automatically
- Supports images, documents, audio, videos and archives
- Unknown file types are placed in `Others`
- Handles duplicate filenames safely
- Handles missing folders
- Handles invalid paths
- Handles permission and operating-system errors
- Includes automated tests

## Supported File Types

| Category | Extensions |
|---|---|
| Images | `.jpg`, `.jpeg`, `.png`, `.gif` |
| Documents | `.pdf`, `.doc`, `.docx`, `.txt`, `.csv` |
| Audio | `.mp3`, `.wav` |
| Videos | `.mp4`, `.mkv` |
| Archives | `.zip`, `.rar` |
| Others | Any unsupported extension |

## How to Use

Run the following command:

```bash
python organizer.py /path/to/folder