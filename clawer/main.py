#导入源文件库
from urllib.request import urlopen

#ouvrir la site corréspond
url1 = "http://www.baidu.com"        #choose the site you want
url2 = "https://www.bilibili.com/"
resp = urlopen(url1)                 #reponse of the site

#print(resp.read().decode('utf-8'))     #afficher les contenus
contenu=resp.read().decode('utf-8')
print(contenu)
                                    #utf-8 is the mode de decode

#if i want to stock the contenu of this site, i going to keep it in a file
with open("contenu.html", mode="w",encoding="utf-8") as f:
    f.write(contenu)
    f.close()

#stokage of the codes source if the zeb site
print("over!")