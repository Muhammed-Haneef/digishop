from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import render, redirect
from digiadminapp.models import categorydb,productdb
from digiuserapp.models import Userlogdb,cartdb,checkoutDb

# Create your views here.
def home_pg(req):
    data=categorydb.objects.all()
    return render(req,"Home.html",{'data':data})
def about_us(req):
    return render(req,"About.html")
def prod_pg(req,cat_name):
    prod=productdb.objects.filter(Category=cat_name)
    return render(req,"product.html",{'prod':prod})
def contact_us(req):
    return render(req,"Contact.html")
def single_pg(req,singleid):
    pro_single=productdb.objects.get(id=singleid)
    data=productdb.objects.all()
    return render(req,"Single_product_pg.html",{'pro_single':pro_single,'data':data})
def cart_pg(req):
    cartdata=cartdb.objects.filter(User_Name=req.session['User_Name'])
    return render(req,"cart.html",{'cartdata':cartdata})

def log_pg(req):
    return render(req,"reg_log.html")

def add_user(req):
    if req.method=="POST":
        na=req.POST.get('uname')
        em=req.POST.get('email')
        mbl=req.POST.get('mobile')
        pwd=req.POST.get('password')
        img=req.FILES['image']
        obj=Userlogdb(User_Name=na,Email=em,Mobile_Number=mbl,Password=pwd,Image=img)
        obj.save()
        return redirect(log_pg)

def user_login(req):
    if req.method=="POST":
        na=req.POST.get('usname')
        pwd=req.POST.get('passd')
        if Userlogdb.objects.filter(User_Name=na,Password=pwd).exists():
            req.session['User_Name']=na
            req.session['Password']=pwd
            return redirect(home_pg)
        else:
            return redirect(log_pg)
    else:
        return redirect(log_pg)


def del_user(req):
    del req.session['User_Name']
    del req.session['Password']
    return redirect(log_pg)

def cart_save(req):
    if req.method=="POST":
        un=req.POST.get('uname')
        pn=req.POST.get('pname')
        des=req.POST.get('pdescript')
        qn=req.POST.get('quantity')
        pr=req.POST.get('pprice')
        tp=req.POST.get('tprice')
        obj=cartdb(User_Name=un,Product_Name=pn,Description=des, Quantity=qn,Price=pr,Total_price=tp)
        obj.save()
        messages.success(req, "ADDED TO CART SUCCESSFULLY")
        return redirect(cart_pg)

def cartdlt(req,dataid):
    data = cartdb.objects.filter(id=dataid)
    data.delete()
    return redirect(cart_pg)


def checkout_pg(req):
    return render(req,"checkout.html")

def order_page(req):
    if req.method=="POST":
        fn=req.POST.get('fname')
        ln=req.POST.get('lname')
        un=req.POST.get('uname')
        em=req.POST.get('email')
        add1=req.POST.get('addrs')
        add2=req.POST.get('addrs2')
        cntr=req.POST.get('cntry')
        state=req.POST.get('state')
        zp=req.POST.get('zip')
        payment1=req.POST.get('paymentMethod')
        noc=req.POST.get('cname')
        ccn=req.POST.get('cnumber')
        exp=req.POST.get('cdate')
        cv=req.POST.get('cvv')
        obj1=checkoutDb(First_name=fn,Last_name=ln,User_name=un,Email=em,Address1=add1,Address2=add2,Country=cntr,
                        State=state,Zip=zp,payment=payment1,Name_on_card=noc,credit_card_number=ccn, Expire_date=exp,
                        Cvv=cv)
        obj1.save()
        messages.success(req,"ORDER PLACED SUCCESSFULLY")
        return redirect(home_pg)










