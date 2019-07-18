# with Division Method
# def withDiv(in_arr):
#     out = []
#     total = 1
#     for i in in_arr:
#         total = total * i
#     for i in in_arr:
#         out.append(total/i)
#     return out
#
# print(withDiv([1,2,3,4,5]))

#O n^2
def withoutDiv(in_arr):
    out = []
    for i in range(0, len(in_arr)):
        current = in_arr[:]
        current[i] = 1
        n = 1
        for j in current:
            n = n*j
        out.append(n)
    return out

print(withoutDiv([1,2,3,4,5]))