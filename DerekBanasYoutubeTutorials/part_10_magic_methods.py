class Time(object):
    """Time format class. Mind that it is heavily simplified, I am just asuming
    here that the input values must be in specific range but if I wanted to
    perform other math operations on them I would have to add another layer of logic
    """
    def __init__(self, hour= 0, minute= 0, second= 0):
        self.hour = hour
        self.minute = minute
        self.second = second

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, hour):
        if type(hour) is int:
            if hour < 0:
                print('ValueError: inappropiate hour value {}'.format(hour))
            elif hour > 24:
                print('ValueError: inappropiate hour value {}'.format(hour))
            else:
                self.__hour = hour

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, minute):
        if type(minute) is int:
            if minute < 0:
                print('ValueError: inappropiate minute value {}'.format(minute))
            elif minute > 60:
                print('ValueError: inappropiate minute value {}'.format(minute))
            else:
                self.__minute = minute
    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, second):
        if type(second) is int:
            if second < 0:
                print('ValueError: inappropiate second value {}'.format(second))
            elif second > 60:
                print('ValueError: inappropiate second value {}'.format(second))
            else:
                self.__second = second

    def __add__(self, second_time):
        result_time = Time()

        #add seconds and correct if >60
        seconds_correction = (second_time.second + self.second)//60
        result_time.second = (second_time.second + self.second)%60

        #add minutes and correct if >60
        minutes_correction = (second_time.minute + self.minute +
                                         seconds_correction)//60
        result_time.minute = (second_time.minute + self.minute +
                                          seconds_correction)%60
        #add hours and correct if >24
        result_time.hour = (second_time.hour + self.hour +
                                         minutes_correction)%24
        return result_time

    def __str__(self):
        return 'A {} object {}:{:02d}:{:02d}'.format(type(self).__name__,
        self.hour, self.minute, self.second)

def main():
    time1, time2 = Time(hour= 2, minute= 42, second= 14),\
                   Time(hour= 1, minute= 17, second= 16)
    print(time1)
    print(time2)
    print(time1 + time2)

main()
