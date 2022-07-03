from yandex_api import YaUploader
from yandex_token_file import TOKEN


if __name__ == '__main__':
    file = r'D:\Python\Netology\netology_api_task\text.txt'
    token = TOKEN
    uploader = YaUploader(token)
    uploader.upload(file_path=file)