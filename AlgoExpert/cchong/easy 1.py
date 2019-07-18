#One Pass Method
#This is similar to Q3 in DCP
def twoNumberSum(in_arr, k):
    out = []
    hash = []
    for i in in_arr:
        complement = k - i
        if complement in in_arr:
            out.append(i)
            out.append(complement)
        else:
            hash[i] = True
    return sorted(out)

# Sorted uses TimSort
# https://en.wikipedia.org/wiki/Timsort
print(twoNumberSum([3,5,-4,8,11,1,-1,6],10))

# def twoNumberSum(in_arr, k):
#     out = []
#     hash = []
#     for i in in_arr:
#         complement = k - i
#         if complement in in_arr:
#             if(complement >i):
#                 out.append(i)
#                 out.append(complement)
#             else:
#                 out.append(complement)
#                 out.append(i)
#         else:
#             hash[i] = True
#     return out