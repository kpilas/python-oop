class Time:
    def __init__(self, hour, minutes, seconds):
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hour(self):
        return self.__dict__['hour']

    @hour.setter
    def hour(self, value):
        if isinstance(value, int) and 0 <= value <= 23:
            self.__dict__['hour'] = value
        else:
            print('Błędne dane. Ustawiono wartośc domyślną godziny: 0.')
            self.__dict__['hour'] = 0

    @property
    def minutes(self):
        return self.__dict__['minutes']

    @minutes.setter
    def minutes(self, value):
        if isinstance(value, int) and 0 <= value <= 59:
            self.__dict__['minutes'] = value
        else:
            print('Błędne dane. Ustawiono wartośc domyślną minut: 0.')
            self.__dict__['minutes'] = 0

    @property
    def seconds(self):
        return self.__dict__['seconds']

    @seconds.setter
    def seconds(self, value):
        if isinstance(value, int) and 0 <= value <= 59:
            self.__dict__['seconds'] = value
        else:
            print('Błędne dane. Ustawiono wartośc domyślną sekund: 0.')
            self.__dict__['seconds'] = 0

    def set_time(self, hour = 0, minutes = 0, seconds = 0):
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return (f'{self.hour if self.hour < 12 else self.hour - 12:02}:{self.minutes:02}:'
                f'{self.seconds:02} {"AM" if self.hour < 12 else "PM"}')


t = Time(13, 12, 45)
# t.hour = 24
print(t)
