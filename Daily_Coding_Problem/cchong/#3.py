def twosum(in_arr, k):
    out = 0
    for i in range(len(in_arr)-1):
        for j in range(len(in_arr)-1):
            if(in_arr[i]+in_arr[len(in_arr)-(j+1)] == k):
                out = 1

    print(out)

twosum([9,10,15,7,3],24)

