import req_proxy
from bs4 import BeautifulSoup
from lxml import html 
import re 
import time 
import sys
import ast 



special_char = ['! ', ' " ', '# ', '$ ', '%', '& ', "'", '(', ')', '* ', '+', ', ',  '. ', '/ ', ':', '; ', '<', '=', '> ', '? ', '@ ', '[', '\\ ', '] ', '^ ', '_ ', '` ', '{ ', '| ', '} ', '~ ', '\xc2\xb4 ', '#! ', '/* ', '*/ ', '&amp;', '']

special_char = map(str.strip, special_char)

clr_list = set(['red', 'green', 'yellow', 'blue', 'orange', 'purple', 'pink', 'cyan', 'magenta', 'violet', 'brown', 'black', 'gray', 'white'])


def my_strip(x):
    try:
        x = str(x).strip()
    except:
        x = str(x.encode("ascii", "ignore")).strip()
    return x

       
def main(f2, f3, line):    
    line_split = ast.literal_eval(line.strip())
    link = line_split[-1]

    page = req_proxy.main(link)
    soup = BeautifulSoup(page, "html.parser")

    soup.find("div", attrs={"id":"mainTop-1"})
    link_split = filter(None, link.split("/"))
    
    sku = link_split[4]


    pro_title = link_split[2]


    target = "unknown"

    tar_sub_cat_box  = soup.find("div", attrs={"id":"mainTop-1"})
    target1 = " ".join([tagt.get_text() for tagt in tar_sub_cat_box.find_all("a")[1:]]).lower()

    if "women" in target1 :
        target = "women"
    elif "men" in target1:
        target = "men"
    elif "unisex" in target1 :
        target = "unisex"
    elif "boy" in target1 : 
        target = "boy"
    elif "girl" in target1 : 
        target = "girl"
    elif "kid" in target1 : 
        target = "kid"
    elif "home" in target1 : 
        target = "home & decor"
    elif "mobile" in target1  :
        target = "mobile"
    elif "appliance" in target1 : 
        target = "appliance"
    elif "computer" in target1 : 
        target = "computer"
    elif "book" in target1 : 
        target = "book"
    else:
         target = target1


    #target = "unisex"
    target_link = line_split[-2]


    cate = line_split[0]
    catelink = ""
    sub_cate = line_split[1]
    sub_cate_link = line_split[2]
    ss__cate = line_split[3][:line_split[3].rfind("(")]
    ss__cate_link = line_split[4]

    brand = line_split[5][:line_split[5].rfind("(")]

    title = soup.find("h1", attrs={"class":"productTitle"}).get_text().lower().replace("(", "").replace(")", "")
    colr_set = set(filter(None, title.split()))
    clr = list(clr_list & colr_set)

    if len(clr) == 1:
       colour = clr[0]

    elif len(clr) > 1:
        colour = "multi"

    else:
        colour = " "

        
    price_big_box = soup.find("div", attrs={"class":"offerPrice"})

    sp = ''

    try:
        sp = price_big_box.find("span", attrs={"class":"whole-price"}).get_text()
    except:
        pass

    try:
        mrp = price_big_box.find("span", attrs={"class":"whole-price"}).get_text()

    except:
        mrp = sp


    start = sp.find(".")

    if start != -1:
        sp = "".join(sp.split(".")[-1].replace(",", "").split())

    else:
        sp = "".join(sp.split()[-1].replace(",", "").split())


    start = mrp.find(".")

    if start != -1:
        mrp = "".join(mrp.split(".")[-1].replace(",", "").split())

    else:
        mrp = "".join(mrp.split()[-1].replace(",", "").split())



    pro_image = soup.find("div", attrs={"class":"jqzoom"}).find("img").get("src")


    pro_url = link 

    seller = "junglee"

    meta_title = soup.find("title").get("content")
    meta_disc = soup.find("meta", attrs={"name":"description"}).get("content")

    try:
        desc = soup.find("div", attrs={"class":"productDetailsTable"}).get_text()
    except:
        desc = ' '

    try:
        spec = soup.find("div", attrs={"class":"productDescription"}).get_text()
    except:
        spec = ' '

    dte = time.strftime("%d:%m:%y")

    try:
        size = soup.find("td", text=re.compile("Size")).find_parent("tr").find("td", attrs={"class":"featureValue"}).get_text()
    except:
        size = " "

    status = "A"

    start =   pro_image.rfind("/")
    sort_image_link = pro_image[start+1:]

    cate = cate.lower() 
    sub_cate = sub_cate.lower()
    ss__cate = ss__cate.lower()

    prl = "-".join("".join([c for c in pro_title if c not in special_char]).split()).lower()       


    desc , spec = tuple(map(my_strip, [desc, spec]))

    desc = "  ".join(desc.split())
    spec = "  ".join(spec.split())
   
    info = [sku, pro_title, prl, target_link, sp, cate, sub_cate, ss__cate, ss__cate_link, brand,
            pro_image, sort_image_link, mrp, colour, target,  pro_url, seller, meta_title, meta_disc, 
            str(size), desc, spec, dte, status]


    info2 = map(my_strip, info)

    f2.write(str(info2) + "\n")

    seller_choice  = soup.find("table", attrs={"class":"outdent"})

    slr_prc_list_box = seller_choice.find_all("tbody", attrs={"class":"offer-has-map offer-hidden-map"})

    f3 = f3.write
    try:
        info = [    f3(str(map(my_strip, [sku, 
                                      "http://www.junglee.com%s" %(slr_prc_list.find("div", attrs={"class":"offer-phone-number paymentsEnabled"}).a.get("href")),
                                      filter(None, slr_prc_list.find("a", text=re.compile("Seller Info")).get("href").split("/"))[0], 
                                      slr_prc_list.find("span", attrs={"class":"whole-price"}).get_text()
                                     ])) + "\n")
                for slr_prc_list in slr_prc_list_box
               ]
    except:
        pass

   



