a = input(' ')
i = []
i = a.split(' ')
result = 0


if i[2] =='+':
    result = int(i[0]) + int(i[1])
if a[2] == '/':
    result = int(i[0]) / int(i[1])
if a[2] == '*':
    result = int(i[0]) * int(i[1])
elif a[2] == '-':
    result = int(i[0]) - int(i[1])


print('',result)