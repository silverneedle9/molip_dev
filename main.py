from molip_class import *
import datetime as dt
import os


def first_menu(): # 초기 메뉴 설정하는 함수 / 입력 받아서 선택한 메뉴 int return 
    try:
        while True:
            print("#" * 30)
            print("1. 새로 입력")
            print("2. 데이터 확인")
            print("3. 기존 데이터 수정")
            print("4. 출력")
            print("5. 데이터 삭제")
            print("6. 전체 데이터 출력")
            print("7. 종료")
            print("#" * 30)
            select_menu = int(input("원하시는 메뉴를 선택해주세요"))
            if select_menu <=7 and select_menu >=1:
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
            if current_data == "":
                break
            current_data.strip()
            temp = current_data.split("|")
            if temp[1] == target_date:
                final_data = current_data
    return final_data

def check_date():
    result = []
    with open("media/molip_db.txt", 'r', encoding='utf8') as f:
        for i in f.readlines():
            temp = i.split("|")
            if temp[1] == "date":
                pass
            elif temp[1] not in result:
                result.append(temp[1])
    result.sort()
    return result

def save_data(target_molip_data, status):
    with open('media/molip_db.txt', 'a', encoding='utf8') as f:
        data_str = f"{target_molip_data.str_date}|{target_molip_data.count_exercise}|{target_molip_data.count_sleep}|{target_molip_data.text}"
        f.write(status + "|" + data_str + "\n")
    print("저장이 완료되었습니다.")

def str_to_molip_class(target_str):  #읽은 줄 가져와서 몰입 클래스로 바꿔줌
    if target_str == None:
        return None
    temp_list = target_str.split("|")
    date = dt.datetime.strptime(temp_list[1], Molip_row.time_format)
    temp = Molip_row(date, int(temp_list[2]), int(temp_list[3]), temp_list[4][:-1])
    return temp

if not os.path.isfile("media/molip_db.txt"):
    with open('media/molip_db.txt', 'w', encoding='utf8') as f:
        f.write("status|date|exercise|sleep|text\n")
        print("파일을 생성하였습니다.") 

while True:
    select_menu = first_menu()
    if select_menu == 1:
        new_date = input("생성할 날짜를 알려주세요. (미입력시 오늘)")
        if new_date == "":
            new_date = dt.datetime.strftime(dt.datetime.now(),Molip_row.time_format)
        if search_data(new_date) == None:
            print("데이터를 새로 작성합니다.")
            if new_date == "":
                pass
            else:
                new_date = dt.datetime.strptime(new_date, Molip_row.time_format)
            exercise = int(input("운동 :"))
            sleep = int(input("선잠 :"))
            text = input("기록 입력 :")
            save_data(Molip_row(new_date, exercise, sleep, text), 'new')
        else:
            print("이미 존재하는 데이터입니다.\n수정메뉴를 이용해주세요.")
    elif select_menu == 2:
        to_find_data = input("찾으실 날짜를 입력하세요")
        if to_find_data == "":
            to_find_data = dt.datetime.strftime(dt.datetime.now(),Molip_row.time_format)
        temp = search_data(to_find_data)
        if temp == None:
            print("찾으시는 날짜는 아직 입력되지 않은 데이터입니다.")
        else:
            temp = str_to_molip_class(temp)
            print(temp)
            input()
    elif select_menu == 3:
        to_find_data = input("찾으실 날짜를 입력하세요")
        if to_find_data == "":
            to_find_data = dt.datetime.strftime(dt.datetime.now(),Molip_row.time_format)
        temp = search_data(to_find_data)
        if temp == None:
            print("찾으시는 날짜는 아직 입력되지 않은 데이터입니다.")
        else:
            temp = str_to_molip_class(temp)
            print("수정하실 데이터를 선택해 주세요 \n1. 운동\n2. 선잠\n3. 내용\n4. 취소")
            n1 = int(input())
            if n1 == 4:
                print("수정을 취소하셨습니다. \n 처음으로 돌아갑니다.")
            else:
                if n1 == 1:
                    print("수정할 데이터를 입력해주세요")
                    edit_num = input("숫자만 입력시 그 숫자로, 기호 입력 증감")
                    if str.isdigit(edit_num):
                        temp.count_exercise = int(edit_num)
                    else:
                        if edit_num[0] == "+":
                            temp.count_exercise += int(edit_num[1:])
                        elif edit_num[0] == "-":
                            temp.count_exercise -= int(edit_num[1:])
                elif n1 == 2:
                    print("수정할 데이터를 입력해주세요")
                    edit_num = input("숫자만 입력시 그 숫자로, 기호 입력 증감")
                    if str.isdigit(edit_num):
                        temp.count_sleep = int(edit_num)
                    else:
                        if edit_num[0] == "+":
                            temp.count_sleep += int(edit_num[1:])
                        elif edit_num[0] == "-":
                            temp.count_sleep -= int(edit_num[1:])
                elif n1 == 3:
                    edit_text = input("수정할 데이터를 입력해주세요\n")
                    temp.text = edit_text
                save_data(temp, "edit")
    elif select_menu == 4:
        date_for_print = input("기준일(금요일)의 날짜를 입력해주세요.(미입력시 오늘)\n입력하신 날짜를 기준으로 일주일의 데이터가 출력됩니다.\n")
        if date_for_print == "":
            date_for_print = dt.datetime.now()
        else:
            date_for_print = dt.datetime.strptime(date_for_print, Molip_row.time_format)
        title = f"[몰입클럽]{((date_for_print - dt.datetime.strptime('2023-11-17', Molip_row.time_format)).days)//7 + 30}주차(2023-04-27,수능).txt"
        path1 = "result/"
        with open(path1 + title, 'w', encoding='utf8') as f:
            f.write(title[:-4]+"\n")
        for i in range(7,-1,-1):
            temp = date_for_print - dt.timedelta(days=i)
            temp = dt.datetime.strftime(temp, Molip_row.time_format)
            with open(path1 + title, 'a', encoding='utf8') as f:
                recode = search_data(temp)
                if recode != None:
                    f.write(str(str_to_molip_class(recode)))
    elif select_menu == 5:
        del_date = input("데이터를 삭제할 날짜를 입력해주세요.\n")
        db_data = []
        with open("media/molip_db.txt", 'r', encoding='utf8') as f:
            db_data = f.readlines()
        
        with open("media/molip_db.txt", 'w', encoding='utf8') as f:
            for i in db_data:
                temp = i.split("|")
                if temp[1] != del_date:
                    f.write(i)
    elif select_menu == 6:
        print("내용을 전체 출력합니다.")
        date_list = check_date()
        with open("result/all_data.txt", 'w', encoding='utf8') as f:
            for i in date_list:
                if i != None:
                    t = str_to_molip_class(search_data(i))
                    f.write(str(t))
                    
    else :
        print("프로그램을 종료합니다.")
        break
