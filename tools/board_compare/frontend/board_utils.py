"""
Board Explorer utilities for PyScript version.
Helper functions for formatting and displaying board data.
"""


def format_board_name(port, board):
    """Format board display name consistently."""
    # print(f"format_board_name called with port={port}, board={board}")
    if not board or board == "":
        return port.rstrip("-")
    # FIXME : Is too port specific
    if board.startswith("esp-"):
        return board[4:]  # Remove "esp-" prefix

    return board


def find_board_in_list(boards, version, board_name):
    """
    Find a board in the list matching version and formatted name.
    Returns tuple (port, board) or None if not found.
    """
    for b in boards:
        if b["version"] == version:
            formatted = format_board_name(b["port"], b["board"])
            if formatted == board_name:
                return (b["port"], b["board"])
    return None


def get_icon_class(icon_type):
    """Get Font Awesome icon class for different entity types."""
    icons = {
        "module": "fas fa-cube",
        "class": "fas fa-object-group",
        "function": "fas fa-bolt",
        "method": "fas fa-bolt",
        "property": "fas fa-ellipsis",
        "constant": "fas fa-circle",
        "variable": "fas fa-circle-dot",
    }
    return icons.get(icon_type, "fas fa-cube")


# Dead code
# def get_board_key(port, board):
#     """Get full board key for URL/comparison purposes."""
#     return f"{port}-{board}".rstrip("-")


# def format_module_summary(class_count, func_count, const_count, module_name=""):
#     """Format module summary counts (suppressing zero counts)."""
#     parts = []
#     if class_count > 0:
#         parts.append(f"{class_count} classes")
#     if func_count > 0:
#         parts.append(f"{func_count} functions")
#     if const_count > 0:
#         parts.append(f"{const_count} constants")

#     if len(parts) > 0:
#         return ", ".join(parts)

#     # Check if it's a deprecated u-module
#     if module_name.startswith("u") and len(module_name) > 1:
#         base_name = module_name[1:]  # Remove 'u' prefix
#         return f"deprecated - use {base_name} instead"

#     return "empty module"


# def format_method_signature(method):
#     """Format method/function signature with parameters."""
#     signature = method["name"]

#     # Build parameter list
#     params = []
#     if "parameters" in method and method["parameters"]:
#         for param in method["parameters"]:
#             param_str = param["name"]

#             # Add type hint if available
#             if param.get("type_hint") and param["type_hint"] not in ("None", ""):
#                 param_str += f": {param['type_hint']}"

#             # Add default value if available
#             if param.get("default_value") and param["default_value"] != "None":
#                 param_str += f" = {param['default_value']}"
#             elif param.get("is_optional"):
#                 param_str += " = None"

#             # Handle variadic parameters
#             if param.get("is_variadic"):
#                 if param["name"] == "kwargs":
#                     param_str = "**" + param_str
#                 else:
#                     param_str = "*" + param_str

#             params.append(param_str)

#     signature += f"({', '.join(params)})"

#     # Add return type if available
#     if method.get("return_type") and method["return_type"] not in ("None", "", "Any"):
#         signature += f" -> {method['return_type']}"

#     return signature
