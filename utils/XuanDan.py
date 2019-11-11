
import requests
from bs4 import BeautifulSoup
import json
'''
选单网：http://www.xuandan.com/
'''
class XuanDan:
    '''
    获取商品的具体信息
    '''
    def getItemInfos(self, itemUrl):
        response = requests.get(itemUrl);
        html = BeautifulSoup(response.text,"html.parser")
        #itemId
        itemId = itemUrl.split("=")[1]

        #标题/详细信息
        title = html.find("p",{"class":"de_con"}).text
        #原价
        originalPrice = html.find("b", {"class":"price-original"}).text
        #券后价
        last_price = html.find("b", {"class":"lastprice"}).text
        #有效日期
        overTime = html.find_all("b", {"class":"price-original"})[1].text
        #领券地址
        couponUrl = html.find("a", {"class":"yhj-btn"}).get('href')
        #主图地址
        imageUrl = html.find("img", {"class":"lazy MainImage"}).get('data-original')
        resultJson = {
            "itemId":itemId,
            "title":title,
            "originalPrice":originalPrice,
            "couponUrl":couponUrl,
            "imageUrl":imageUrl,
            "overTime":overTime
        }
        return resultJson


if __name__ == '__main__':
    xuanDan = XuanDan()
    itemUrl = "http://www.xuandan.com/Detail.html?id=3300530"
    xuanDan.getItemInfos(itemUrl)