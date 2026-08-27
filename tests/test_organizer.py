import pytest
from pathlib import Path

from organizer import get_category, unique_destination, organize_folder


def test_get_category():
    assert get_category(Path("photo.jpg")) == "Images"
    assert get_category(Path("document.pdf")) == "Documents"
    assert get_category(Path("song.mp3")) == "Audio"
    assert get_category(Path("unknown.xyz")) == "Others"


def test_unique_destination(tmp_path):
    file_path = tmp_path / "test.txt"
    file_path.write_text("first")

    result = unique_destination(file_path)

    assert result != file_path
    assert result.name == "test_1.txt"


def test_organize_folder(tmp_path):
    (tmp_path / "photo.jpg").write_text("image")
    (tmp_path / "document.pdf").write_text("document")
    (tmp_path / "song.mp3").write_text("audio")

    result = organize_folder(tmp_path)

    assert result is True
    assert (tmp_path / "Images" / "photo.jpg").exists()
    assert (tmp_path / "Documents" / "document.pdf").exists()
    assert (tmp_path / "Audio" / "song.mp3").exists()


def test_empty_folder(tmp_path):
    result = organize_folder(tmp_path)

    assert result is True


def test_missing_folder(tmp_path):
    missing_folder = tmp_path / "does_not_exist"

    result = organize_folder(missing_folder)

    assert result is False