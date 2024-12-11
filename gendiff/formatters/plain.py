def plain(diff):
    result = "\n".join(plain_format(diff))
    return result


def plain_format(diff, path=""):
    lines = []

    for key in diff:
        item = diff[key]
        status = item["status"]
        value = to_str(item["value"])
        full_path = f"{path}.{key}" if path else key

        if status == "added":
            lines.append(
                f"Property '{full_path}' was added with value: {value}"
            )
        elif status == "removed":
            lines.append(f"Property '{full_path}' was removed")
        elif status == "changed":
            old, new = item["value"]
            old_value = to_str(old)
            new_value = to_str(new)
            lines.append(
                f"Property '{full_path}' was updated. "
                f"From {old_value} to {new_value}"
            )
        elif status == "nested":
            lines.extend(plain_format(item["value"], full_path))
    return lines


def to_str(value):
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, str):
        return f"'{value}'"
    if value is None:
        return "null"
    return str(value).lower()
