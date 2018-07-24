st_list = input().split('()')

if not st_list[0]:
    st_list.remove('')
check = 0
result = 0

for x in st_list:
    for y in x:
        if y is '(': check = check + 1
        else:
            check = check - 1
            result = result + 1
    result = result + check
print(result)
