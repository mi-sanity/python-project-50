DEFAULT_INDENT = 4


def stylish(diff, depth=0):
    tree = []
    indent = " " * (depth * DEFAULT_INDENT)

    for key in diff:
        item = diff[key]
        stylish_formatted = stylish_format(key, item, indent, depth)
        tree.append(stylish_formatted)
    tree = "\n".join(tree)
    return f"{{\n{tree}\n{indent}}}"


def stylish_format(key, item, indent, depth):
    status = item["status"]
    val = item["value"]
    value = to_str(val, depth)
    prefix = "    "
    prefix_plus = "  + "
    prefix_minus = "  - "

    if status == "unchanged":
        return f"{indent}{prefix}{key}: {value}"
    elif status == "added":
        return f"{indent}{prefix_plus}{key}: {value}"
    elif status == "removed":
        return f"{indent}{prefix_minus}{key}: {value}"
    elif status == "changed":
        old, new = val
        old_value = to_str(old, depth)
        new_value = to_str(new, depth)
        return (
            f"{indent}{prefix_minus}{key}: {old_value}"
            f"\n{indent}{prefix_plus}{key}: {new_value}"
        )
    elif status == "nested":
        return f"{indent}{prefix}{key}: {stylish(val, depth + 1)}"


def to_str(value, depth, indent=0):
    if isinstance(value, dict):
        lines = []
        nested_indent1 = " " * ((depth + 1) * DEFAULT_INDENT)
        nested_indent2 = " " * ((depth + 2) * DEFAULT_INDENT)
        for key, val in value.items():
            lines.append(
                f"{nested_indent2}{key}: "
                f"{to_str(val, depth + 1, DEFAULT_INDENT)}"
            )
        lines = "\n".join(lines)
        return f"{{\n{lines}\n{nested_indent1}}}"
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return str(value)
