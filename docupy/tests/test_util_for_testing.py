import os
import pytest
from .util_for_testing import create_test_structure, delete_test_structure


def test_create_and_delete_test_structure():
    base_path = "/tmp/test"
    structure = {
        "folder1": {
            "folder2": {
                "file1.py": "content1",
                "file2.py": "content2",
            },
            "file3.py": "content3",
        },
        "folder3": {
            "file4.py": "content4",
        },
        "file5.py": "content5",
    }
    create_test_structure(base_path, structure)

    # Add a file outside the structure to test that it is not deleted
    with open("/tmp/file6.py", "w") as file:
        file.write("content6")

    # Test if the structure was created correctly - were all the folders and files created?
    assert os.path.exists(
        "/tmp/test/folder1"
    ), f"folder1 does not exist in {base_path}: {os.listdir(base_path)}"
    assert os.path.exists(
        "/tmp/test/folder1/folder2"
    ), f"folder2 does not exist in {base_path}/folder1: {os.listdir(base_path + '/folder1')}"
    assert os.path.exists(
        "/tmp/test/folder3"
    ), f"folder3 does not exist in {base_path}: {os.listdir(base_path)}"

    assert os.path.exists(
        "/tmp/test/folder1/folder2/file1.py"
    ), f"file1.py does not exist in {base_path}/folder1/folder2: {os.listdir(base_path + '/folder1/folder2')}"
    assert os.path.exists(
        "/tmp/test/folder1/folder2/file2.py"
    ), f"file2.py does not exist in {base_path}/folder1/folder2: {os.listdir(base_path + '/folder1/folder2')}"
    assert os.path.exists(
        "/tmp/test/folder1/file3.py"
    ), f"file3.py does not exist in {base_path}/folder1: {os.listdir(base_path + '/folder1')}"
    assert os.path.exists(
        "/tmp/test/folder3/file4.py"
    ), f"file4.py does not exist in {base_path}/folder3: {os.listdir(base_path + '/folder3')}"
    assert os.path.exists(
        "/tmp/test/file5.py"
    ), f"file5.py does not exist in {base_path}: {os.listdir(base_path)}"
    assert os.path.exists(
        "/tmp/file6.py"
    ), f"file6.py does not exist in /tmp: {os.listdir('/tmp')} - this is fine for create_test_structure() but should be able to be deleted by delete_test_structure()"

    # Test if the structure was created correctly - do the files contain the expected content?
    with open("/tmp/test/folder1/folder2/file1.py") as file:
        assert (
            file.read() == "content1"
        ), f"file1.py does not contain the expected content in {base_path}/folder1/folder2:\nactual:{file.read()}\nexpected:content1"
    with open("/tmp/test/folder1/folder2/file2.py") as file:
        assert (
            file.read() == "content2"
        ), f"file2.py does not contain the expected content in {base_path}/folder1/folder2:\nactual:{file.read()}\nexpected:content2"
    with open("/tmp/test/folder1/file3.py") as file:
        assert (
            file.read() == "content3"
        ), f"file3.py does not contain the expected content in {base_path}/folder1:\nactual:{file.read()}\nexpected:content3"
    with open("/tmp/test/folder3/file4.py") as file:
        assert (
            file.read() == "content4"
        ), f"file4.py does not contain the expected content in {base_path}/folder3:\nactual:{file.read()}\nexpected:content4"
    with open("/tmp/test/file5.py") as file:
        assert (
            file.read() == "content5"
        ), f"file5.py does not contain the expected content in {base_path}:\nactual:{file.read()}\nexpected:content5"

    # Delete the test structure
    delete_test_structure(base_path)

    # Test if the structure was deleted correctly - were all the folders and files deleted?
    assert not os.path.exists(
        "/tmp/test/folder1"
    ), f"folder1 still exists in {base_path}: {os.listdir(base_path)}"
    assert not os.path.exists(
        "/tmp/test/folder1/folder2"
    ), f"folder2 still exists in {base_path}/folder1: {os.listdir(base_path + '/folder1')}"
    assert not os.path.exists(
        "/tmp/test/folder3"
    ), f"folder3 still exists in {base_path}: {os.listdir(base_path)}"
    assert not os.path.exists(
        "/tmp/test/folder1/folder2/file1.py"
    ), f"file1.py still exists in {base_path}/folder1/folder2: {os.listdir(base_path + '/folder1/folder2')}"
    assert not os.path.exists(
        "/tmp/test/folder1/folder2/file2.py"
    ), f"file2.py still exists in {base_path}/folder1/folder2: {os.listdir(base_path + '/folder1/folder2')}"
    assert not os.path.exists(
        "/tmp/test/folder1/file3.py"
    ), f"file3.py still exists in {base_path}/folder1: {os.listdir(base_path + '/folder1')}"
    assert not os.path.exists(
        "/tmp/test/folder3/file4.py"
    ), f"file4.py still exists in {base_path}/folder3: {os.listdir(base_path + '/folder3')}"


def test_create_test_structure_invalid_base_path():
    with pytest.raises(TypeError):
        create_test_structure(123, {})


def test_create_test_structure_invalid_structure():
    with pytest.raises(TypeError):
        create_test_structure("/tmp/test", "not a dict")
