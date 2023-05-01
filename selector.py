# lucky-num-selector

import random # random 함수 불러오기

num = int(input("몇번 반복할까요? :")) # 반복할 횟수

for i in range(num): # num번 반복하기
    
    for i in range(6): # 1부터 45까지 숫자에서 6개 숫자 뽑기
        print(random.randint(1,46))
    print("===")
