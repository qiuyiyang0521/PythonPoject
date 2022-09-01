# -*- coding: utf-8 -*-
# @Author: qiuyiyang
# @Date: 2022-07-07 15:23:15
# @Email: 22133090041@qq.com
# @Last_modified_by: qiuyiyang
# @Last_modified_time: 2022-07-13 19:10:14

import sys
import os 
sys.path.append("E:\\GitHub\\PythonPoject\\计算图形\\2D")
sys.path.append("E:\\GitHub\\PythonPoject\\计算图形\\3D")
from 圆 import rounds
from 三角形 import triangles
from 梯形 import trapezoidal
from 正方形 import square
from 长方形 import rectangular
C = 60
S = 300
x = 0
z = 1
while True:
    x = C / 2 - z
    if x * z == S:
        print("{},{}".format(x,z))
        break
    print(x,z)
    z += 1
os.system("pause")
    
