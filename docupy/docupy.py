from .src import (
    collect_functions_and_docstrings,
    find_subfolders_and_modules,
    generate_documentation,
)


class DocuPy:
    def __init__(self, root_folder_path):
        self.root_folder_path = root_folder_path
        self.subfolders, self.modules = find_subfolders_and_modules(root_folder_path)
        self.functions_docstrings = collect_functions_and_docstrings(self.modules)
        self.documentation = generate_documentation(
            self.subfolders, self.functions_docstrings
        )

    def __repr__(self):
        return f"DocuPy(root_folder_path={self.root_folder_path})"


# Main function to orchestrate the process
def main(root_folder_path):
    subfolders, modules = find_subfolders_and_modules(root_folder_path)
    functions_docstrings = collect_functions_and_docstrings(modules)
    documentation = generate_documentation(subfolders, functions_docstrings)
    return documentation
