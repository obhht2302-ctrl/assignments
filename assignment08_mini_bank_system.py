# 실생활에서 쓰이는 은행의 시스템을 베이스로 만든 미니 뱅크 시스템
# 함수로 메뉴의 기능들을 구현했고, while True문으로 각각 메뉴들이 진행됩니다.
# 프로그램을 종료해서 다시 재생시켜도 이전 기록이 다시 떠오르도록 DB 연동을 아직은 구현 못한, 아주 기본적인 틀만 잡아둔 상태입니다.
# 에러가 발생하거나 잘못된 값을 입력한 경우, 제대로 된 입력값을 다시 입력하는 것에 포커싱. 예를 들어 출금 메뉴에서 저축액보다 큰 금액을 입력하면 다시 초기 화면으로 이동합니다.
#

accounts = {}
account_counter = 1


def create_account():
    """계좌 개설 함수"""
    global account_counter
    print("-" * 40)
    print("계좌 개설입니다.")
    customer_name = input("성함: ")

    while True:
        first_deposit = int(input("초기 입금액: "))
        if first_deposit < 1000:
            print("1000원 이상 입금해주세요.")
        else:
            break

    account_num = f"ACC{account_counter}"

    accounts[account_num] = {"customer_name": customer_name, "balance": first_deposit}

    account_counter += 1

    print("-" * 40)
    print("계좌가 성공적으로 개설되었습니다.")
    print(f"성함:  {customer_name}")
    print(f"계좌명: {account_num}")
    print(f"잔액: {first_deposit:,}")
    print("-" * 40)


def check_balance():
    """잔액 조회 함수"""
    print("-" * 40)
    print("잔액 조회를 합니다.")
    account_number = input("계좌번호를 적어주세요: ")

    if account_number in accounts:
        account = accounts[account_number]

        print("-" * 40)
        print(f"{account['customer_name']}님 어서오세요!")
        print(f"고객명: {account['customer_name']}")
        print(f"현재 잔액: {account['balance']:,}원")
        print("-" * 40)
    else:
        print("-" * 40)
        print("존재하지 않는 계좌번호입니다.")
        print("-" * 40)


def balance_deposit():
    """입금 함수"""
    print("-" * 40)
    print("입금하기 ")
    account_number = input("계좌 번호를 입력해주세요: ")
    balance = int(input("입금 금액: "))
    if account_number in accounts:
        account = accounts[account_number]
        account["balance"] += balance
        print(
            f"\n입금이 완료되었습니다.\n현재 잔고는 {account['balance']:,}원입니다.\n"
        )
    else:
        print("해당 계좌명이 없습니다.")


def withrawl_money():
    """출금 함수"""
    print("-" * 40)
    print("출금하기 ")
    account_number = input("계좌명을 입력해주세요: ")
    while account_number not in accounts:
        account_number = input("해당 계좌명이 없습니다. 계좌명을 다시 입력해주십시오: ")
        if account_number in accounts:
            break
    balance = int(input("출금 금액: "))
    print()

    account = accounts[account_number]

    if account["balance"] == 0:
        print("잔고가 현재 0원이므로 출금이 불가합니다.")
    elif account["balance"] < balance:
        print("잔고의 금액보다 출금하려는 금액이 큽니다.")
    elif account_number in accounts:
        account["balance"] -= balance
        print(
            f"\n출금이 완료되었습니다.\n현재 잔고는 {account['balance']:,}원입니다.\n"
        )


def all_member():
    """전체 이용자 기록 확인 함수"""
    print("-" * 40)
    print("전체 이용자 기록 확인\n")
    for account_number in accounts:
        account = accounts[account_number]
        print(f"계좌명: {account_number}")
        print(f"성함: {account['customer_name']}")
        print(f"잔고: {account['balance']:,}")
        print()
    print("-" * 40)


while True:
    """메뉴 시작"""
    print("미니뱅크 시스템입니다.\n")
    print(
        "1. 계좌 개설\n2. 잔액 조회\n3. 입금하기\n4. 출금하기\n5. 전체 이용자 확인\n6. 종료하기"
    )
    user_choice = int(input("메뉴를 선택해주세요: "))

    if user_choice == 1:
        create_account()

    elif user_choice == 2:
        check_balance()

    elif user_choice == 3:
        balance_deposit()

    elif user_choice == 4:
        withrawl_money()

    elif user_choice == 5:
        all_member()

    elif user_choice == 6:
        break

    else:
        print("1-5번 중 하나를 선택해주세요.")

print("프로그램을 종료합니다.")