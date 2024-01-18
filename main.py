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

def str_to_molip_class(target_str):  #읽은 줄 가져와서 몰입 클래스로 바꿔줌
    temp_list = target_str.split("|")
    date = dt.datetime.strptime(temp_list[1], target_str.time_format)
    temp = Molip_row(date, int(temp_list[2]), int(temp_list[3]), temp_list[4])
    return temp

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
        to_find_data = input("찾으실 날짜를 입력하세요")
        temp = search_data(to_find_data)
        if temp == None:
            print("찾으시는 날짜는 아직 입력되지 않은 데이터입니다.")
        else:
            print("수정하실 데이터를 선택해 주세요 \n 1. 운동\n2. 선잠\n3. 내용\n4. 취소")
            n1 = int(input())
            if n1 == 4:
                print("수정을 취소하셨습니다. \n 처음으로 돌아갑니다.")
            elif n1 == 1:
                pass
    elif select_menu == 3:
        pass
    else :
        print("프로그램을 종료합니다.")
        break
