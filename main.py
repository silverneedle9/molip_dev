from molip_class import *

def first_menu(): # 초기 메뉴 설정하는 함수 / 입력 받아서 선택한 메뉴 int return 
    try:
        while True:
            print("#" * 30)
            print("1. 새로 입력")
            print("2. 기존 데이터 수정")
            print("3. 출력")
            print("4. 종료")
            print("#" * 30)
            select_menu = int(input("원하시는 메뉴를 선택해주세요"))
            if select_menu <=4 and select_menu >=1:
                return select_menu
            print("잘못 입력하셨습니다. 다시 입력해주세요")
    except:
        print("메뉴는 정수형 숫자만 입력해주세요.")


