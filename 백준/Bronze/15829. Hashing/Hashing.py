L = int(input())
arr = input()
result = 0

for i in range(L):
    result += (ord(arr[i])-96) * (31**i)

print(result)