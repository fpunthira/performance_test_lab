arr = []

b = raw_input()

arr.append(b[0])

for i in b:
    for j in arr:
        if i == j:
            break
        if j == arr[len(arr)-1]:
            arr.append(i)

if len(arr) % 2 == 0:
    print "CHAT WITH HER!"
else: 
    print "IGNORE HIM!"
