import os
import shutil


def create_test_structure(base_path: str = None, structure: dict = None) -> None:
    """Utility function to create a test structure of folders and files.

    Takes a base path and a dictionary with the structure to create. Loops through
    the dictionary, starting at the base path, and creates the structure. If the value
    of a key is a dictionary, it creates a folder, recursively calling the function
    to create the folder structure inside the folder. If the value is a string, it
    creates a file with the string as content.

    Parameters
    ----------
    base_path : str, optional
        Base path for the test structure. If None, defaults to the current working
        directory.
    structure : dict, optional
        Dictionary with the structure to create. If None, defaults to a default
        structure:
            ```structure = {
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
            }```

    Returns
    -------
    None
        Creates the test file structure, but does not return anything.

    Raises
    ------
    TypeError
        If base_path is not a string or structure is not a dictionary.

    Examples
    --------
    >>> from docupy.src.util_for_testing import create_test_structure
    >>> base_path = "/pathToTest"
    >>> structure = {
    ...     "folder1": {
    ...         "folder2": {
    ...             "file1.py": "content1",
    ...             "file2.py": "content2",
    ...         },
    ...         "file3.py": "content3",
    ...     },
    ...     "folder3": {
    ...         "file4.py": "content4",
    ...     },
    ...     "file5.py": "content5",
    ... }
    >>> create_test_structure(base_path, structure)
    >>> os.listdir("/pathToTest")
    ['folder1', 'folder3', 'file5.py']
    >>> os.listdir("/pathToTest/folder1")
    ['folder2', 'file3.py']
    >>> os.listdir("/pathToTest/folder1/folder2")
    ['file1.py', 'file2.py']
    >>> with open("/pathToTest/folder1/folder2/file1.py") as file:
    ...     print(file.read())
    content1
    >>> with open("/pathToTest/folder1/folder2/file2.py") as file:
    ...     print(file.read())
    content2
    >>> with open("/pathToTest/folder1/file3.py") as file:
    ...     print(file.read())
    content3
    >>> with open("/pathToTest/folder3/file4.py") as file:
    ...     print(file.read())
    content4
    >>> with open("/pathToTest/file5.py") as file:
    ...     print(file.read())
    content5
    """
    # Check if base_path is a string
    if not isinstance(base_path, str):
        raise TypeError("base_path must be a string.")

    # Check if structure is a dictionary
    if not isinstance(structure, dict):
        raise TypeError("structure must be a dictionary.")

    # Loop through the structure dictionary
    for name, content in structure.items():
        path = os.path.join(base_path, name)  # Create path

        # If content is a dictionary, create a folder
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)

            # Recursively call the function to create the folder
            # structure inside the folder
            create_test_structure(path, content)

        # If content is a string, create a file
        else:
            with open(path, "w") as file:
                file.write(content)


def delete_test_structure(base_path: str) -> None:
    """Utility function to delete a test structure of folders and files.

    Cleans up the test file structure created by create_test_structure() after
    running the tests.

    Parameters
    ----------
    base_path : str
        Base path for the test structure.

    Returns
    -------
    None
        Deletes the test file structure, but does not return anything.

    Raises
    ------
    TypeError
        If base_path is not a string.

    Examples
    --------
    >>> from docupy.src.util_for_testing import create_test_structure, delete_test_structure
    >>> base_path = "/pathToTest"
    >>> structure = {
    ...     "folder1": {
    ...         "folder2": {
    ...             "file1.py": "content1",
    ...             "file2.py": "content2",
    ...         },
    ...         "file3.py": "content3",
    ...     },
    ...     "folder3": {
    ...         "file4.py": "content4",
    ...     },
    ...     "file5.py": "content5",
    ... }
    >>> create_test_structure(base_path, structure)
    >>> os.listdir("/pathToTest")
    ['folder1', 'folder3', 'file5.py']
    >>> delete_test_structure(base_path)
    >>> os.listdir("/pathToTest")
    []
    """
    # Check if base_path is a string
    if not isinstance(base_path, str):
        raise TypeError("base_path must be a string.")

    # Delete the test structure
    shutil.rmtree(base_path, ignore_errors=True)
