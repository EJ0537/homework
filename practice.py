# 리스트 끝에 요소 1을 더해라
def add1(listlist):
    listlist.append(1)
# 리스트 끝에 요소 1을 더한 새 리스트를 돌려줘라
def add2(listlist):
    return listlist+[1]
a=[0, 1, 2]
add1(a)
print(a)          #결과: [0, 1, 2, 1]
b=add1(a)
print(a, b)       #결과: [0, 1, 2, 1, 1] None : add1은 return값이 없으므로 b에 아무것도 저장되지 않는다.
c=add2(a)
print(a, c)          #결과: [0, 1, 2, 1, 1] [0, 1, 2, 1, 1, 1]