"""
Board Explorer utilities for PyScript version.
Helper functions for formatting and displaying board data.
"""

def format_board_name(port, board):
    """Format board display name consistently."""
    if not board or board == "":
        return port.rstrip("-")
    
    if board.startswith("esp-"):
        return board[4:]  # Remove "esp-" prefix
    
    return board


def get_board_key(port, board):
    """Get full board key for URL/comparison purposes."""
    return f"{port}-{board}"


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


def format_module_summary(class_count, func_count, const_count, module_name=""):
    """Format module summary counts (suppressing zero counts)."""
    parts = []
    if class_count > 0:
        parts.append(f"{class_count} classes")
    if func_count > 0:
        parts.append(f"{func_count} functions")
    if const_count > 0:
        parts.append(f"{const_count} constants")
    
    if len(parts) > 0:
        return ", ".join(parts)
    
    # Check if it's a deprecated u-module
    if module_name.startswith("u") and len(module_name) > 1:
        base_name = module_name[1:]  # Remove 'u' prefix
        return f"deprecated - use {base_name} instead"
    
    return "empty module"


def format_method_signature(method):
    """Format method/function signature with parameters."""
    signature = method["name"]
    
    # Build parameter list
    params = []
    if "parameters" in method and method["parameters"]:
        for param in method["parameters"]:
            param_str = param["name"]
            
            # Add type hint if available
            if param.get("type_hint") and param["type_hint"] not in ("None", ""):
                param_str += f": {param['type_hint']}"
            
            # Add default value if available
            if param.get("default_value") and param["default_value"] != "None":
                param_str += f" = {param['default_value']}"
            elif param.get("is_optional"):
                param_str += " = None"
            
            # Handle variadic parameters
            if param.get("is_variadic"):
                if param["name"] == "kwargs":
                    param_str = "**" + param_str
                else:
                    param_str = "*" + param_str
            
            params.append(param_str)
    
    signature += f"({', '.join(params)})"
    
    # Add return type if available
    if method.get("return_type") and method["return_type"] not in ("None", "", "Any"):
        signature += f" -> {method['return_type']}"
    
    return signature


def create_icon_html(icon_type):
    """Create Font Awesome icon HTML."""
    icons = {
        "module": "fas fa-cube",
        "class": "fas fa-object-group",
        "function": "fas fa-bolt",
        "method": "fas fa-bolt",
        "property": "fas fa-ellipsis",
        "constant": "fas fa-circle",
        "variable": "fas fa-circle-dot"
    }
    
    fa_class = icons.get(icon_type, "fas fa-cube")
    return f'<i class="{fa_class}" style="margin-right: 8px;"></i>'


def build_module_tree_html(modules, show_details=True):
    """
    Build HTML for module tree with optional class/method details.
    
    Args:
        modules: List of module dictionaries with classes, functions, constants
        show_details: If True, show expandable class/method tree
    
    Returns:
        HTML string for module tree
    """
    html = ""
    
    for module in modules:
        class_count = len(module.get("classes", []))
        func_count = len(module.get("functions", []))
        const_count = len(module.get("constants", []))
        
        is_deprecated = module["name"].startswith("u") and len(module["name"]) > 1 and \
                       (class_count + func_count + const_count) == 0
        
        summary = format_module_summary(class_count, func_count, const_count, module["name"])
        
        html += f'''
        <div class="tree-item">
            <div class="tree-node" onclick="toggleModule('module-{module["name"]}')" 
                 style="cursor: pointer; padding: 12px; background: #f8f9fa; border-radius: 8px; margin-bottom: 6px; border-left: 4px solid #667eea;">
                {create_icon_html("module")}
                <strong style="font-size: 1.1em;">{module["name"]}</strong>
                <span style="margin-left: auto; color: #666; font-size: 0.9em; background: #e9ecef; padding: 4px 8px; border-radius: 12px;">
                    {summary}
                </span>
            </div>
        '''
        
        if show_details and (class_count > 0 or func_count > 0 or const_count > 0):
            html += f'<div id="module-{module["name"]}" class="tree-children" style="display: none; margin-left: 24px; border-left: 3px solid #667eea; padding-left: 20px; margin-top: 8px;">'
            
            # Add classes
            for cls in module.get("classes", []):
                method_count = len(cls.get("methods", []))
                attr_count = len(cls.get("attributes", []))
                
                base_classes = cls.get("base_classes", [])
                base_str = f"({', '.join(base_classes)})" if base_classes else ""
                
                html += f'''
                <div class="tree-item">
                    <div class="tree-node" style="padding: 10px; background: #fff; border-radius: 6px; margin-bottom: 4px; border-left: 4px solid #e3f2fd;">
                        {create_icon_html("class")}
                        <span style="font-weight: 600;">class {cls["name"]}{base_str}</span>
                        <span style="margin-left: auto; color: #6c757d; font-size: 0.85em;">{method_count} methods, {attr_count} attrs</span>
                    </div>
                </div>
                '''
            
            # Add functions
            for func in module.get("functions", []):
                sig = format_method_signature(func)
                html += f'''
                <div class="tree-item">
                    <div class="tree-node" style="padding: 8px; background: #fff; border-radius: 6px; margin-bottom: 4px;">
                        {create_icon_html("function")}
                        <code style="font-family: 'Courier New', monospace; font-size: 0.9em;">{sig}</code>
                    </div>
                </div>
                '''
            
            # Add constants
            for const in module.get("constants", []):
                value_str = f" = {const['value']}" if const.get("value") else ""
                html += f'''
                <div class="tree-item">
                    <div class="tree-node" style="padding: 8px; background: #fff; border-radius: 6px; margin-bottom: 4px;">
                        {create_icon_html("constant")}
                        <code style="font-family: 'Courier New', monospace; font-size: 0.9em;">{const["name"]}{value_str}</code>
                    </div>
                </div>
                '''
            
            html += '</div>'
        
        html += '</div>'
    
    return html
