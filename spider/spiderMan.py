import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup

# 爬取jd数据
class Jd:
    def __init__(self,keywords):
        self.keywords=urllib.parse.quote(keywords,safe='')
        self.url="https://search.jd.com/Search?keyword="+self.keywords+"&enc=utf-8&suggest=4.def.0.T01&wq=head&pvid=mx07bqvi.f86hvj"
        self.response = urlopen(self.url)
        self.html = self.response.read()
        self.soup = BeautifulSoup(self.html,"html.parser",from_encoding="utf-8")
    # 爬取图片链接
    def getBookImg(self):
        img_node = self.soup.find('img', class_="err-product")
        return img_node['src']
    # 爬取价格
    def getBookPrice(self):
        price=None
        try:
            price_node = self.soup.find('div', class_="p-price").find('strong').find('i')
            price=price_node.get_text()
        except:
            price="0"
        return price
    # 获取详情页
    def getBookDetail(self):
        soup2=None
        try:
            buy_link=self.soup.find('div' , class_="p-img").find('a')
            url="https:"+buy_link['href']
            response2 = urlopen(url)
            # html文档
            html2 = response2.read()
            soup2 = BeautifulSoup(html2, "html.parser", from_encoding="utf-8")
        except:
            pass
        return soup2

    # 爬取作者
    def getBookAuthor(self):
        author=[]
        try:
            soup2=self.getBookDetail()
            author_a=soup2.find('div',class_="p-author").find_all("a")
            for item in author_a:
                author.append(item.get_text())
                print (author)
        except:
            author=None
        return author

