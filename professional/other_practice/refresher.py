input_list = [
    {"a":1, "b":2, "c":3},
    {"b":5, "d":7, "g":3, "m":3},
    {},
    {"x":9, "d":9, "b":1, "p":4}
]

output_list = {
    "a": [1, 0, 0, 0],
    "b": [2, 5, 0, 1],
    "c": [3, 0, 0, 0],
    "d": [0, 7, 0, 9],
    "g": [0, 3, 0, 0],
    "m": [0, 3, 0, 0],
    "x": [0, 0, 0, 9],
    "p": [0, 0, 0, 4]
}

def lod_to_dol(input):
    new_map = {}
    index = 0
    
    for dict in input:
        print(dict)
        for key in dict:
            print(key)
            print(index)
            if key not in new_map:
                new_map[key] = [0] * (index)
            new_map[key].append(dict[key])
        index += 1
        for key in new_map:
            if key not in dict:
                new_map[key].append(0)

    print(new_map)
    return new_map

lod_to_dol(input_list)
print(output_list == lod_to_dol(input_list))