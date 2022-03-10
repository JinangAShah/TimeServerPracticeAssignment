# Server file

from flask import Flask, request
from datetime import datetime, time, timedelta
import math

app = Flask(__name__)

db = []


def add_datetime_to_db(date, units):
    new_datetime = {'date': date,
                    'units': units
                    }
    return new_datetime


@app.route('/time', methods=["GET"])
def current_time():
    date_to_string = datetime.now().time() \
        .strftime("Current time is %H hours %M minutes %S seconds")
    return date_to_string


@app.route('/date', methods=["GET"])
def current_date():
    date_to_string = datetime.now().date() \
        .strftime("Today's date is %m-%d-%y")
    return date_to_string


@app.route('/age', methods=["POST"])
def age_calc():
    a = request.get_json()
    in_date = a['date'].split('/')
    x = datetime.date(datetime(int(in_date[2]),
                               int(in_date[0]), int(in_date[1])))

    todays_date = datetime.now().date()

    if a['units'] == 'years':
        unit = 365

    c = todays_date - x
    age = c.days / unit
    print('Your age is {} years'.format(age))
    return 'Your age is ' + str(float(age)) + ' years'


@app.route('/until_next_meal/<meal>', methods=["GET"])
def time_until_meal(meal):
    present_time = datetime.now().time()
    # present_time = time(13, 0, 0)

    print(present_time)
    print(type(present_time))
    c = datetime.now()
    if meal == 'lunch':
        meal_time = time(13, 0, 0)
        print(meal_time)
    elif meal == 'breakfast':
        meal_time = time(9, 0, 0)
        print(meal_time)
    elif meal == 'dinner':
        meal_time = time(18, 30, 0)
        print(meal_time)
    temp_time = datetime.date(datetime(year=c.year, month=c.month, day=c.day))
    datetime1 = (datetime.combine(temp_time, present_time))
    datetime2 = (datetime.combine(temp_time, meal_time))
    time_elapsed = datetime2 - datetime1
    print('time elapsed is {}'.format(time_elapsed))

    if time_elapsed.total_seconds() >= 0:
        meal_time_in = (time_elapsed +
                        timedelta(hours=0, minutes=0, seconds=0))
    elif time_elapsed.total_seconds() < 0:
        meal_time_in = (time_elapsed +
                        timedelta(hours=24, minutes=0, seconds=0))

    print('time in seconds is {}'.format(meal_time_in.total_seconds()))
    hours = meal_time_in.total_seconds() // 3600
    print('hours is {}'.format(hours))
    minutes = (meal_time_in.total_seconds() // 60) % 60
    print('minutes is {}'.format(minutes))
    seconds = meal_time_in.total_seconds() - hours * 3600 - minutes * 60
    if seconds / 60 > 0:
        minutes = minutes + 1
    print(hours, minutes)
    return 'Time until next ' \
           '{}: {} hours'.format(meal, hours + math.ceil(minutes) * 0.01)


if __name__ == "__main__":
    app.run(debug=False)
