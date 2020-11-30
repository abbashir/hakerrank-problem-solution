import json
import time
import datetime


def test():
    My_data = {}

    My_data['a'] = str(datetime.datetime.now())
    # WRITE
    with open("making_json.json", "w") as f:
        json.dump(My_data, f)

    f = open('making_json.json', )
    fetch_data = json.load(f)
    f.close()
    a = fetch_data['a']
    print(a)


while True:
    test()
    waiting_time_In_Min = 1
    next_run_time = datetime.datetime.now() + datetime.timedelta(minutes=waiting_time_In_Min)

    print(f'Next Run Time: {next_run_time}')

    time.sleep(waiting_time_In_Min * 60)
