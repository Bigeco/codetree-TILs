count = 0

for _ in range(3):
    symptom, temp = input().split()
    temp = int(temp)
    if symptom == "Y" and temp >= 37:
        count += 1

if count >= 2:
    print("E")
else:
    print("N")
