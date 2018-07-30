def algorithm():
    nm_list = [int(x) for x in input().split()]
    num_list = [int(x) for x in input().split()]
    check = max(num_list) # list max값

    imp = num_list[nm_list[1]] #찾는 수
    check = num_list.index(check) #list max값 위치
    result = 1
    num = 0

    front_list = [x for x in num_list[:nm_list[1]] if x >= imp] # 찾는 수 기준으로 앞 list
    result = result + len(front_list)

    if check < nm_list[1]: # max 위치가 찾는수보다 앞에 있는경우
        rear_list = [x for x in num_list[nm_list[1]:] if x >= imp] # 남은 뒤 list
        rear_list.reverse()
        for x in rear_list:
            if x > imp: break
            result = result + 1
            num = num + 1
        for x in rear_list[num:]:
            if x > imp: result = result + 1

    elif check > nm_list[1]: # max 위치가 찾는수보다 뒤에 있는 경우
        middle_list = [x for x in num_list[nm_list[1]:check] if x>imp] # 찾는 위치와 max위치 사이 list
        result = len(middle_list) + result
        rear_list = [x for x in num_list[check:] if x>= imp]
        rear_list.reverse()
        for x in rear_list:
            if x > imp: break
            result = result + 1
            num = num + 1
        for x in rear_list[num:]:
            if x > imp: result = result + 1

    return result

num = int(input())
result_list = list()
for x in range(num):
    result_list.append(algorithm())
for x in result_list:
    print(x)
