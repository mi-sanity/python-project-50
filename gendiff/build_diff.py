def build_diff(data1, data2):
    keys = sorted(set(data1.keys()).union(data2.keys()))
    diff = {}

    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)
        if key in data1 and key not in data2:
            diff[key] = {"status": "removed", "value": value1}
        elif key not in data1 and key in data2:
            diff[key] = {"status": "added", "value": value2}
        elif data1[key] == data2[key]:
            diff[key] = {"status": "unchanged", "value": value1}
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff[key] = {
                "status": "nested", "value": build_diff(value1, value2)
            }
        else:
            diff[key] = {"status": "changed", "value": (value1, value2)}
    return diff
