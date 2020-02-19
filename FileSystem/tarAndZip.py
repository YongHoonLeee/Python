import tarfile
import zipfile
import glob
import os

#os.mkdir('FileSystem/test')
#os.mkdir('FileSystem/test/subdir')
# with tarfile.open('test.tar.gz','w:gz') as tr:
#     tr.add('test')

with zipfile.ZipFile('test.zip','w') as z:
    z.write('FileSystem/test/sub_dir/ziptest.txt')


