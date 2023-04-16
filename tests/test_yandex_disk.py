import yandex_disk_api
import unittest
from yandex_token import token_yandex


class TestYandexDisk(unittest.TestCase):
    def setUp(self) -> None:
        ''' восстановим правильный токен для яндекс.диска'''
        yandex_disk_api.ya_token = token_yandex

    def tearDown(self) -> None:
        pass

    def test_create_new_folder_succesfull(self):
        #чтобы при повторном запуске тестов не стирать вручную папку yandex_folder_name
        if yandex_disk_api.folder_exists(yandex_disk_api.yandex_folder_name):
            yandex_disk_api.delete_folder(yandex_disk_api.yandex_folder_name)
        result = yandex_disk_api.create_new_folder(yandex_disk_api.yandex_folder_name)
        expected = 201
        self.assertEqual(result, expected)

    def test_create_new_folder_fail_token(self):
        '''испортим токен, должны получить ответ от яндекс.диска 401'''
        yandex_disk_api.ya_token = token_yandex + '123'
        result = yandex_disk_api.create_new_folder(yandex_disk_api.yandex_folder_name)
        expected = 401
        self.assertEqual(result, expected)

    def test_folder_exists(self):
        result = yandex_disk_api.folder_exists(yandex_disk_api.yandex_folder_name)
        expected = True
        self.assertEqual(result, expected)

    def test_folder_exists_wrong_name(self):
        result = yandex_disk_api.folder_exists('unexisted_folder')
        expected = False
        self.assertEqual(result, expected)

    def test_folder_exists_code_wrong_name(self):
        result = yandex_disk_api.folder_exists_code('unexisted_folder')
        expected = 404
        self.assertEqual(result, expected)
