import sys
import os
import datetime as dt

from dotenv import load_dotenv
import requests


load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
TASK_JORNADA_LABORAL = os.getenv("TASK_JORNADA_LABORAL")

DATETIME_FORMAT = "%Y-%m-%d"
SECONDS_IN_HOUR = 3600
TIME_SLOTS = [
    ['09:00:00', '13:00:00'],
    ['14:00:00', '18:00:00'],
]


def main(ini, fin):
    curr = ini
    while curr <= fin:
        for slot in TIME_SLOTS:
            data = {
                'date': dt.datetime.strftime(curr, DATETIME_FORMAT),
                'duration': str(4*SECONDS_IN_HOUR),
                'start_time': slot[0],
                'end_time': slot[1],
                'task_id': TASK_JORNADA_LABORAL
            }

            # POST time-entry request
            response = requests.post(f"https://app.timecamp.com/third_party/api/entries/format/json/api_token/{API_TOKEN}",
                                     json=data)

            print(response.json())
        curr += dt.timedelta(days=1)


if __name__ == "__main__":
    ini = dt.datetime.strptime(sys.argv[1], DATETIME_FORMAT)
    fin = dt.datetime.strptime(sys.argv[2], DATETIME_FORMAT)
    main(ini, fin)
