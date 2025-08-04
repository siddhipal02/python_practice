def flatten(nested):
    flat = []
    for item in nested:
        if isinstance(item, list):
            flat += flatten(item)  
        else:
            flat.append(item)
    return flat

nested = [[1, 2], 3, [4, [5, 6]]]
print(flatten(nested))
