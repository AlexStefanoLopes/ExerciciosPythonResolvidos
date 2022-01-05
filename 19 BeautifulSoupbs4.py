# O exercício How To Decode A Web Page 2 foi uma continuação do prelúdio extremamente desafiador, How To Decode
# A Web Page. O objetivo do original (e do exercício de acompanhamento) era dar às pessoas a chance de vasculhar
# uma aplicação quase real do Python.

# import requests
# from bs4 import BeautifulSoup
#
# base_url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
# r = requests.get(base_url)
# soup = BeautifulSoup(r.text)
#
#
# all_p_cn_text_body = soup.select("div.parbase.cn_text > div.body > p")
#
# for elem in all_p_cn_text_body[7:]:
#   print(elem.text)

import requests
from bs4 import BeautifulSoup

def print_to_text(base_url):
    """
    :param base_url: URL of article to scrape
    :return: naked content to text file
    """
    r = requests.get(base_url)
    soup = BeautifulSoup(r.text)
    with open("work less.txt", "w") as textfile:
        for paragraph in soup.find_all(dir="ltr"):
            textfile.write(paragraph.text.replace("<span>",""))

if __name__ == "__main__":
    #Chose my own article
    base_url = "http://www.theatlantic.com/business/archive/2014/08/to-work-better-work-less/375763/"
    base_url2 = "http://www.theatlantic.com/business/archive/2014/08/to-work-better-work-less/375763/2/"
    print_to_text(base_url)
    print_to_text(base_url2)