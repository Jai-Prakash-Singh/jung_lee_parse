from requests import Session
from random import choice
#import logging
import requests

#logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-10s) %(message)s')


#pass_ip_list = ['190.207.184.229', '109.175.8.38', '120.202.249.233', '122.146.176.41', '210.101.131.232', '210.101.131.231', '109.175.8.45', '125.214.171.26', '94.228.205.33', '107.17.100.254', '103.11.116.46', '218.207.208.55  ']


def main(link):
    f = open("/home/desktop/proxy_http_auth.txt")
    #f = open("/home/user1/proxy_http_auth.txt")
    pass_ip_list = f.read().strip().split("\n")
    f.close()

    headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:23.0) Gecko/20100101 Firefox/23.0'}

    for l in xrange(6):
        pass_ip = choice(pass_ip_list)
        pass_ip = pass_ip.strip()
        #pass_ip = "%s:8080" %(pass_ip)
        #pass_ip = "vinku:india123@%s" %(pass_ip.strip())

        try:
            http_proxy = "http://" + pass_ip

            proxyDict = {"http"  :http_proxy}
            #r = requests.get(link,  proxies = proxyDict, headers=headers, timeout = 5)
            session = Session()
            r = session.get(link,  proxies = proxyDict, headers=headers, timeout = 5)
            #r = session.get(link)

            if r.status_code in [200, 301]:
                page = r.content

                #logging.debug(r.status_code)
                r.cookies.clear()

                r.close()
                return page

            else:
                r.cookies.clear()
                r.close()

        except:
            pass

    return None




if __name__=="__main__":
    link = "http://www.flipkart.com/united-colors-benetton-men-s-solid-casual-shirt/p/itmdvjfhuknafbsv?pid=SHTDTH99CD9CUAY4&srno=b_1&ref=aee8d63b-38ab-4d95-b96f-9d930f81c548"
    page = main(link)
    print page
