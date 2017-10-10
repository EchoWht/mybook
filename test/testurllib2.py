import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
keywords=urllib.parse.quote("Head First Python",safe='')
url="https://search.jd.com/Search?keyword="+keywords+"&enc=utf-8&suggest=4.def.0.T01&wq=head&pvid=mx07bqvi.f86hvj"
print (url)

response = urlopen(url)
# html文档
html = response.read()
# 打印状态码
print(response.getcode())

soup = BeautifulSoup(html,"html.parser",from_encoding="utf-8")
link_node=soup.find_all('a')
# 获取第一个商品的图片
img_node=soup.find('img',class_="err-product")
print (img_node['src'])

# 获取价格
price_node=soup.find('div' , class_="p-price").find('strong').find('i')
print (price_node.get_text())

# 获取图书购买链接
buy_link=soup.find('div' , class_="p-img").find('a')
print (buy_link["href"])

# 获取图书简介
url2="https:"+buy_link["href"]

response2 = urlopen(url2)
# html文档
html2 = response2.read()
soup2 = BeautifulSoup(html2,"html.parser",from_encoding="utf-8")
book_detail_content=soup2.find('div' , class_="book-detail-content").find('p')
print (type(book_detail_content.get_text()))