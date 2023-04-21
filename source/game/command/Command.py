import datetime


class Command:

    def __init__(self, value: str):
        self.__value = value
        # Order player actions by time
        self.time_stamp = datetime.datetime.now()