def supermain():
    f2 = open("last_info.csv", "w+")
    f3 = open("last_info2.csv", "w+")
    line = """['beauti', 'Makeup & Nails', 'http://www.junglee.com/s/ref=sitedir_6_2_1_1?rh=n:837260031,p_6:A13MD9B2XLIH8A|AKDCPSL9IQAU6|A2BK6A7ZQSZQJG|A299H0VJ7NTYQB|AMG8F0ERJWT88|A2Z051XXI6G268|A3BWQCXRIC95AT|AVPK1RAEYLH4A|A13LM2TDBOZHCB|A1SGXBS8Y6CVIL|A1HO7CPLJR7L5V|A1TLGR9V95HT38|AILXAO8G66Z2D|A10QVIJF0GF2G1|A372MXV8AH4QJM|A3DUHKGDBZ98QR,n:!837261031,n:921073031&bbn=837261031&ie=UTF8&qid=1407222899&rnid=837261031', 'Body Art(217)', 'http://www.junglee.com/s/ref=sr_nr_n_1/276-3762650-8817245?rh=n%3A837260031%2Cp_6%3AA13MD9B2XLIH8A%7CAKDCPSL9IQAU6%7CA2BK6A7ZQSZQJG%7CA299H0VJ7NTYQB%7CAMG8F0ERJWT88%7CA2Z051XXI6G268%7CA3BWQCXRIC95AT%7CAVPK1RAEYLH4A%7CA13LM2TDBOZHCB%7CA1SGXBS8Y6CVIL%7CA1HO7CPLJR7L5V%7CA1TLGR9V95HT38%7CAILXAO8G66Z2D%7CA10QVIJF0GF2G1%7CA372MXV8AH4QJM%7CA3DUHKGDBZ98QR%2Cn%3A%21837261031%2Cn%3A921073031%2Cn%3A921311031&bbn=921073031&ie=UTF8&qid=1411713638&rnid=921073031', 'COVERGIRL', 'http://www.junglee.com/s/ref=sr_nr_p_4_22/276-3762650-8817245?rh=n%3A837260031%2Cp_6%3AA13MD9B2XLIH8A%7CAKDCPSL9IQAU6%7CA2BK6A7ZQSZQJG%7CA299H0VJ7NTYQB%7CAMG8F0ERJWT88%7CA2Z051XXI6G268%7CA3BWQCXRIC95AT%7CAVPK1RAEYLH4A%7CA13LM2TDBOZHCB%7CA1SGXBS8Y6CVIL%7CA1HO7CPLJR7L5V%7CA1TLGR9V95HT38%7CAILXAO8G66Z2D%7CA10QVIJF0GF2G1%7CA372MXV8AH4QJM%7CA3DUHKGDBZ98QR%2Cn%3A%21837261031%2Cn%3A921073031%2Cn%3A921311031%2Cp_4%3ACOVERGIRL&bbn=921311031&ie=UTF8&qid=1411713643&rnid=905182031', 'http://www.junglee.com/Deepika-Padukone-deewani-Celebrity-Replica/dp/B00L7SQK6M/ref=sr_1_1?s=apparel&ie=UTF8&qid=1411717041&sr=1-1']"""
    main(f2, f3,  line)
    f2.close()
    f3.close()


if __name__=="__main__":
    supermain()
    
