import scrapy
import requests

class PDFSpider(scrapy.Spider):
    name = "pdfs"
    start_urls=[
        'http://ir.expediainc.com/annuals.cfm'
    ]

    def __init__(self, *args, **kwargs):
        super(PDFSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        docLists = response.xpath('//table[@class="dataTable"]//tr[@class="primary" or @class="alternate"]/td[@style="width:82%"]')
        for docList in docLists:
            file_url = "http://ir.expediainc.com/" + docList.xpath('a[@class="docList"]/@href').extract_first()
            file_name = docList.xpath('a[@class="docList"]/text()').extract_first() + ".pdf"
            http_response = requests.get(file_url, stream = True)
            with open("Reports/" + file_name, "wb") as pdf:
                for chunk in http_response.iter_content(chunk_size=1024):
                     # writing one chunk at a time to pdf file
                     if chunk:
                         pdf.write(chunk)
