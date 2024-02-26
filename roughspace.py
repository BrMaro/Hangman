def pseudoword(word, letter):
    string = ""
    stringlist = []
    for i in range(len(word)):
        if word[i] == letter:
            stringlist.append(letter)
        else:
            stringlist.append("_")
    for j in range(len(word)):
        string = string + stringlist[j]
    print(string)
