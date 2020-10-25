def calculate_frequency(list_):
    frequencies = {}
    for i in list_:
        if i in frequencies:
            frequencies[i] += 1
        else:
            frequencies[i] = 1
    return frequencies


print(calculate_frequency(["hi", "I", "am", "Alexa", "I", "would", "just", "like", "to", "say", "hi"]))