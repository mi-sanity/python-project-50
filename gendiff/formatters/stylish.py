DEFAULT_INDENT = 4
LEFT_INDENT = 2
CHANGE_DEPTH = 1


def stylish(diff):
    result = '{\n' + tree_view(diff) + '\n}'
    return result


def tree_view(diff, depth=1):
    lines = []
    for key, (status, value) in sorted(diff.items()):
        lines = create_lines(lines, key, value, depth, status)
    result = '\n'.join(lines)
    return result


def create_lines(lines, key, value, depth, status):
    prefix = '  '
    if status == 'nested':
        indent = (DEFAULT_INDENT * depth - LEFT_INDENT) * ' '
        child_diff = tree_view(value, depth + CHANGE_DEPTH)
        format_value = f'{{\n{child_diff}\n{indent}  }}'
        lines = add_format(depth, lines, prefix, key, format_value, status)
    elif status == 'changed':
        lines = add_format(depth, lines, prefix, key, value, status)
    elif status == 'added':
        prefix = '+ '
        lines = add_format(depth, lines, prefix, key, value, status)
    elif status == 'removed':
        prefix = '- '
        lines = add_format(depth, lines, prefix, key, value, status)
    else:
        lines = add_format(depth, lines, prefix, key, value, status)
    return lines


def create_format_value(value, depth):
    if isinstance(value, dict):
        prefix = '  '
        lines = ['{']
        for key, val in value.items():
            format_value = create_format_value(val, depth + CHANGE_DEPTH)
            lines = add_format(depth, lines, prefix, key, format_value)
        indent = ' ' * (DEFAULT_INDENT * (depth - CHANGE_DEPTH))
        lines.append(f"{indent}}}")
        return '\n'.join(lines)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return value
    return str(value)


def add_format(depth, lines, prefix, key, value, status=None):
    indent = (DEFAULT_INDENT * depth - LEFT_INDENT) * ' '
    if status != 'changed':
        format_value = create_format_value(value, depth + CHANGE_DEPTH)
        lines.append(f"{indent}{prefix}{key}: {format_value}")
        return lines
    else:
        old, new = value
        old_format_value = create_format_value(old, depth + CHANGE_DEPTH)
        new_format_value = create_format_value(new, depth + CHANGE_DEPTH)
        old_prefix = '- '
        new_prefix = '+ '
        lines.append(
            f"{indent}{old_prefix}{key}: {old_format_value}"
            f"\n{indent}{new_prefix}{key}: {new_format_value}"
        )
        return lines
