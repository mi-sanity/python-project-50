def plain(diff):
    result = '\n'.join(plain_format(diff))
    return result


def plain_format(diff, path=""):
    lines = []

    def add_lines(status, value, full_path):
        actions = {
            "nested": lambda value, full_path: lines.extend(
                plain_format(value, full_path)
            ),
            "added": lambda value, full_path: lines.append(
                create_format_data(status, value, full_path)
            ),
            "removed": lambda value, full_path: lines.append(
                f"Property '{full_path}' was removed"
            ),
            "changed": lambda value, full_path: lines.append(
                create_format_data(status, value, full_path)
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


def create_format_data(status, value, full_path):
    if status == "added":
        value = create_format_value(value)
        text = (
            f"Property '{full_path}' was added "
            f"with value: {value}"
        )
        return text
    elif status == "changed":
        old, new = value
        old_value = create_format_value(old)
        new_value = create_format_value(new)
        text = (
            f"Property '{full_path}' was updated. "
            f"From {old_value} to {new_value}"
        )
        return text
