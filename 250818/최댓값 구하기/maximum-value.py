arr = list(map(int, input().split()))

# print(max(arr))
max_val = 0
for val in arr:
    if val > max_val:
        max_val = val

print(max_val)