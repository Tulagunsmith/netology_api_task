import requests
from pprint import pprint
from datetime import datetime, timedelta


def get_date():
    date = datetime.now() - timedelta(days=2)
    unix_date = date.timestamp()
    return int(unix_date)


class StackLoader:
    def __init__(self):
        self.headers = {'Content-Type': 'application/json'}
        self.url = 'https://api.stackexchange.com/questions'

    def get_api_response(self, start_date):
        response = False
        params = {
            'site': 'stackoverflow',
            'tagged': 'python',
            'fromdate': start_date,
            'todate': f'{int((datetime.now()).timestamp())}',
            'sort': 'month',
            'order': 'desc'
        }
        if requests.get(url=self.url, params=params).status_code == 200:
            response = requests.get(url=self.url, params=params).json()
        return response


if __name__ == '__main__':
    start_datetime = get_date()
    questions = StackLoader()
    stack_questions = questions.get_api_response(start_date=start_datetime)
    pprint(stack_questions)
