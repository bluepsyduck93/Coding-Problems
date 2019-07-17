#One Pass Method
#This is similar to Q3 in DCP
def twoNumberSum(in_arr, k):
    out = []
    hash = []
    for i in in_arr:
        complement = k - i
        try :
            hash.index(complement)
            out.append(in_arr[hash.index(complement)])
            out.append(i)
        except (ValueError) as e:
            pass
        hash.append(i)
    return sorted(out)

# Sorted uses TimSort
# https://en.wikipedia.org/wiki/Timsort
print(twoNumberSum([3,5,-4,8,11,1,-1,6],10))

# def twoNumberSum(in_arr, k):
#     out = []
#     hash = []
#     for i in in_arr:
#         complement = k - i
#         try :
#             hash.index(complement)
#             if complement < i:
#                 out.append(in_arr[hash.index(complement)])
#                 out.append(i)
#             else:
#                 out.append(i)
#                 out.append(in_arr[hash.index(complement)])
#         except (ValueError) as e:
#             pass
#         hash.append(i)
#     return out