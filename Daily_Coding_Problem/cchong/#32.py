#O 2^n
# def editDist(str1, str2, m, n):
#     if m == 0 or n == 0:
#         return 0;
#     elif str1[m-1] == str2[n-1]:
#         return 1 + editDist(str1,str2,m-1,n-1);
#     else:
#         return max(editDist(str1, str2, m, n-1), editDist(str1, str2, m-1, n));
#
#
# str1 = "applepen"
# str2 = "pen"
# print(editDist(str1, str2, len(str1), len(str2)))

#O(m*n)

def editDist(str1, str2, m, n):
    L = [[0 for i in range(n+1)]
            for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                L[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    print(L)
    maxlen = len(str1) if len(str1) > len(str2) else len(str2)
    return maxlen - L[m][n]


str1 = "pen"
str2 = "apen"
print(editDist(str1, str2, len(str1), len(str2)))