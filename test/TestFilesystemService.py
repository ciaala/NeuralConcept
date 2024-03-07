from dataclasses import dataclass
from typing import List
import os
import pytest
from unittest.mock import MagicMock

from app.service.filesystem.FileSystemService import FileSystemService, FileSystemItem



@dataclass
class MockedFile:
    name: str
    size: int


@pytest.fixture
def mock_os_functions(mocker):
    mocked_listdir = mocker.patch('os.listdir')
    mocked_isfile = mocker.patch('os.path.isfile')
    mocked_getsize = mocker.patch('os.path.getsize')
    return mocked_listdir, mocked_isfile, mocked_getsize


def test_list_files_in_directory(mock_os_functions):
    mock_listdir, mock_isfile, mock_getsize = mock_os_functions

    # Setup mock behavior
    mock_path = "/mock/path"
    mock_files = [
        MockedFile(name="file1.txt", size=100),
        MockedFile(name="file2.txt", size=200),
    ]

    mock_listdir.return_value = [file.name for file in mock_files]
    mock_isfile.side_effect = lambda path: any(file.name in path for file in mock_files)
    mock_getsize.side_effect = lambda path: next(file.size for file in mock_files if file.name in path)

    # Instantiate your service
    service = FileSystemService()

    # Call the method under test
    result = service.list(mock_path)

    # Verify the result
    expected = [FileSystemItem(filename=file.name, size=file.size) for file in mock_files]
    assert result == expected, "The list method did not return the expected list of FileSystemItem instances"
