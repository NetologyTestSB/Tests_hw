import unittest
from parameterized import parameterized
import lect_4_hw

class TestOldHW(unittest.TestCase):

    @parameterized.expand([
        [['2018-01-01', 'yandex', 'cpc', 100], {'2018-01-01': {'yandex': {'cpc': 100}}}],
        [['1', '2', '3', 4, 5, 6], {'1': {'2': {'3': {4: {5: 6}}}}}],
        [[1, 2, 3], {1: {2: 3}}],
        [[], None]
    ])
    def test_nested_dict(self, input_list, correct_dict):
        result = lect_4_hw.nested_dict(input_list)
        if isinstance(result, dict):
            self.assertDictEqual(result, correct_dict)
        else:
            self.assertEqual(result, correct_dict)


    @parameterized.expand([
        [{'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}, 'yandex'],
        [{'facebook': 255, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}, 'facebook'],
        [{'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 400, 'email': 42, 'ok': 98}, 'google'],
        [{'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 555}, 'ok'],
        [{}, None]
    ])
    def test_statistics(self, input_dict, correct_str):
        result = lect_4_hw.statistics(input_dict)
        self.assertEqual(result, correct_str)


    @parameterized.expand([
        [{'user1': [213, 213, 213, 15, 213], 'user2': [54, 54, 119, 119, 119], 'user3': [213, 98, 98, 35]},
         [213, 15, 54, 119, 98, 35]],
        [{'user1': [213, 213, 213, 213], 'user2': [54, 54, 119, 119, 119], 'user3': [213, 98, 98, 35, 15]},
         [213, 15, 54, 119, 98, 35]],
        [{'user1': [213, 213, 213], 'user2': [54, 54], 'user3': [213, 98, 98, 35, 213]},
         [213, 54, 98, 35]],
        [{}, None]
    ])
    def test_uniq_id(self, input_dict, expected):
        result = lect_4_hw.uniq_id(input_dict)
        if isinstance(result, list):
            self.assertSequenceEqual(sorted(result), sorted(expected))
        else:
            self.assertEqual(result, expected)