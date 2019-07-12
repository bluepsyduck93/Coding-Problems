def generate_string(in_string):
    out = ""
    n = ""
    for i in in_string:
        if i.isdigit():
            n = n + i
        else:
            for x in range(int(n)):
                out = out + i
            n = ""
    return out


print(generate_string("10A10B10C"))

