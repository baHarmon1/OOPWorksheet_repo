class AlarmClock:
    def __init__(self):
        self.current_time = ""
        self.is_alarm_on = False
        self.alarm_time = "1:30"

    def change_current_time(self):
        self.current_time = input("What is the current time? ")
        print(self.current_time)

    def change_alarm_on(self):
        self.alarm_time = input("Would you like to turn on your alarm? ")
        if self.alarm_time.upper() == "YES":
            self.is_alarm_on = True
            self.alarm_time = input(
                "What time would you like your alarm to go off? ")
            print(f"Alarm is set to go off at {self.alarm_time}! ")

        else:
            self.is_alarm_on = False
            print("Ok, your alarm is off")
