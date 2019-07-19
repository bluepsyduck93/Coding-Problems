# O(n) solution
def editDist(string1, string2):
    string1 = list(string1)
    string2 = list(string2)
    min = len(string1) if len(string1) < len(string2) else len(string2)
    max = len(string2) if len(string1) < len(string2) else len(string2)
    samechar = 0
    for i in range(0, min):
        if string1[i] == string2[i]:
            samechar = samechar +1

    print(max-samechar)

editDist("kitten", "sitting")