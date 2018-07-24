def VPS():
    st_list = input()
    check = list()

    for x in st_list:
        if x is '(': check.append('0') #"'('이면 추가"
        else:
            if not check: return False # "list가 비어있을때 return"
            else: check.pop() # "')'이면 pop"

    if not check: return True
    else : return False

num = int(input())
result = list()

for i in range(num):
    result.append(VPS())

for i in range(num):
    if result[i]: print('YES')
    else: print('NO')
