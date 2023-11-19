import os
from docupy import DocuPy
from .util_for_testing import create_test_structure, delete_test_structure


def test_empty_directory():
    """Test function for empty directory."""
    test_base_path = "./empty_test_path/"
    os.makedirs(test_base_path, exist_ok=True)

    dp = DocuPy(test_base_path)

    assert dp.subfolders == [], f"Expected empty list, got {dp.subfolders}"
    assert dp.modules == [], f"Expected empty list, got {dp.modules}"
    assert (
        dp.functions_docstrings == {}
    ), f"Expected empty dict, got {dp.functions_docstrings}"
    assert (
        dp.root_folder_path == test_base_path
    ), f"Expected {test_base_path}, got {dp.root_folder_path}"
    assert (
        dp.documentation == "<p class='no-data'>No modules or functions found.</p>"
    ), f"Expected <p class='no-data'>No modules or functions found.</p>, got {dp.documentation}"
    assert (
        dp.__repr__() == f"DocuPy(root_folder_path={test_base_path})"
    ), f"Expected DocuPy(root_folder_path={test_base_path}), got {dp.__repr__()}"
    assert (
        dp.__str__() == f"DocuPy(root_folder_path={test_base_path})"
    ), f"Expected DocuPy(root_folder_path={test_base_path}), got {dp.__str__()}"

    delete_test_structure(test_base_path)

    assert not os.path.exists(
        test_base_path
    ), f"Expected {test_base_path} to be deleted, but it still exists."


def test_directory_with_subfolders_only():
    """Test function for directory with only subfolders."""
    test_base_path = "./subfolder_only_test_path/"
    test_structure = {"subfolder1": {}, "subfolder2": {}}
    create_test_structure(test_base_path, test_structure)

    dp = DocuPy(test_base_path)

    assert (
        len(dp.subfolders) == 2
    ), f"Expected 2 subfolders, got {len(dp.subfolders)}:\n{dp.subfolders}"
    assert (
        len(dp.modules) == 0
    ), f"Expected 0 modules, got {len(dp.modules)}:\n{dp.modules}"
    assert (
        dp.root_folder_path == test_base_path
    ), f"Expected {test_base_path}, got {dp.root_folder_path}"
    assert dp.subfolders[0] == os.path.join(
        test_base_path, "subfolder1"
    ), f"Expected {os.path.join(test_base_path, 'subfolder1')}, got {dp.subfolders[0]}"
    assert dp.subfolders[1] == os.path.join(
        test_base_path, "subfolder2"
    ), f"Expected {os.path.join(test_base_path, 'subfolder2')}, got {dp.subfolders[1]}"

    delete_test_structure(test_base_path)

    assert not os.path.exists(
        test_base_path
    ), f"Expected {test_base_path} to be deleted, but it still exists."


def test_directory_with_modules_only():
    """Test function for directory with only Python modules."""
    test_base_path = "./test_only_python_modules"

    test_structure = {
        "module1.py": """def function_one():
            \"\"\"Docstring for function one.\"\"\"
                pass""",
        "module2.py": """def function_two():
            \"\"\"Docstring for function two.\"\"\"
                pass""",
    }

    create_test_structure(test_base_path, test_structure)

    dp = DocuPy(test_base_path)

    assert (
        len(dp.subfolders) == 0
    ), f"Expected 0 subfolders, got {len(dp.subfolders)}:\n{dp.subfolders}"
    assert (
        len(dp.modules) == 2
    ), f"Expected 2 modules, got {len(dp.modules)}:\n{dp.modules}"
    assert (
        dp.root_folder_path == test_base_path
    ), f"Expected {test_base_path}, got {dp.root_folder_path}"
    assert (
        len(dp.functions_docstrings.keys()) == 2
    ), f"Expected 2 functions with docstrings, got {len(dp.functions_docstrings.keys())}:\n{dp.functions_docstrings.keys()}"
    assert (
        "function_one" in dp.functions_docstrings.keys()
    ), f"Expected function_one in functions_docstrings, but it was not found:\n{dp.functions_docstrings.keys()}"
    assert (
        "function_two" in dp.functions_docstrings.keys()
    ), f"Expected function_two in functions_docstrings, but it was not found:\n{dp.functions_docstrings.keys()}"
    assert (
        dp.functions_docstrings["function_one"] == "Docstring for function one."
    ), f"Expected 'Docstring for function one.', got {dp.functions_docstrings['function_one']}"
    assert (
        dp.functions_docstrings["function_two"] == "Docstring for function two."
    ), f"Expected 'Docstring for function two.', got {dp.functions_docstrings['function_two']}"
    assert (
        dp.documentation
        == "<h3 class='module-name'>module1.py:</h3><p>function_one: Docstring for function one.</p><h3 class='module-name'>module2.py:</h3><p>function_two: Docstring for function two.</p>"
    ), f"Expected <h3 class='module-name'>module1.py:</h3><p>function_one: Docstring for function one.</p><h3 class='module-name'>module2.py:</h3><p>function_two: Docstring for function two.</p>\n\nGot {dp.documentation}"
    assert (
        dp.__repr__() == f"DocuPy(root_folder_path={test_base_path})"
    ), f"Expected DocuPy(root_folder_path={test_base_path}), got {dp.__repr__()}"

    delete_test_structure(test_base_path)

    assert not os.path.exists(
        test_base_path
    ), f"Expected {test_base_path} to be deleted, but it still exists."


