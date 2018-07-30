def VPS():
    st_list = input()
    check = 0

    if not st_list: # "입력없을때"
        return False
    else:
        if st_list[0] is ')' or st_list[-1] is '(':# "처음과 마지막 확인"
            return False

        for x in st_list: #"괄호 갯수 확인"
            if x is '(': check = check + 1
            else:
                if check < 0 : return False 
                check = check -1


        return not check

num = int(input())
result = list()

for i in range(num):
    result.append(VPS())

for i in range(num):
    if result[i]: print('YES')
    else: print('NO')
