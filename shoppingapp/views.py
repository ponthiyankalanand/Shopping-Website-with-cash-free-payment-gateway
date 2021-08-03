from django.shortcuts import render, redirect
from .models import product, user, shoppingdetails ,reviewdetails
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.template import RequestContext
import datetime
import hashlib
import hmac
import base64
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def timehash(val):
	x = datetime.datetime.now()
	z= val
	y= (x.strftime("%f"))
	h=hash(y)
	return(h)
def home(request):
	pvalue = product.objects.all()
	return render(request, 'index.html',{'pvalue': pvalue})
def adminpage(request):
	return render(request, 'uploadfiles.html')

def Contact(request):
	return render(request, 'contact.html')
def userMessage(request):
	try:
		if request.method == 'POST':
			uname = request.POST['name']
			uemail = request.POST['email']
			usubject = request.POST['subject']
			umessage = request.POST['message']
			userMessage = user(uname=uname, umail=uemail, usubject=usubject, umessage=umessage)
			userMessage.save()
			res = not userMessage
			if res != True:
				return render(request,'return.html',{'obj': 'Thank you for your response !😍'})
			else:
				return render(request,'return.html',{'obj': 'Try again.😕'})
	except:
		return render(request, '404.html',)


def login(request):
	try:
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']
			user = auth.authenticate(username=username, password=password)
			res = not user
			if res != True:
				auth.login(request, user)
				return render(request,'uploadfiles.html')
			else:
				messages.info(request,'Invalid Credentials')
				return render(request,'login.html')
		else:
			return render(request,'login.html')
	except:
		return render(request, '404.html',)
def upload(request):
	try:	
		if request.method == 'POST':
			pname = request.POST['ProductName']
			pabout = request.POST['about']
			pdesc = request.POST['desc']
			pcount = request.POST['count']
			pprice = request.POST['price']
			pimg1 = request.POST['image1']
			pimg2 = request.POST['image2']
			pimg3 = request.POST['image3']
			poffer = request.POST['offer']
			paylink = request.POST['paylink']
			code = request.POST['code']
			Product = product(code=code, pname=pname, pdisc=pdesc, pabout=pabout, pprice=pprice, pimg1=pimg1, pimg2=pimg2, pimg3=pimg3, count=pcount, paylink=paylink, poffer=poffer)
			Product.save()
			res = not Product
			if res != True:
				messages.info(request,'Success')
				return render(request,'uploadfiles.html')
			else:
				messages.info(request,'Failed in DB')
				return render(request,'uploadfiles.html')
		else:
			messages.info(request,'upload fail')
			return redirect(request,'adminpage')
	except:
		return render(request, '404.html',)
def logout(request):
	auth.logout(request)
	return render(request,'login.html')
def search(request):
	try:
		key = request.POST['key']
		obj = product.objects.filter(pname__icontains=key)
		res = not obj
		if res != True:
			return render(request, 'uploadfiles.html',{'obj': obj})
		else:
			return render(request, 'uploadfiles.html')
	except:
		return render(request, '404.html',)

def updatestatus(request):
	try:
		key = request.POST['key']
		temp = product.objects.get(id=key)
		tempval=temp.status
		if tempval == 1:
			val='False'
		else:
			val='True'
		obj = product.objects.filter(id=key).update(status=val)
		res = not obj
		if res != True:
			messages.info(request,'status changed')
			return render(request, 'uploadfiles.html',)
		else:
			messages.info(request,'status change failed')
			return render(request, 'uploadfiles.html')
	except:
		return render(request, '404.html',)
def getproduct(request):
	pid = request.POST['key']
	print(pid)
	obj1 = product.objects.filter(id=pid).count()
	print(obj1)
	if obj1 != 0 :		
		obj = product.objects.get(id=pid)
		return render(request, 'index-product.html',{'obj': obj})
	else:
		return render(request, 'return.html',{'obj': 'Nothing left.👀'})
 

def honmesearch(request):
	try:
		key = request.POST['key']
		obj = product.objects.filter(pname__icontains=key)
		res = not obj
		if res != True:
			return render(request, 'index_gallery.html',{'pvalue': obj})
		else:
			return render(request, 'return.html',{'obj': 'Nothing left.👀'})
	except:
		return render(request, '404.html',)
def reviewupload(request):
	customercode = request.POST['code']
	customermessage =  request.POST['message']
	customername =  request.POST['name']
	key = shoppingdetails.objects.filter(code__icontains=customercode)
	res = not key
	if res != True:
		mesg = reviewdetails(customercode=customercode ,customername=customername ,customermessage=customermessage)
		mesg.save()
		return render(request,'return.html',{'obj': 'Thank you for your response !😍'})
	else:
		return render(request,'return.html',{'obj': 'Check your order ID, Try again 🤔'})
def gallery(request):
	pvalue = product.objects.all()
	return render(request, 'index_gallery.html',{'pvalue':pvalue})
def ordervalidate(orderDetails):
	obj = product.objects.get(code=orderDetails["pid"])
	qun=int(orderDetails["qun"])
	count=int(obj.count)
	if (0 < qun <= count):
		print("proceed")
	else:
		print("not proceed")
 

