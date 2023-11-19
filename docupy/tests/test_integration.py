# Unit Tests for each component of the project
import os
from docupy import DocuPy
from .util_for_testing import create_test_structure, delete_test_structure


# Test for find_subfolders_and_modules function
def test_find_subfolders_and_modules():
    # Setup a test directory structure
    test_base_path = "/path/to/test_find_subfolders_and_modules"
    test_structure = {"subfolder1": {}, "module1.py": "def function_one(): pass"}
    create_test_structure(test_base_path, test_structure)

    dp = DocuPy(test_base_path)

    # assert len(subfolders) == 1 and "subfolder1" in subfolders[0]
    # assert len(modules) == 1 and "module1.py" in modules[0]
    assert dp.subfolders == [os.path.join(test_base_path, "subfolder1")]
    assert dp.modules == [os.path.join(test_base_path, "module1.py")]
    assert dp.root_folder_path == test_base_path

    delete_test_structure(test_base_path)


# Test for collect_functions_and_docstrings function
def test_collect_functions_and_docstrings():
    test_base_path = "/path/to/test_collect_functions_and_docstrings"
    test_structure = {
        "module1.py": 'def function_one():\\n    \\"\\"\\"Docstring for function one.\\"\\"\\"\\n    pass'
    }
    create_test_structure(test_base_path, test_structure)

    modules = [os.path.join(test_base_path, "module1.py")]
    dp = DocuPy(test_base_path)
    assert dp.functions_docstrings == {"function_one": "Docstring for function one."}

    delete_test_structure(test_base_path)


# Test for generate_documentation function
def test_generate_documentation():
    subfolders = ["/project/subfolder1", "/project/subfolder2"]
    functions_docstrings = {
        "/project/module1.py": {"function_one": "Docstring one."},
        "/project/module2.py": {"function_two": "Docstring two."},
    }
    os.makedirs("/project")
    os.makedirs("/project/subfolder1")
    os.makedirs("/project/subfolder2")
    with open("/project/module1.py", "w") as file:
        file.write("def function_one(): pass")
    with open("/project/module2.py", "w") as file:
        
    dp = DocuPy("/project")
    documentation = generate_documentation(subfolders, functions_docstrings)

    # Check if the output contains expected substrings (simplified check)
    assert "<h2 class='subfolders-header'>Subfolders:</h2>" in documentation
    assert "<h3 class='module-name'>/project/module1.py:</h3>" in documentation
    assert "function_one: Docstring one." in documentation
