import tempfile
import os
# 바로 지워짐
with tempfile.TemporaryFile(mode='w+') as t:
    t.write('hello temporary file')
    t.seek(0)
    print(t.read())

# 안지워지는버전

with tempfile.NamedTemporaryFile(delete=False)as t:
    print(t.name)
    with open(t.name,'w+') as f:
        f.write('test\n')
        f.seek(0)
        print(f.read())

os.remove(t.name)

with tempfile.TemporaryDirectory() as td:
    print(td)

temp_dir = tempfile.mkdtemp()

#아직 temp file 을 어떨 때 써야하는지 감은 오지 않는다.