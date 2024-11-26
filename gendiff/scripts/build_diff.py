def build_diff(data1, data2):
    keys = sorted(set(data1.keys() | data2.keys()))
    diff = []

    for key in keys:
        if not data2.get(key):
            diff.append(f"  - {key}: {data1.get(key)}")
        elif data1.get(key) == data2.get(key):
            diff.append(f"    {key}: {data1.get(key)}")
        elif not data1.get(key):
            diff.append(f"  + {key}: {data2.get(key)}")
        else:
            diff.append(f"  - {key}: {data1.get(key)}\n  + {key}: {data2.get(key)}")
    return '\n'.join(diff)
