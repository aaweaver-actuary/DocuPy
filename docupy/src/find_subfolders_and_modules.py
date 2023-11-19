import os


def find_subfolders_and_modules(root_folder: str) -> tuple:
    """Utility function to find subfolders and modules from a root folder.

    Parameters
    ----------
    root_folder : str
        Path to root folder.

    Returns
    -------
    tuple
        Tuple with subfolders and modules.

    Raises
    ------
    TypeError
        If root_folder is not a string.

    Examples
    --------
    >>> from docupy import find_subfolders_and_modules
    >>> root_folder = "docupy"
    >>> find_subfolders_and_modules(root_folder)
    (['docupy/src'], ['docupy/__init__.py', 'docupy/src/__init__.py', 'docupy/src/collect_functions_and_docstrings.py', 'docupy/src/find_subfolders_and_modules.py'])
    """
    # Check if root_folder is a string
    if not isinstance(root_folder, str):
        raise TypeError("root_folder must be a string.")

    # Initialize lists to store subfolders and modules
    subfolders = []
    modules = []

    # Walk through the root folder
    for root, dirs, files in os.walk(root_folder):
        # Add subfolders and modules to lists
        for name in dirs:
            subfolders.append(os.path.join(root, name))
        for file in files:
            if file.endswith(".py"):  # Only add Python files
                modules.append(os.path.join(root, file))

    return subfolders, modules
