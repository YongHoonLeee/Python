import os
import pathlib
import glob
import shutil

ex =os.path.exists('test.txt')
print(ex)
# 존재하지 않아도 false 인듯하다.
ex = os.path.isfile('Datature')
print(ex)

ex = os.path.isdir('ModuleSys')
print(ex)
# change name
os.rename
# symbolic link make
os.symlink

os.mkdir

os.rmdir
# 빈 파일 생성하기 ㅋㅋ
pathlib.Path('wowwow.py').touch()
# remove file
os.remove('wowwow.py')
# list in folder by list
ex =os.listdir('FileSystem')
print(ex)

# copy
#shutil.copy()

# shutil.rmtree('pwd') 이거 폴더 안에 있어서 싹다 날림 조심

ex = os.getcwd()
print(ex)