text = "aabaabaabba$"
words = list(text)
lst = []
for i in range(len(words)):
    word = text[-1] + text[:-1]
    new = ''.join(word)
    text = new
    lst.append(new)
    i += 1

sort = sorted(lst)
print(sort)
for i in range(len(words)):
    element = sort[i]
    last = element[- 1]
    i = i + 1
    print(last)