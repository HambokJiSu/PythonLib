#	현재 디렉토리의 모든 텍스트 파일을 archive라는 디렉토리로 이동, archive는 현 폴더 하위에 존재한다는 가정

#	use glob, os, shutil
# import glob
# import os
# import shutil


# for file_path in glob.glob('%s/*.txt' % os.getcwd()):
#     parent = os.path.dirname(file_path)
#     filename = os.path.basename(file_path)
#     new_path = os.path.join(parent, 'archive', filename)
#     shutil.move(file_path, new_path)

#	use pathlib 
import pathlib


for p in pathlib.Path.cwd().glob('*.txt'):
    new_p = p.parent.joinpath('archive', p.name)
    p.replace(new_p)

#	현 폴더 모들 파일 확장자별 개수 구하기
import collections, pathlib
ct = collections.Counter([p.suffix for p in pathlib.Path.cwd().iterdir()])
print(ct)

#	디렉토리 구성 확인	os.path
import os

def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        filepath = os.path.join(dirname, filename)
        if os.path.isdir(filepath):
            search(filepath)
        elif os.path.isfile(filepath):
            name, ext = os.path.splitext(filepath)
            if ext == '.py': 
                print(filepath)


search("c:/projects/pylib")  # c:/projects/pylib 디렉터리와 하위 디렉터리의 모든 .py 파일 출력

#	pathlib 활용
import pathlib

def search(dirname):
    for p in pathlib.Path(dirname).rglob('*.py'):
        print(p)

#	여러개의 파일을 한꺼번에 읽기
import fileinput
import glob

with fileinput.input(glob.glob("*.txt")) as f:
    for line in f:
        print(line)

#	디렉터리간 파일을 비교하려면? ― filecmp
import filecmp

fd = filecmp.dircmp('a', 'b')

for a in fd.left_only:
    print("a: %s" % a)

for b in fd.right_only:
    print("b: %s" % b)

for x in fd.diff_files:
    print("x: %s" % x)


#	파일을 찾으려면? ― glob
import glob

for filename in glob.glob("**/*.txt", recursive=True):
    print(filename)

#	특정 파일만 찾으려면? ― fnmatch
import fnmatch
import os

for filename in os.listdir('.'):
    if fnmatch.fnmatch(filename, 'a???[0-9].py'):
        print(filename)

"""
패턴	의미
*		모든 것과 일치
?		모든 단일 문자와 일치
[seq]	seq의 모든 문자와 일치
[!seq]	seq에 없는 모든 문자와 일치
"""

#	파일에서 랜덤으로 한 줄만 가져오려면	linecache
import linecache
import random

no = random.randint(1, 100)
print(linecache.getline('saying.txt', no))


#	파일을 복사하거나 이동하려면? ― shutil
import shutil

shutil.copy("c:/doit/a.txt", "c:/temp/a.txt.bak")	#	복사
shutil.move("c:/doit/a.txt", "c:/temp/a.txt")		#	이동