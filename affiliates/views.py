from django.http import HttpResponse
from django.shortcuts import render
from .models import ProductLinks
from bs4 import BeautifulSoup
import requests
from django.contrib import messages

# Create your views here.
def links(request):
    links=ProductLinks.objects.all()
    n=len(links)
    params={'products':links}
    return render(request,'links.html',params)

def add_page(request):
    return render(request,'affiliate.html')

def add_link(request):
    if request.method=="POST":
        htmlurl=request.POST['link']
        webapp=request.POST['website']
        inflname=request.POST['inflname']
        HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) Chrome/44.0.2403.157 Safari/537.36',
                            'Accept-Language': 'en-US, en;q=0.5'})
        webpage = requests.get(htmlurl, headers=HEADERS)
        soup = BeautifulSoup(webpage.content, "lxml")
        title_text=""
        price=""
        imagelink=""
        merchant_name=""

        if webapp=="FLIPKART":
            titles=soup.find('span',class_="B_NuCI")
            title_text=titles.contents[0]
            print(title_text)
            price=soup.find('div',class_="_30jeq3 _16Jk6d").contents[0]
            print(price)
            try:
                imglink=soup.find('img',class_="_396cs4 _2amPTt _3qGmMb _3exPp9")
                imagelink=imglink.get('src')
            except:
                None
            print(imglink)
            merchant=soup.find('div',id="sellerName")
            merchant_name=merchant.contents[0].contents[0].contents[0]
            print(merchant_name)
        elif webapp=="AMAZON":
            titles=soup.find(id="productTitle")
            title_text=titles.string
            price="₹"+soup.find('span',class_="a-price-whole").contents[0]
            imglink=soup.find('div',id="imgTagWrapperId")
            imagelink=imglink.find('img').get('src')
            try:
                merchant=soup.find('div',id="merchant-info")
                merchant_name=merchant.contents[2].contents[0].contents[0]
            except:
                merchant_name="Amazon"
        else:
            return HttpResponse("Can,t Add Link.\n Currently In Development Phase")
        newlink=ProductLinks(product_name=title_text,price=price,website=webapp,product_seller=merchant_name,image=imagelink,influencer=inflname,affiliate_link=htmlurl)
        newlink.save()
        messages.success(request,"Link Added Successfully")
        return render(request,'homepage.html')

def search(request):
    stext=request.GET['stext']
    products=ProductLinks.objects.all()
    prods=[]
    for product in products:
        if stext.upper() in product.product_name.upper() or stext in product.influencer.upper() or stext in product.product_seller.upper():
            prods.append(product)
    return render(request,'links.html',{'products':prods})