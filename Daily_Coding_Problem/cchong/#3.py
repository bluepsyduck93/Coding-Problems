# Brute Force Method
# def twosum(in_arr, k):
#     out = 0
#     for i in range(len(in_arr)-1):
#         for j in range(len(in_arr)-1):
#             if(in_arr[i]+in_arr[len(in_arr)-(j+1)] == k):
#                 out = 1
#                 break
#             break
#
#     print(out)
#
# twosum([1,3,4,2],6)

#One Pass Method
def twosum(in_arr, k):
    out = 0
    hash = []
    for i in in_arr:
        complement = k - i
        try :
            hash.index(complement)
            out = 1
        except (ValueError) as e:
            pass
        hash.append(i)
    return out


print(twosum([1,99,49,2],100))

