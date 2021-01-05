import unittest
from file_management import FileManagement

class TestFileManagement(unittest.TestCase):

    # 最小ケースで正常に0埋めされて返ってくるか
    def test_zero_padding1(self):
        file = FileManagement()
        file.name = '1A'
        file.zero_padding()
        self.assertEqual(file.name, '001A.py')

    # 数字が0から始まるときは余分に0埋めされずに返ってくるか
    def test_zero_padding2(self):
        file = FileManagement()
        file.name = '02B'
        file.zero_padding()
        self.assertEqual(file.name, '02B.py')

    # 英文字が2つ以上あるときは0埋めされずにそのまま返ってくるか
    def test_zero_padding3(self):
        file = FileManagement()
        file.name = '3AC'
        file.zero_padding()
        self.assertEqual(file.name, '3AC.py')

    # 英文字がA-F以外のときは0埋めされずにそのまま返ってくるか
    def test_zero_padding4(self):
        file = FileManagement()
        file.name = '11G'
        file.zero_padding()
        self.assertEqual(file.name, '11G.py')

    # 0埋めの最大ケースで正常に返ってくるか
    def test_zero_padding5(self):
        file = FileManagement()
        file.name = '99F'
        file.zero_padding()
        self.assertEqual(file.name, '099F.py')

    # 数字3桁のときはそのまま返ってくるか
    def test_zero_padding6(self):
        file = FileManagement()
        file.name = '100D'
        file.zero_padding()
        self.assertEqual(file.name, '100D.py')

    # 数字が無いときはそのまま返ってくるか
    def test_zero_padding7(self):
        file = FileManagement()
        file.name = 'E'
        file.zero_padding()
        self.assertEqual(file.name, 'E.py')