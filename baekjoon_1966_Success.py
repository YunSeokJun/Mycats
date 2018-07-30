def algorithm():
    nm_list = [int(x) for x in input().split()]
    num_list = [[int(x),0] for x in input().split()]

    num_list[nm_list[1]][1] = 1 #확인하고 싶은곳 =1 나머지 =0
    temp = num_list[nm_list[1]][0] #해당 위치 값

    num_list = [x for x in num_list if x[0]>=temp] #원하는 값보다 작으면 list에서 제외
    temp_list = list() #출력용 list

    for x in range(nm_list[0]):
        check = num_list.index(max(num_list)) #list의 가장 큰 값의 위치 찾기
        if num_list[check][1]: #큰값의 위치가 1인지 확인
            result = len(num_list[:check]) + len(temp_list) + 1 #출력용 list 크기와 1을 가지고 있는 값
            break                                               #list의 크기를 더한후 return
        front_list = num_list[:check]
        rear_list  = num_list[check:]           #max값 기준으로 front, rear list 나누어 합침
        num_list = rear_list + front_list
        temp_list.append(num_list[0])           #0번째 값을 temp_list에 추가 & num_list에서 제외
        num_list.pop(0)

    return result


num = int(input())
result_list = list()
for x in range(num):
    result_list.append(algorithm())
for x in result_list:
    print(x)
