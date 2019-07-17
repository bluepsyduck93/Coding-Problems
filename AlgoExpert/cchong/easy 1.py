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

print(twoNumberSum([3,5,-4,8,11,1,-1,6],10))