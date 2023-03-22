n = list(map(int,input().split()))

if n == [1,2,3,4,5,6,7,8]:
    print("ascending")
elif n[::-1] == [1,2,3,4,5,6,7,8]:
    print("descending")
else:
    print("mixed")
