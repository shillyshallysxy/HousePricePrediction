from bs4 import BeautifulSoup
from lib.item.fangzi import *
from lib.zone.area import *
import json
import os


def get_contents(urls):
    content = requests.get(urls, timeout=10, headers=create_headers()).content
    return content


def get_fangzi_detail(content):
    fangzi_list_ = []
    soup = BeautifulSoup(content, 'lxml')
    fangzi_details = soup.find_all('div', class_='info clear')
    for fangzi_detail in fangzi_details:
        fangzi_detail_title = fangzi_detail.contents[1].text.strip().replace('\n', ' ')
        fangzi_detail_size = [item.strip().split('\n')[0].replace('\n', '') for item in
                              fangzi_detail.contents[3].text.strip().split('|')
                              ][1:]
        fangzi_detail_price = [item.strip() for item in
                               fangzi_detail.contents[3].contents[9].text.strip().split('\n')
                               if item.strip() != '']
        try:
            if len(fangzi_detail_size) == 3:
                fangzi_ = FangZi(fangzi_detail_title, fangzi_detail_size[0], fangzi_detail_size[1],
                                 fangzi_detail_price[1], fangzi_detail_price[0], fangzi_detail_size[2])
            else:
                fangzi_ = FangZi(fangzi_detail_title, fangzi_detail_size[0], fangzi_detail_size[1],
                                 fangzi_detail_price[1], fangzi_detail_price[0])
        except:
            fangzi_ = FangZi()
            print(fangzi_detail_title)
            print(fangzi_detail_size)
            print(fangzi_detail_price)
        fangzi_list_.append(fangzi_)
    return fangzi_list_


def get_house_detail_list(house_detail_response):
    house_detail_soup = BeautifulSoup(house_detail_response, 'lxml')
    house_details = house_detail_soup.find_all('div', class_='xiaoquInfoItem')
    # for house_detail in house_details:
    # house_label = house_details[3].contents[1].contents[0].strip()
    if len(house_details) == 0:
        house_developer = ''
    else:
        house_developer = house_details[3].text.strip().split('\n')[-1]
    # print(house_label,":",house_content)
    if SPIDER_NAME == 'ke':
        all_house_href = house_detail_soup.find_all('a', class_='fr CLICKDATA')
    else:
        all_house_href = house_detail_soup.find_all('a', class_='fr')
    all_house_href = [house_href for house_href in all_house_href if 'ershoufang' in house_href.attrs['href']]
    if len(all_house_href) == 0:
        fangzi_null = FangZi()
        return [fangzi_null], house_developer
    all_house_href = all_house_href[0].attrs['href']
    all_h_response = requests.get(all_house_href, timeout=10)
    all_h_soup = BeautifulSoup(all_h_response.content, 'lxml')
    page_num = all_h_soup.find_all('div', class_='page-box house-lst-page-box')[0].attrs['page-data']
    page_num = json.loads(page_num)['totalPage']
    href_root = all_house_href[0:-1].rpartition('/')
    fangzi_list = []
    for i in range(page_num):
        if i != 0:
            href_now = '{}{}pg{}{}'.format(href_root[0], href_root[1], i+1, href_root[2])
            fangzi_list.extend(get_fangzi_detail(get_contents(href_now)))
        else:
            fangzi_list.extend(get_fangzi_detail(all_h_response.content))
    return fangzi_list, house_developer


# 获取文件大小
def getDocSize(path):
    try:
        size = os.path.getsize(path)
        size = float(size)
        kb = size / 1024
        return kb
    except Exception as err:
        print(err)


if __name__ == '__main__':
    with open('aaa.txt', 'rb') as f:
        strrr = f.read().decode('utf-8')
    fangz_list, dev = get_house_detail_list(strrr)
    print(1)