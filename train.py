from data_loader import *
from network import *

import os
import sys

rootpath = os.getcwd()
syspath = sys.path
sys.path = []
sys.path.append(rootpath)  # 将工程根目录加入到python搜索路径中
sys.path.extend([rootpath + i for i in os.listdir(rootpath) if i[0] != "."])  # 将工程目录下的一级目录添加到python搜索路径中
sys.path.extend(syspath)

if __name__ == "__main__":
    my_data_loader = MaskData()
    X, y = my_data_loader.load_data()
    my_model = MaskOrNotNetwork(X, y)
    history = my_model.train()
    test_loss, test_accuracy = my_model.test()
    my_model.save(os.path.join(os.getcwd(), "MaskOrNot.h5"))
