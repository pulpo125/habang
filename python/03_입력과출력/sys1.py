# pythin sys1.py aaa bbb ccc
import sys

args = sys.argv[1:]
# for arg in args:
#     print(arg)

total = 0
for arg in args:
    total += int(arg)

print('합계: ', total)
# 터미널 파일 이동 cd ../ 상위폴더 이동
# cd/하위폴더명
