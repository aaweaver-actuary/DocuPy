# Utility function to generate documentation in HTML format


def generate_documentation(subfolders: list, functions_docstrings: dict) -> str:
    """Utility function to generate documentation in HTML format.

    Parameters
    ----------
    subfolders : list
        List of subfolders.
    functions_docstrings : dict
        Dictionary with functions and docstrings.

    Returns
    -------
    str
        HTML formatted documentation.

    Raises
    ------
    TypeError
        If subfolders is not a list or functions_docstrings is not a dictionary.

    Examples
    --------
    >>> from docupy import generate_documentation
    >>> subfolders = ["docupy/src"]
    >>> functions_docstrings = {"generate_documentation": "Utility function to generate documentation in HTML format."}
    >>> generate_documentation(subfolders, functions_docstrings)
    "<h2 class='subfolders-header'>
        Subfolders:
    </h2>
    <ul class='subfolders-list'>
        <li class='subfolder-item'>
            docupy/src
        </li>
    </ul>
    <h2 class='modules-header'>
        Modules and Functions:
    </h2>
    <div class='module-section'>
        <h3 class='module-name'>
            generate_documentation:
        </h3>
        <p class='function-item'>
            <b>generate_documentation:</b> Utility function to generate documentation in HTML format.
        </p>
    </div>"
    """
    # Check if subfolders is a list
    if not isinstance(subfolders, list):
        raise TypeError("subfolders must be a list.")

    # Check if functions_docstrings is a dictionary
    if not isinstance(functions_docstrings, dict):
        raise TypeError("functions_docstrings must be a dictionary.")

    # If no subfolders and no functions_docstrings, return message
    if not subfolders and not functions_docstrings:
        return "<p class='no-data'>No modules or functions found.</p>"

    # Initialize list to store HTML output
    html_output = []

    # Loop over subfolders and functions_docstrings
    if subfolders:
        # Subfolders get `h2` header and `ul` list
        html_output.append(
            """<h2 class='subfolders-header'>
                    Subfolders:
                </h2>
                <ul class='subfolders-list'>"""
        )

        # Add each subfolder as `li` item
        for subfolder in subfolders:
            html_output.append(
                f"""<li class='subfolder-item'>
                        {subfolder}
                    </li>"""
            )

        # Close `ul` list
        html_output.append("</ul>")

    # Functions and docstrings get `h2` header and `div` section
    if functions_docstrings:
        # `h2` header
        html_output.append(
            """<h2 class='modules-header'>
                    Modules and Functions:
                </h2>"""
        )

        for module, functions in functions_docstrings.items():
            # Add `div` with `h3` header for module name
            html_output.append(
                f"""<div class='module-section'>
                        <h3 class='module-name'>
                            {module}:
                        </h3>"""
            )

            # Add `p` item for each function and docstring
            for function, docstring in functions.items():
                html_output.append(
                    f"""<p class='function-item'>
                            <b>{function}:</b> {docstring}
                        </p>"""
                )

            # Close `div` section
            html_output.append("</div>")

    # Return HTML output as string
    return "".join(html_output)
