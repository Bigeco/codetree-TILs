arr = list(map(int, input().split()))

# print(max(arr))
max_val = arr[0]
for val in arr[1:]:
    if val > max_val:
        max_val = val

print(max_val)