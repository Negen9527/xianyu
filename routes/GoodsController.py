import datetime
import time

from flask import Flask, request, Blueprint
from models.Goods import Goods
from services.GoodsService import GoodsService
from db import db
from utils.XuanDan import XuanDan
import json
goodsController = Blueprint("goods", __name__)

@goodsController.route('/add', methods=['GET','POST'])
def addGoodsInfo():
    postJson = json.loads(request.get_data())
    # postJson = request.get_json()
    itemId = postJson['itemId']
    title = postJson['title']
    originalPrice = float(postJson['originalPrice'])
    couponUrl = postJson['couponUrl']
    imageUrl = postJson['imageUrl']
    overTime = postJson['overTime']
    overTime = datetime.datetime.strptime(overTime, "%Y-%m-%d")
    goods = Goods(itemId, title, originalPrice, couponUrl, imageUrl, overTime, False)
    goodsService = GoodsService()
    goodsService.addGoodsInfo(goods)
    return "ok"

@goodsController.route('/getItemInfo', methods=['GET'])
def getGoodsInfo():
    itemUrl = request.args.get("itemUrl")
    xuanDan = XuanDan()
    return xuanDan.getItemInfos(itemUrl)


