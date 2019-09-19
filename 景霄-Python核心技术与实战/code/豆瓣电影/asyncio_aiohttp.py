"""
用协程爬取北京最近上映的电影，信息包括：名称、上映时间、海报（具体电影描述页面中抓取）
"""

import asyncio
import aiohttp

from bs4 import BeautifulSoup
import time

header={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"}

"""
#异步方法：
async def fetch_content(url):
    async with aiohttp.ClientSession(
        headers=header, connector=aiohttp.TCPConnector(ssl=False)
    ) as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    url = "https://movie.douban.com/cinema/later/shanghai/"
    init_page = await fetch_content(url)
    init_soup = BeautifulSoup(init_page, 'html.parser')

    movie_list = []
    #movie_names, urls_to_fetch, movie_dates, favor_size = [], [], [], []

    all_movies = init_soup.find('div', id="showing-soon")
    for each_movie in all_movies.find_all('div', class_="item"):
        all_a_tag = each_movie.find_all('a')
        all_li_tag = each_movie.find_all('li')
        # print(all_a_tag)
        # print(all_li_tag)
        movie_info = []
        movie_info.append(all_a_tag[1].text)
        movie_info.append(all_a_tag[1]['href'])
        movie_info.append(all_li_tag[0].text)
        movie_info.append(int(all_li_tag[3].text[:-3]))
        movie_list.append(movie_info)

    movie_list = sorted(movie_list, key=lambda m:m[3])
    #print(movie_list)

    tasks = [fetch_content(movie[1]) for movie in movie_list]
    pages = await asyncio.gather(*tasks)

    for movie, page in zip(movie_list, pages):
        soup_item = BeautifulSoup(page, 'html.parser')
        img_tag = soup_item.find('img')
        img_url = img_tag['src']

        print('{} {} {} {}'.format(movie[0], movie[2], movie[3], img_url))

asyncio.run(main())

"""

#同步方法：
import requests

def main():
    url = "https://movie.douban.com/cinema/later/shanghai/"
    init_page = requests.get(url=url,headers=header,timeout=5).content
    init_soup = BeautifulSoup(init_page, 'html.parser')

    all_movies = init_soup.find('div', id="showing-soon")
    for each_movie in all_movies.find_all('div', class_="item"):
        all_a_tag = each_movie.find_all('a')
        all_li_tag = each_movie.find_all('li')

        movie_name = all_a_tag[1].text
        url_to_fetch = all_a_tag[1]['href']
        movie_date = all_li_tag[0].text

        response_item = requests.get(url_to_fetch).content
        soup_item = BeautifulSoup(response_item, 'lxml')
        img_tag = soup_item.find('img')
        img_url = img_tag['src']

        content_item = soup_item.find('div', id="link-report")
        print(content_item)
        print('{} {} {} {}'.format(movie_name, movie_date, img_url))

        try:
            response_img = requests.get(url=img_url,headers=header,timeout=5).content
        except Exception as e:
            print(img_url + 'download failed')
            continue

        filename = 'later/' + movie_name + '.jpg'
        with open(filename, 'wb') as f:
            f.write(response_img)
            print('%s下载成功' % filename)
            time.sleep(1)
        break



main()

