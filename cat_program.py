import random
x = random.randint(1,3)
import os
path = filename = input("表示したいファイル名を入力してください：")
is_file = os.path.isfile(path)

if is_file:
  f = open(filename,encoding="utf8")
  data = f.read()
  for i in range(x):
    print(data)
else:
  print("ファイルを発見できませんでした")

  
  
