import requests
from yandex_token_file import TOKEN
import os


class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_upload_url(self, file_path):
        params = {'path': file_path, 'overwrite': 'true'}  # file_path - путь, где файл будет в яндексе
        response = requests.get(url=self.url, headers=self.headers, params=params)
        return response.json()

    def upload(self, file_path: str):
        file_name = os.path.basename(file_path)
        href = self.get_upload_url(file_name).get("href", "")
        response = requests.put(url=href, data=open(file_path, 'rb'))  # file_name - путь до файла в системе
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")
        else:
            print('God damn you!')


if __name__ == '__main__':
    file = r'D:\Python\Netology\netology_api_task\text.txt'
    token = TOKEN
    uploader = YaUploader(token)
    uploader.upload(file_path=file)

