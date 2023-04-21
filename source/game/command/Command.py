import datetime


class Command:

    def __init__(self, value: str):
        self.__value = value
        self.time_stamp = datetime.datetime.now()
