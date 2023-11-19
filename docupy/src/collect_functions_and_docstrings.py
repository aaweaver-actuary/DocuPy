import ast


def collect_functions_and_docstrings(module_paths: list) -> dict:
    """Utility function to collect functions and docstrings from modules.

    Parameters
    ----------
    module_paths : list
        List of paths to modules.

    Returns
    -------
    dict
        Dictionary with functions and docstrings.

    Raises
    ------
    TypeError
        If module_paths is not a list.

    Examples
    --------
    >>> from docupy import collect_functions_and_docstrings
    >>> module_paths = ["docupy/src/collect_functions_and_docstrings.py"]
    >>> collect_functions_and_docstrings(module_paths)
    {'collect_functions_and_docstrings': 'Utility function to collect functions and docstrings from modules.'}
    """
    # Check if module_paths is a list
    if not isinstance(module_paths, list):
        raise TypeError("module_paths must be a list.")

    # Initialize dictionary to store collected data
    collected_data = {}

    # Iterate over module paths in module_paths list
    for module_path in module_paths:
        with open(module_path, "r") as file:
            module_content = file.read()

        # For each file, parse the content into an AST (Abstract Syntax Tree)
        tree = ast.parse(module_content)

        # Iterate over nodes in the AST
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                function_name = node.name  # Get function name
                docstring = ast.get_docstring(node)  # Get docstring

                # Store function name and docstring in collected_data dictionary
                collected_data[function_name] = docstring if docstring else ""

    return collected_data
