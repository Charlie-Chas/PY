
import requests
import re
import parsel

# print(response.text)

url = 'https://www.luoxiabook.com/zhigengniao/'
response = requests.get(url)
response.encoding = 'UTF-8'


href = re.findall('<li class="list-group-item col-md-4 vv-book"><a href="(.*?)" title=".*?">.*?</a></li>',response.text)
print(href)
for index in href:
# import os
    # url = "https://www.99csw.com/book/8831/index.htm"

    response = requests.get(index)
    response.encoding = 'UTF-8'
# filename = '杀死一只知更鸟'
# if not os.path.exists(filename):
#     os.mkdir(filename)



    selector = parsel.Selector(response.text)

    title = selector.css('body > div > div > div > div > div.panel-footer.col-md-12 > h1::text').get()


    content_list = selector.css('#content::text').getall()

    content = '\n'.join(content_list)
    # print(content) 

    f= open('杀死一只知更鸟.txt', mode='a',encoding='utf-8')
    f.write(title)
    f.write('\n')
    f.write(content)
    f.write('\n')

    f.close()
