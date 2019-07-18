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
    hash = {}
    for i in in_arr:
        complement = k - i
        if complement in in_arr:
            out = 1
        else:
            hash[i]= True
    return out


print(twosum([1,99,49,2],100))

# Hash Table - Key Value can be any data type, java is the only language that makes sure that they must be type safe

