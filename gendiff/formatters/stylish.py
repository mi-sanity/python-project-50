DEFAULT_INDENT = 4


def stylish(diff, depth=0):
    tree = []

    for key in diff:
        item = diff[key]
        status = item["status"]
        val = item["value"]
        value = to_str(val, depth)
        indent = " " * (depth * DEFAULT_INDENT)
        prefix = "    "
        prefix_plus = "  + "
        prefix_minus = "  - "

        if status == "unchanged":
            tree.append(f"{indent}{prefix}{key}: {value}")
        elif status == "added":
            tree.append(f"{indent}{prefix_plus}{key}: {value}")
        elif status == "removed":
            tree.append(f"{indent}{prefix_minus}{key}: {value}")
        elif status == "changed":
            old, new = val
            old_value = to_str(old, depth)
            new_value = to_str(new, depth)
            tree.append(f"{indent}{prefix_minus}{key}: {old_value}")
            tree.append(f"{indent}{prefix_plus}{key}: {new_value}")
        elif status == "nested":
            tree.append(
                f"{indent}{prefix}{key}: {stylish(val, depth + 1)}"
            )
    format = "\n".join(tree)
    return f"{{\n{format}\n{indent}}}"


def to_str(value, depth, indent=0):
    if isinstance(value, dict):
        format_value = []
        nested_indent1 = " " * ((depth + 1) * DEFAULT_INDENT)
        nested_indent2 = " " * ((depth + 2) * DEFAULT_INDENT)
        for key, val in value.items():
            format_value.append(
                f"{nested_indent2}{key}: "
                f"{to_str(val, depth + 1, DEFAULT_INDENT)}"
            )
        formatted_str = "\n".join(format_value)
        return f"{{\n{formatted_str}\n{nested_indent1}}}"
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return str(value)
