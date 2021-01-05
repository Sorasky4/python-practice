import os
import shutil
from paths import path_abc  # 同フォルダに必要なパスが書かれたファイルを用意
from file_management import FileManagement

for foldername, subfolders, filenames in os.walk(path_abc):
    for filename in filenames:
        file = FileManagement()
        file.path = foldername + '\\' + filename
        file.name = filename
        file.zero_padding()
        '''
        shutil.move(hoge, fuga)はファイルやフォルダに対し移動及び名前の変更をするため、
        print(hoge, fuga)で大丈夫なことを必ず確認した後にコメントアウトを消し、実行する
        '''
        # shutil.move(file.path, foldername + '\\' + file.name)
        print(file.path, foldername + '\\' + file.name)