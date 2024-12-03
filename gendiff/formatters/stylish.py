DEFAULT_INDENT = 4
LEFT_INDENT = 2
CHANGE_DEPTH = 1


def stylish(diff):
    result = '{\n' + tree_view(diff) + '\n}'
    return result


def tree_view(diff, depth=1):
    lines = []
    for key, (type, value) in sorted(diff.items()):
        lines = create_lines(lines, key, value, depth, type)
    result = '\n'.join(lines)
    return result


def create_lines(lines, key, value, depth, type):
    prefix = '  '
    if type == 'nested':
        indent = (DEFAULT_INDENT * depth - LEFT_INDENT) * ' '
        child_diff = tree_view(value, depth + CHANGE_DEPTH)
        format_value = f'{{\n{child_diff}\n{indent}  }}'
        lines = add_format_and_indent(depth, lines, prefix, key, format_value)
    elif type == 'changed':
        lines = changed_data_diff(lines, value, depth, key)
    elif type == 'added':
        prefix = '+ '
        lines = add_format_and_indent(depth, lines, prefix, key, value)
    elif type == 'removed':
        prefix = '- '
        lines = add_format_and_indent(depth, lines, prefix, key, value)
    else:
        lines = add_format_and_indent(depth, lines, prefix, key, value)
    return lines


def add_format_and_indent(depth, lines, prefix, key, value):
    format_value = create_format_value(value, depth + CHANGE_DEPTH)
    indent = (DEFAULT_INDENT * depth - LEFT_INDENT) * ' '
    lines.append(f"{indent}{prefix}{key}: {format_value}")
    return lines


def create_format_value(value, depth):
    if isinstance(value, dict):
        prefix = '  '
        lines = ['{']
        for key, val in value.items():
            format_value = create_format_value(val, depth + CHANGE_DEPTH)
            lines = add_format_and_indent(depth, lines,
                                          prefix, key, format_value)
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


def changed_data_diff(lines, value, depth, key):
    old, new = value
    old_new_pairs = [('- ', old), ('+ ', new)]
    for prefix, value in old_new_pairs:
        format_value = create_format_value(value, depth + CHANGE_DEPTH)
        lines = add_format_and_indent(depth, lines, prefix, key, format_value)
    return lines
