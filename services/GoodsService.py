from db import *

class GoodsService():
    def addGoodsInfo(self, Goods):
        db.session.add(Goods)
        db.session.commit()
        print("记录添加成功")



