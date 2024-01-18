import datetime as dt

class Molip_row:
    time_format = "%Y-%m-%d"
    def __init__(self, date, count_exercise, count_sleep, text) -> None:
        self.date = date
        self.count_exercise = count_exercise
        self.count_sleep = count_sleep
        self.text = text
        self.count_day = 0
        self.str_date = dt.datetime.strftime(self.date, self.time_format) 

    def __str__(self) -> str:
        result_date = dt.datetime.strftime(self.date, "%m월 %d일")
        result1 =  f"{result_date}(공부자체 몰입 {self.count_day}일, "
        if self.count_exercise == 0:
            result2 = "운동 X, "
        else:
            result2 = f"운동 {self.count_exercise}분, "
        
        if self.count_sleep == 0:
            result3 = "선잠 X)"
        else:
            result3 = f"선잠 {self.count_sleep}회)"

        return result1 + result2 + result3 + f"\n{self.text}"


if __name__ == "__main__":
    print("정상작동")
    test = Molip_row(dt.datetime.now(), 0, 3, "Hello World!")
    print(test)