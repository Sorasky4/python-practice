import re

class file_management:
    def __init__(self):
        self.path = ''  # ファイルの絶対パス
        self.name = ''  # ファイルの名前
        self.regex = ''  # ファイルの名前を検索するための正規表現
        self.match = '' # パターンマッチしたオブジェクトを渡す

    def zero_padding(self):
        # 競プロコードのファイル名で0埋めされたものとされていないものが混在しているため、0埋めに統一したい
        # 例) 1A→001A, 26D→026Dのようにする
        self.regex = re.compile(r'(^[^0]\d+)([A-F]$)')
        self.match = self.regex.search(self.name)
        if self.match is not None:  # パターンマッチすれば0埋めし、今回はpyファイルなので.pyをつける
            self.name = self.match.group(1).zfill(3) + self.match.group(2) + '.py'