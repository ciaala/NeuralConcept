from unittest.mock import Mock, create_autospec

import pytest

from app.model.filter.Filter2 import FilterBase, MatchExtensionFilter, AndOperationFilter, HigherThanSizeFilter, LowerThanSizeFilter, OrOperationFilter
#
# from app.model.filter.AndOperationFilter import AndOperationFilter
# from app.model.filter.FilterBase import FilterBase
# from app.model.filter.HigherThanSizeFilter import HigherThanSizeFilter
# from app.model.filter.LowerThanSizeFilter import LowerThanSizeFilter
# from app.model.filter.MatchExtensionFilter import MatchExtensionFilter
# from app.model.filter.OrOperationFilter import OrOperationFilter
from app.service.filesystem.FileSystemService import FileSystemService
from app.service.filesystem.FileSystemItem import FileSystemItem
from app.service.filter.FilterService import FilterService


@pytest.fixture
def mock_file_system_service():
    # Create an autospec of the FileSystemService to ensure interface correctness
    return create_autospec(FileSystemService)


@pytest.fixture
def mock_filter():
    # Mock the Filter object
    filter_mock = Mock(spec=FilterBase)
    return filter_mock


def test_filter_service_can_filter(mock_file_system_service, mock_filter) -> None:
    # Setup mock behavior for FileSystemService
    mock_files = [
        FileSystemItem(filename="file1.txt", size=100),
        FileSystemItem(filename="file2.txt", size=200),
    ]
    mock_file_system_service.list.return_value = mock_files

    # Setup the mock Filter to only apply (return True) for the first file
    def mock_apply(file: FileSystemItem):
        return file.filename == "file1.txt"

    mock_filter.apply.side_effect = mock_apply

    # Instantiate the FilterService with the mocked FileSystemService
    filter_service = FilterService(filesystem_service=mock_file_system_service)

    # Call the filter method
    path = "/mock/path"
    filtered_files = filter_service.filter(mock_filter, path)

    # Expected result should only contain the filename of the file that passes the filter
    expected_files = ["file1.txt"]

    assert filtered_files == expected_files, "FilterService did not filter files as expected"

    # Verify interactions with the mock objects
    mock_file_system_service.list.assert_called_once_with(path)
    assert mock_filter.apply.call_count == len(mock_files), "Filter.apply was not called the expected number of times"


def test_filter_service_with_real_filter(mock_file_system_service, mock_filter) -> None:
    # Setup mock behavior for FileSystemService
    mock_files = [
        FileSystemItem(filename="file1.txt", size=100),
        FileSystemItem(filename="file2.txt", size=200),
        FileSystemItem(filename="image.png", size=200),
    ]
    mock_file_system_service.list.return_value = mock_files

    # Setup a real filter
    filter = AndOperationFilter(operands=[HigherThanSizeFilter(size=199), MatchExtensionFilter(extension="png")])

    # Instantiate the FilterService with the mocked FileSystemService
    filter_service = FilterService(filesystem_service=mock_file_system_service)

    # Call the filter method
    path = "/mock/path"
    filtered_files = filter_service.filter(filter, path)

    # Expected result should only contain the filename of the file that passes the filter
    expected_files = ["image.png"]

    assert filtered_files == expected_files, "FilterService did not filter files as expected"

    # Verify interactions with the mock objects
    mock_file_system_service.list.assert_called_once_with(path)


def test_filter_service_with_complex_filter(mock_file_system_service, mock_filter) -> None:
    # Setup mock behavior for FileSystemService
    mock_files = [
        FileSystemItem(filename="file1.txt", size=100),
        FileSystemItem(filename="file2.txt", size=200),
        FileSystemItem(filename="image.png", size=200),
    ]
    mock_file_system_service.list.return_value = mock_files

    # Setup a real filter
    filter = OrOperationFilter(
        operands=[AndOperationFilter(operands=[HigherThanSizeFilter(size=199), MatchExtensionFilter(extension="png")]),
                  LowerThanSizeFilter(size=101)])

    # Instantiate the FilterService with the mocked FileSystemService
    filter_service = FilterService(filesystem_service=mock_file_system_service)

    # Call the filter method
    path = "/mock/path"
    filtered_files = filter_service.filter(filter, path)

    # Expected result should only contain the filename of the file that passes the filter
    expected_files = ["file1.txt", "image.png"]

    assert filtered_files == expected_files, "FilterService did not filter files as expected"

    # Verify interactions with the mock objects
    mock_file_system_service.list.assert_called_once_with(path)
