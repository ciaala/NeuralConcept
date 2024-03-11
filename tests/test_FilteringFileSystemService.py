import pytest

from app.service.filter.FilteringFileSystemService import FilteringFileSystemService
from app.model.filter.FilterBase import FilterBase
from app.service.filesystem.FileSystemItem import FileSystemItem


@pytest.fixture
def mock_os(mocker):
    listdir_mock = mocker.patch('os.listdir', return_value=['file1.txt', 'file2.txt', "file3.txt" 'dir1'])
    isfile_mock = mocker.patch('os.path.isfile', side_effect=lambda x: not x.endswith('dir1'))
    getsize_mock = mocker.patch('os.path.getsize', side_effect=lambda x: 512 if '3' in x else 1024)
    return listdir_mock, isfile_mock, getsize_mock


@pytest.fixture
def filter_base_mock(mocker):
    mock = mocker.create_autospec(FilterBase, instance=True)
    mock.apply.side_effect = lambda item: item.size > 512  # Example condition
    return mock


def test_filtering_file_system_service(mock_os, filter_base_mock):
    service = FilteringFileSystemService()
    filtered_files = service.filter(filter_base_mock, '/test/path')

    # Assertions
    assert len(filtered_files) == 2
    assert 'file1.txt' in filtered_files
    assert 'file2.txt' in filtered_files
    # Verify that the apply method was called with the expected FileSystemItem
    filter_base_mock.apply.assert_any_call(FileSystemItem(filename='file1.txt', size=1024))
    filter_base_mock.apply.assert_any_call(FileSystemItem(filename='file2.txt', size=1024))
