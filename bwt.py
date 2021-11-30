def rotate(text):
    rotations = []
    for char in text:
        text = text[-1] + text[:-1]
        rotations.append(text)
    return rotations

def matrix(text):
    return sorted(rotate(text))

def get_transform(text):
    return ''.join([t[-1] for t in matrix(text)])

def get_f(text):
    return [t[1] for t in matrix(text)]

def main():
    print("Texte a transformer : ")
    text = input()
    print("####")
    print("Matrice : ")
    print(matrix(text))
    print("####")

    print("Transformee : ")
    print(get_transform(text))

if __name__ == "__main__":
    main()