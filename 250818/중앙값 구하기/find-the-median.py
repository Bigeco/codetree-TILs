# sort()


A, B, C = list(map(int, input().split()))

min_val = A
max_val = A
for val in [B, C]:
    if min_val > val:
        min_val = val
    if max_val < val:
        max_val = val


for val in [A, B, C]:
    if val not in [min_val, max_val]:
        median_val = val

print(median_val)
