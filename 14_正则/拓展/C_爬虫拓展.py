import requests
import re
#1、拿到网易云资源地址 url
    #步骤一：F12 开发者工具
    #步骤二：找到正确的资源包
    #步骤三：复制标头的请求url
# url = 'https://music.163.com/playlist?id=3001035934'
path = 'https://music.163.com/playlist?id='
ID = input("请输入歌单id:")
URL = path + ID
#2、伪装请求头--》应对反爬策略（安检-》验证身份）   UA伪装
heads = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
#3、伪装浏览器去骗取网易云服务器的数据，
response = requests.get(url=URL,headers=heads)
# 得到网页源码数据
html = response.text
# print(html)
#4、解析网易云服务器获取的数据
# HTML在线格式化工具网址  http://www.wetools.com/html-formatter
# 正则数据源：html
# 正则表达式：<li><a href="/song\?id=(\d+)">(.*?)</a></li>
# r修饰的字符串是一个普通字符串，python在识别到的时候，会知道里面的内容是取消转义。
# 单用r其实还是不够保险，一般建议用\取消转义后加上r修饰最好。
musicList = re.findall(r'<li><a href="/song\?id=(\d+)">(.*?)</a></li>',html)
print(musicList)


for musci_id ,music_name in musicList:
    print(musci_id ,music_name,"正在下载！")
    # 5、根据歌曲id获取歌曲数据
    music_url = f'http://music.163.com/song/media/outer/url?id={musci_id}.mp3'
    music = requests.get(url=music_url,headers=heads).content
    # 6、将拿到的歌曲（二进制）数据写入电脑，并保存为MP3文件
    with open("./歌曲资源//"+music_name+".mp3","wb")as f:
        f.write(music)
print("歌曲下载成功！")

# 解析网址 f'http://music.163.com/song/media/outer/url?id={歌曲id}.mp3'

