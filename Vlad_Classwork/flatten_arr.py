def flatten_arr(arr: list) -> list:
    result = []
    for item in arr:
        if isinstance(item, list):
            result.extend(flatten_arr(item))
            continue
        result.append(item)

    return result


arr = [
    [1, 2],
    2,
    4,
    5,
    [
        2,
        3,
        [
            1,
            2,
            3
        ]
    ], [[[1, 2, 3]], 1, 2]]

print(flatten_arr(arr))
