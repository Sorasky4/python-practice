'''
パスやファイル名を与え、一定の規則に則った名前のファイル名を0埋めしたものに変更するコードの一部
0から始まらず、数字1～3桁+A~Fの英文字からなるファイル名を0埋めし、数字3桁+A~Fの英文字からなるファイル名に統一する
'''

import re

class FileManagement:

    def __init__(self):
        self.path = ''  # ファイルの絶対パス
        self.name = ''  # ファイルの名前
        self.regex = ''  # ファイルの名前を検索するための正規表現
        self.match = '' # パターンマッチしたオブジェクトを渡す

    def zero_padding(self):
        # 競プロコードのファイル名で0埋めされたものとされていないものが混在しているため、0埋めに統一したい
        # 例) 1A→001A, 26D→026Dのようにする
        # 元のファイルの数字部分は1~999までで、英語部分はA~Fまでとし、01A,02Cのように0から始まるものはマッチさせない
        self.regex = re.compile(r'(^[^0]\d{0,2})([A-F]$)')
        self.match = self.regex.search(self.name)
        if self.match is not None:  # パターンマッチすれば0埋めし、今回はpyファイルなので.pyをつける
            self.name = self.match.group(1).zfill(3) + self.match.group(2) + '.py'
        '''
        else:
            self.name += '.py'  # テストのときだけコメントアウトを外す
        '''