def vieworderdetails(request):
	if request.method == 'POST': 
		uname =  request.POST['name']
		uHname =  request.POST['Hname']
		uemail =  request.POST['email']
		umob =  request.POST['mob']
		upostoffice = request.POST['Postoffice']
		ulandmark =  request.POST['Landmark']
		upin =  request.POST['pin']
		ucity =  request.POST['City']
		udistrict =  request.POST['district']
		ustate =  request.POST['state']
		ucountry =  request.POST['country']
		qu =  request.POST['qun']
		pid =  request.POST['id']
		quantity = qu
		orderval = {"pid":pid,"name": uname,"qun": quantity,"houseName": uHname,"email": uemail,"mob": umob,"post": upostoffice,"land": ulandmark,"pin": upin,"city": ucity,"dist": udistrict,"state": ustate,"country": ucountry}
		print(pid)
		ordervalidate(orderval)
		obj = product.objects.get(code=pid)
		price=obj.pprice
		pname=obj.pname
		code=timehash(uname)
		res = not price
		if res != True:
			if int(qu) < 1:
				quantity = 1
			else:
				price = float(quantity) * obj.pprice 
		orderDetails = {"pname": pname,"name": uname,"qun": quantity,"houseName": uHname,"email": uemail,"mob": umob,"post": upostoffice,"land": ulandmark,"pin": upin,"city": ucity,"dist": udistrict,"state": ustate,"country": ucountry,"price": price,"code":code }
		user = shoppingdetails(code=code, price=price, uname=uname, uHname=uHname, uemail=uemail, umob=umob, upostoffice=upostoffice, ulandmark=ulandmark, upin=upin, ucity=ucity, udistrict=udistrict, ustate=ustate, ucountry=ucountry, quantity=quantity, pid=pid)
		user.save()
		return render(request, 'index_details.html', {'obj':orderDetails})
	else:
		return render(request, '404.html',)

def orderDetails(request):
	return render(request, 'adminOrderDetails.html',)

#adjusting counter value after purchase	
def counter(pid):
	obj1 = shoppingdetails.objects.filter(code=pid).count()
	if obj1 != 0 :		
		obj = shoppingdetails.objects.get(code=pid)
		pid = obj.pid
		pdetails = product.objects.get(code=pid)
		count = pdetails.count
		if count > 0:
			count = count-obj.quantity
			product.objects.filter(code=pid).update(count=count)

#cash free API Gate Way
def getpaymentdetails(orderid):
	key = orderid
	returnUrl = "http://127.0.0.1:8000/return"
	notifyUrl = "http://127.0.0.1:8000/notify.html"
	appId = "putyourappid"
	
	obj = shoppingdetails.objects.get(code=key)
	res = not obj
	if res != True:
		orderId=str(obj.code)
		orderAmount=str(obj.price)
		customerName=str(obj.uname)
		customerPhone=str(obj.umob)
		customerEmail=str(obj.uemail)
		postData ={		
		"appId":appId,		 
		"orderId":orderId, 
		"orderAmount":orderAmount, 
		"customerName":customerName, 
		"customerPhone":customerPhone, 
		"customerEmail":customerEmail,
		"notifyUrl":notifyUrl,
		"returnUrl":returnUrl
		}
		signature = generatesignature(postData)
		orderDetail ={"appId":appId,"orderId":orderId,"orderAmount":orderAmount,"customerName":customerName,"customerPhone":customerPhone,"customerEmail":customerEmail,"returnUrl":returnUrl,"notifyUrl":notifyUrl,"signature":signature}
	else:
		return render(request, '404.html',)
	return(orderDetail)
def generatesignature(postData):
	sortedKeys = sorted(postData)
	signatureData = ''
	secretKey=""
	for key in sortedKeys:
  		signatureData += key+postData[key];
	message = bytes((signatureData).encode('utf-8'))
	#get secret key from your config
	secret = bytes((secretKey).encode('utf-8'))
	signature = base64.b64encode(hmac.new(secret, message,digestmod=hashlib.sha256).digest())
	signature=signature.decode('utf-8')
	return(signature)

def checkout(request):
	if request.method == 'POST': 
		orderid =  request.POST['code']
		orderdetails = getpaymentdetails(orderid)
		print (orderdetails)
		return render(request, 'submitPay.html',{'obj': orderdetails}) 
	
#retun cashfree
@csrf_exempt 
def notify_url_process(request):
	postData = {
	"orderId" : request.POST['orderId'], 
	"orderAmount" : request.POST['orderAmount'], 
	"referenceId" : request.POST['referenceId'],
	"txStatus" : request.POST['txStatus'], 
  	"paymentMode" : request.POST['paymentMode'], 
  	"txMsg" : request.POST['txMsg'], 
	"txTime" : request.POST['txTime'], 
	"signature": request.POST['signature']
	}
	print (postData)
	signatureData = postData["orderId"] + postData["orderAmount"] + postData["referenceId"] + postData["txStatus"] + postData["paymentMode"] + postData["txMsg"] + postData["txTime"]

	message = bytes((signatureData).encode('utf-8'))
	 #get secret key from your config
	secretKey=""
	secret = bytes((secretKey).encode('utf-8'))
	signature = base64.b64encode(hmac.new(secret,message,digestmod=hashlib.sha256).digest())
	signature=signature.decode('utf-8')
	print(signature,postData["txStatus"])
	if signature == postData["signature"]:
		if postData["txStatus"]=="SUCCESS":
			counter(postData["orderId"])			
			return render(request, 'return.html',{'obj': 'Your order has been Successfuly palced !😍'})
		else:
			return render(request, 'return.html',{'obj': 'Sorry we cannot place your Order. Try again.😟'})
	else:
		return render(request, 'return.html',{'obj':'Error😟'})


 





		 


 