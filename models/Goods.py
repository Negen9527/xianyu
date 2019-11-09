
from db import db
"""
1、商品id      itemId
2、标题        title
3、原价        originalPrice
4、优惠券地址   couponUrl
5、主图地址     imageUrl
6、有效期       overTime
7、是否过期     isOver  
"""
class Goods(db.Model):
    __tablename__ = "goods"
    id = db.Column(db.Integer, primary_key=True)
    itemId = db.Column(db.String(8))
    title = db.Column(db.Text)
    originalPrice = db.Column(db.Float(5))
    couponUrl = db.Column(db.Text)
    imageUrl = db.Column(db.Text)
    overTime = db.Column(db.TIMESTAMP)
    isOver = db.Column(db.Boolean)
    def __init__(self, itemId, title, originalPrice, couponUrl, imageUrl, overTime, isOver):
        self.itemId = itemId
        self.title = title
        self.originalPrice = originalPrice
        self.couponUrl = couponUrl
        self.imageUrl = imageUrl
        self.overTime = overTime
        self.isOver = isOver