# Test function for directory with subfolders and Python modules


def test_directory_with_subfolders_and_modules():
    """Test function for directory with subfolders and Python modules."""
    test_base_path = "./test_subfolders_and_python_modules"

    test_structure = {
        "subfolder1": {
            "module1.py": """def function_one():
                \"\"\"Docstring for function one.\"\"\"
                pass""",
            "module2.py": """def function_two():
                \"\"\"Docstring for function two.\"\"\"
                pass""",
        },
        "subfolder2": {
            "module3.py": """def function_three():
            \"\"\"Docstring for function three.\"\"\"
            pass""",
            "subfolder3": {
                "module4.py": """def function_four():
                \"\"\"Docstring for function four.\"\"\"
                pass"""
            },
        },
        "module5.py": """def function_five():
        \"\"\"Docstring for function five.\"\"\"
        pass""",
    }

    create_test_structure(test_base_path, test_structure)

    dp = DocuPy(test_base_path)

    expected_html = (
        """
    <h2 class='subfolders-header'>Subfolders:</h2>
        <h3 class='module-name'>subfolder1:</h3>
            <h3 class='module-name'>module1.py:</h3>
                <p>function_one: Docstring for function one.</p>
            <h3 class='module-name'>module2.py:</h3>
                <p>function_two: Docstring for function two.</p>
        <h3 class='module-name'>subfolder2:</h3>
            <h3 class='module-name'>module3.py:</h3>
                <p>function_three: Docstring for function three.</p>
            <h3 class='module-name'>subfolder3:</h3>
                <h3 class='module-name'>module4.py:</h3>
                    <p>function_four: Docstring for function four.</p>
        <h3 class='module-name'>module5.py:</h3>
            <p>function_five: Docstring for function five.</p>
    """.replace("\n", "")
        .replace("    ", "")
        .replace("  ", "")
    )

    assert (
        dp.documentation == expected_html
    ), f"Expected {expected_html}, got {dp.documentation}"

    delete_test_structure(test_base_path)

    assert not os.path.exists(
        test_base_path
    ), f"Expected {test_base_path} to be deleted, but it still exists."


# Test function for modules with no functions


def test_modules_with_no_functions():
    """Test function for modules with no functions."""
    test_base_path = "./test_modules_with_no_functions"
    test_structure = {"empty_module.py": "# No functions here"}

    create_test_structure(test_base_path, test_structure)

    dp = DocuPy(test_base_path)

    expected_html = "<p class='no-data'>No modules or functions found.</p>"

    assert (
        dp.documentation == expected_html
    ), f"Expected {expected_html}, got {dp.documentation}"

    delete_test_structure(test_base_path)


def test_complex_nested_structure():
    """Test function for complex nested structure."""
    test_base_path = "./initial_test_path"

    test_structure = {
        "subfolder1": {
            "module1.py": """def function_one():
                \"\"\"Docstring for function one.\"\"\"
                pass""",
            "module2.py": """def function_two():
                \"\"\"Docstring for function two.\"\"\"
                pass""",
            "subfolder1A": {
                "module3.py": """def function_three():
                \"\"\"Docstring for function three.\"\"\"
                pass""",
                "subfolder1B": {
                    "module4.py": """def function_four():
                    \"\"\"Docstring for function four.\"\"\"
                    pass"""
                },
            },
        },
        "subfolder2": {},
        "subfolder3": {
            "deep_subfolder3A": {
                "very_deep_subfolder3B": {
                    "really_deep_subfolder3C": {
                        "really_really_deep_subfolder3D": {
                            "module5.py": """def function_five():
                            \"\"\"Docstring for function five.\"\"\"
                            pass"""
                        }
                    }
                }
            }
        },
    }

    create_test_structure(test_base_path, test_structure)

    dp = DocuPy(test_base_path)

    expected_html = (
        """
    <h2 class='subfolders-header'>Subfolders:</h2>
        <h3 class='module-name'>subfolder1:</h3>
            <h3 class='module-name'>module1.py:</h3>
                <p>function_one: Docstring for function one.</p>
            <h3 class='module-name'>module2.py:</h3>
                <p>function_two: Docstring for function two.</p>
            <h3 class='module-name'>subfolder1A:</h3>
                <h3 class='module-name'>module3.py:</h3>
                    <p>function_three: Docstring for function three.</p>
                <h3 class='module-name'>subfolder1B:</h3>
                    <h3 class='module-name'>module4.py:</h3>
                        <p>function_four: Docstring for function four.</p>
        <h3 class='module-name'>subfolder2:</h3>
            <p class='no-data'>No modules or functions found.</p>
        <h3 class='module-name'>subfolder3:</h3>
            <h3 class='module-name'>deep_subfolder3A:</h3>
                <h3 class='module-name'>very_deep_subfolder3B:</h3>
                    <h3 class='module-name'>really_deep_subfolder3C:</h3>
                        <h3 class='module-name'>really_really_deep_subfolder3D:</h3>
                            <h3 class='module-name'>module5.py:</h3>
                                <p>function_five: Docstring for function five.</p>
    """.replace("\n", "")
        .replace("    ", "")
        .replace("  ", "")
    )

    assert (
        dp.documentation == expected_html
    ), f"Expected {expected_html}, got {dp.documentation}"

    delete_test_structure(test_base_path)

    assert not os.path.exists(
        test_base_path
    ), f"Expected {test_base_path} to be deleted, but it still exists."
