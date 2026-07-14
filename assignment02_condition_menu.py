# ## 요구사항

# ```text
# 1. 메뉴를 출력합니다.
# 2. 메뉴 번호를 입력받습니다.
# 3. 1번: 점수 등급 계산
# 4. 2번: 숫자 양수/0/음수 판별
# 5. 3번: 사용자 역할 안내
# 6. 그 외: 알 수 없는 메뉴 안내
# ```

# ## 세부 조건

# 점수 등급 계산:

# ```text
# 90 이상: A
# 80 이상: B
# 70 이상: C
# 그 외: D
# ```

# 사용자 역할 안내:

# ```text
# admin: 관리자입니다.
# member: 일반 사용자입니다.
# guest: 게스트입니다.
# 그 외: 알 수 없는 역할입니다.
# ```

# ## 권장 문법

# ```text
# if
# elif
# else
# match-case
# ```

# ## 확인 기준

# ```text
# 여러 조건이 올바른 순서로 검사되는가?
# 잘못된 메뉴 입력도 처리하는가?
# match-case 또는 if/elif/else 중 적절한 방식을 선택했는가?
# ```

print("메뉴를 선택해주세요.\n1. 점수 등급 계산\n2. 숫자 양수/0//음수 판별\n3. 사용자 역할 안내\n")

num = input("\n번호를 입력해주세요.")

if num == "1" :
    print("점수 등급 판별기\n")
    score = int(input("점수를 입력해주세요."))
    if score >= 90 :
        print("A등급")
    elif score >= 80 :
        print("B등급")
    elif score >= 70 :
        print("C등급")
    else :
        print("D등급")

elif num == "2" :
    print("양수, 음수, 0 판별기\n")
    num1 = int(input("양수, 음수, 0 중에 한 숫자를 적어주세요."))
    if num1 < 0 :
        print("음수입니다.")
    elif num1 > 0 :
        print("양수입니다.")
    elif num1 == 0 :
        print("0입니다.")

elif num == "3" :
    print("역할 안내서\n1.아이브 멋져요\n2.member\n3.guest")
    letter = input("번호를 입력해주세요.")
    if letter == "1" :
        print("방탄소년단 짱이에요!")    
    elif letter == "2" :
        print("member: 일반 사용자입니다.")
    elif letter == "3" :
        print("guest: 게스트입니다.")
    else :
        print("그 외: 알 수 없는 역할입니다.")

else :
    print("알 수 없는 메뉴입니다.")

    

            