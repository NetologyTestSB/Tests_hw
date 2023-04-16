import requests
import json
from yandex_token import token_yandex
from pprint import pprint

folder_url = 'https://cloud-api.yandex.net/v1/disk/resources'
yandex_folder_name = 'test_folder'
ya_token = token_yandex

def get_headers():
    return {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(ya_token)
        # 'Authorization': 'OAuth {}'.format(token_yandex)
    }

def get_headers_param(token):
    return {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(token)
        # 'Authorization': 'OAuth {}'.format(token_yandex)
    }

def create_new_folder(folder_name):
    ''' создание новой папки на яндекс.диске'''
    headers = get_headers_param(ya_token)
    try:
        response = requests.put(folder_url, headers=headers, params={'path': folder_name})
        response.raise_for_status()
    except:
        pass
    return response.status_code

def folder_exists(folder_name) -> bool:
    ''' проверка существования папки на яндекс.диске'''
    headers = get_headers()
    try:
        response = requests.get(folder_url, headers=headers, params={'path': folder_name})
        response.raise_for_status()
        if response.status_code == 200:
            response_dict = json.loads(response.text)
            if response_dict['name'] == folder_name:
                return True
    except:
        pass
    return False

def folder_exists_code(folder_name) -> bool:
    ''' проверка существования папки на яндекс.диске с возвратом кода ответа сайта'''
    headers = get_headers()
    try:
        response = requests.get(folder_url, headers=headers, params={'path': folder_name})
        response.raise_for_status()
        if response.status_code == 200:
            response_dict = json.loads(response.text)
            if response_dict['name'] == folder_name:
                return 200
    except:
        pass
    return response.status_code

def delete_folder(folder_name):
    ''' удаление папки на яндекс.диске'''
    headers = get_headers()
    try:
        response = requests.delete(folder_url, headers=headers, params={'path': folder_name})
        response.raise_for_status()
    except:
        pass
    return response.status_code

def get_files_list():
    ''' получение плоского (из всех папок) списка всех файлов с яндекс.диска '''
    files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
    headers = get_headers()
    response = requests.get(files_url, headers=headers, params={'limit': 100})
    dct = response.json()
    return dct

def get_folders_list():
    ''' получение списка всех папок с яндекс.диска (корневых, без вложенных) '''
    files_url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = get_headers()
    response = requests.get(files_url, headers=headers, params={'limit': 100, 'path': '/', 'type': 'dir'})
    dct = response.json()
    return dct


if __name__ == '__main__':
    #print(create_new_folder(yandex_folder_name))
    #print(folder_exists(yandex_folder_name))
    #print(delete_folder(yandex_folder_name))
    pprint(folder_exists_code('unexisting_folder'))


