# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line
import this
import time
from math import sin
import datetime


def main():
    # wait(1)
    print(my_sin(1.5))
    print(iso_now())


def wait(seconds):
    time.sleep(seconds)


def my_sin(float_number):
    return sin(float_number)

def iso_now():
    today_date = datetime.datetime.today()
    iso_date = today_date.isoformat(timespec='minutes')
    return iso_date

if __name__ == '__main__':
    main()