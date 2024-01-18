from molip_class import *
import datetime as dt
import os


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

def search_data(target_date):
    final_data = None
    if target_date == "":
        return None
    with open("media/molip_db.txt", 'r', encoding='utf8') as f:
        while True:
            current_data = f.readline()
            current_data.strip()
            if current_data == "":
                break
            temp = current_data.split("|")
            if temp[1] == target_date:
                final_data = current_data
    return final_data

def save_data(target_molip_data, status):
    with open('media/molip_db.txt', 'a', encoding='utf8') as f:
        data_str = f"{target_molip_data.str_date}|{target_molip_data.count_exercise}|{target_molip_data.count_sleep}|{target_molip_data.text}"
        f.write(status + "|" + data_str + "\n")
    print("저장이 완료되었습니다.")

if not os.path.isfile("media/molip_db.txt"):
    with open('media/molip_db.txt', 'w', encoding='utf8') as f:
        f.write("status|date|exercise|sleep|text\n")
        print("파일을 생성하였습니다.") 
while True:
    select_menu = first_menu()
    if select_menu == 1:
        new_date = input("생성할 날짜를 알려주세요. (미입력시 오늘)")
        if search_data(new_date) == None:
            print("데이터를 새로 작성합니다.")
            if new_date == "":
                new_date = dt.datetime.now()
            else:
                new_date = dt.datetime.strptime(new_date, Molip_row.time_format)
            exercise = int(input("운동 :"))
            sleep = int(input("선잠 :"))
            text = input("기록 입력")
            save_data(Molip_row(new_date, exercise, sleep, text), 'new')
        else:
            print("이미 존재하는 데이터입니다.\n 수정메뉴를 이용해주세요.")
    elif select_menu == 2:
        pass
    elif select_menu == 3:
        pass
    else :
        print("프로그램을 종료합니다.")
        break
