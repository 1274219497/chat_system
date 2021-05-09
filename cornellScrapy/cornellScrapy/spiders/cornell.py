import scrapy
class Test(scrapy.Spider):
    name = "cornell"#定义蜘蛛名
    start_urls=['https://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html']#要爬取的网址
    def start_requests(self):
        #定义要爬取的链接
        urls = ['https://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html']
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)#爬取的页面交给parse方法进行处理
    def parse(self, response):
        datas1 = response.xpath('//*[@id="id1"]/div/div/p/text()').extract()
        datas2 = response.xpath('//*[@id="id2"]/div/div/p/text()').extract()
        filename1="movie_lines.txt"
        filename2="movie_conversations.txt"
        with open(filename1, 'w',encoding='utf-8') as f1:
            for each_data1 in datas1:
                f1.write(each_data1)
                f1.write("\n")
        f1.close()

        with open(filename2, 'w', encoding='utf-8') as f2:
            for each_data2 in datas2:
                f2.write(each_data2)
                f2.write("\n")
        f2.close()
