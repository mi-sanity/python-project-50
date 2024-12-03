def plain(diff):
    lines = plain_format(diff)
    result = '\n'.join(lines)
    return result


def plain_format(diff, path=""):
    lines = []

    def add_lines(status, value, full_path):
        actions = {
            "nested": lambda value, full_path: lines.extend(
                plain_format(value, full_path)
            ),
            "added": lambda value, full_path: lines.append(
                format_added_data(value, full_path)
            ),
            "removed": lambda value, full_path: lines.append(
                f"Property '{full_path}' was removed"
            ),
            "changed": lambda value, full_path: lines.append(
                format_changed_data(value, full_path)
            ),
            "unchanged": lambda value, full_path: None
        }
        action = actions.get(status)
        if action:
            action(value, full_path)

    for key, (status, value) in diff.items():
        full_path = create_full_path(path, key)
        add_lines(status, value, full_path)
    return lines


def create_full_path(path, key):
    if path == "":
        full_path = f"{key}"
    else:
        full_path = f"{path}.{key}"
    return full_path


def create_format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, str):
        return f"'{value}'"
    if value is None:
        return "null"
    return str(value).lower()


def format_added_data(value, full_path):
    value = create_format_value(value)
    if isinstance(value, dict):
        value_description = "[complex value]"
    elif isinstance(value, str):
        value_description = f"{value}"
    else:
        value_description = str(value).lower()
    text = (
        f"Property '{full_path}' was added "
        f"with value: {value_description}"
    )
    return text


def format_changed_data(value, full_path):
    old, new = value
    old, new = create_format_value(old), create_format_value(new)
    if isinstance(old, dict):
        old_value = "[complex value]"
    elif isinstance(old, str):
        old_value = f"{old}"
    else:
        old_value = str(old).lower()
    if isinstance(new, dict):
        new_value = "[complex value]"
    elif isinstance(new, str):
        new_value = f"{new}"
    else:
        new_value = str(new).lower()
    text = (
        f"Property '{full_path}' was updated. "
        f"From {old_value} to {new_value}"
    )
    return text
