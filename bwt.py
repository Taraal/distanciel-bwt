def rotate(text):
    rotations = []
    for i in text:
        text = text[-1] + text[:-1]
        rotations.append(text)
    return rotations

def matrix(text):
    return sorted(rotate(text))

def transform(text):
    return [t[-1] for t in matrix(text)]