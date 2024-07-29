import requests
import os
import re
import time

u = input('请输入网易云歌单链接：')

rid = re.findall("id=(\d+)",u)
for id in rid:
    eid = id[0]
url = f'https://music.163.com/discover/toplist?id={eid}'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'cookie': ''
}
filename = 'D:music\\'
if not os.path.exists(filename):
    os.makedirs(filename)
resqonse = requests.get(url=url,headers=headers)
re_id = re.findall('<li><a href="\/song\?id=(\d+)">(.*?)</a>',resqonse.text)
for id_name in re_id:
    rid = id_name[0]
    #
    rname = id_name[1]
    #print(rname)
    music_url = f'https://api.shserve.cn/api/wyy?url=https://y.music.163.com/m/song?id={rid}'
    ye_url = requests.get(url=music_url)
    music_song_url = ye_url.json()['music']
    song = requests.get(url=music_song_url).content
    with open(filename + rname +'.mp3',mode='wb', )as fp:
        fp.write(song)
        time.sleep(1)
        print(f'正在下载"{rname}"')
print('下载完成{}首歌曲'.format(len(re_id)))
