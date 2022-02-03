import datetime


def add(moment):
    # receive a date time and return a date time
    return moment + datetime.timedelta(seconds=1e9)
