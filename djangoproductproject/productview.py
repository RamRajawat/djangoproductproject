from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from . import pool
import os

def ProductInterface(request):
    return render(request,"ProductInterface.html")

def FetchAllProductTypes(request):
  try:  
    DB,SMT=pool.OpenConnection()
    SMT.execute("select * from producttype")
    records=SMT.fetchall()
    print(records)
    return JsonResponse(records,safe=False)
  except Exception as e:
    print(e)
    return JsonResponse([],safe=False) 
def FetchAllProductItems(request):
  try:  
    DB,SMT=pool.OpenConnection()
    SMT.execute("select * from productitem where producttypeid={0}".format(request.GET['producttypeid']))
    records=SMT.fetchall()
    print(records)
    return JsonResponse(records,safe=False)
  except Exception as e:
    print(e)
    return JsonResponse([],safe=False) 
def ProductSubmit(request):
 try:  
   if request.method == 'POST': 
    DB,SMT=pool.OpenConnection()
    producttypeid=request.POST['producttypeid']
    productitemid=request.POST['productitemid']
    productstatus=request.POST['productstatus']
    description=request.POST['description']
    price=request.POST['price']
    offer=request.POST['offer']
    picture=request.FILES['picture']

    q="insert into productlist(producttypeid, productitemid, productstatus, description, price, offer, picture)values({0},{1},'{2}','{3}',{4},{5},'{6}')".format(producttypeid,productitemid,productstatus,description,price,offer,picture.name)
    SMT.execute(q)
    F=open("d:/djangoproductproject/assets/"+picture.name,"wb")
    for chunck in picture.chunks():
      F.write(chunck)
    F.close()  

    DB.commit() 
    
   return render(request,"ProductInterface.html",{'status':True,'message':"Record Submitted"})
 except Exception as e:
   print(e)
   return render(request,"ProductInterface.html",{'status':False,'message':"Server Error"})
 
def FetchAllProducts(request):
  try:  
    DB,SMT=pool.OpenConnection()
    SMT.execute("select PL.*,(select PT.producttype from producttype PT where PT.producttypeid=PL.producttypeid) as producttype,(select PI.productitem from productitem PI where PI.productitemid=PL.productitemid) as product from productlist PL") 
    records=SMT.fetchall()
    print(records)
    return render(request,"DisplayAllProducts.html",{'data':records})
  except Exception as e:
    print(e)
    return render(request,"DisplayAllProducts.html",{'data':[]})

def DisplayById(request):
  try:  
    productid=request.GET['productid']
    DB,SMT=pool.OpenConnection()
    SMT.execute("select PL.*,(select PT.producttype from producttype PT where PT.producttypeid=PL.producttypeid) as producttype,(select PI.productitem from productitem PI where PI.productitemid=PL.productitemid) as product from productlist PL where productlistid={0}".format(productid))
    records=SMT.fetchone()
    if(records):
      status=False
      print("xxxxxxxxxxxxxxxxxxxxxxxxxxxx",records)
      if(records['productstatus']=="Delivered"):
        status=True
      else:
        status=False
          

      return render(request,"DisplayById.html",{'data':records,'status':status})
    else:
     return render(request,"DisplayById.html",{'data':[]}) 

  except Exception as e:
    print(e)
    return render(request,"DisplayById.html",{'data':[]})

def Edit_Product_Data(request):
 try:  
  if request.method == 'POST': 
   DB,SMT=pool.OpenConnection()
   if(request.POST['btn']=='Edit'):
    productlistid=request.POST['productlistid']
    producttypeid=request.POST['producttypeid']
    productitemid=request.POST['productitemid']
    productstatus=request.POST['productstatus']
    description=request.POST['description']
    price=request.POST['price']
    offer=request.POST['offer']
    

    q="update productlist set producttypeid={0},productitemid={1},productstatus='{2}', description='{3}', price={4}, offer={5} where productlistid={6}".format(producttypeid,productitemid,productstatus,description,price,offer,productlistid)
    SMT.execute(q)
   
    DB.commit() 
   else:
    productlistid=request.POST['productlistid']
    q="delete from productlist where productlistid={0}".format(productlistid)
    SMT.execute(q)
   
    DB.commit() 
      
       
   return redirect('/fetchallproducts')
 except Exception as e:
      print(e)
      return redirect('/fetchallproducts')


def DisplayPicture(request):
  print("request",dict(request.GET))
  return render(request,"DisplayPicture.html",{'data':dict(request.GET)})  
    
def Edit_Picture(request):
 try:  
   if request.method == 'POST': 
    DB,SMT=pool.OpenConnection()
    productid=request.POST['productid']
    picture=request.FILES['picture']
    oldfile=request.POST['oldfile']

    q="update productlist set picture='{0}' where productlistid={1}".format(picture.name,productid)
    SMT.execute(q)
    F=open("d:/djangoproductproject/assets/"+picture.name,"wb")
    for chunck in picture.chunks():
      F.write(chunck)
    F.close()  
    os.remove('d:/djangoproductproject/assets/{0}'.format(oldfile))
    DB.commit() 
    return redirect('/fetchallproducts')

 except Exception as e:
    return redirect('/fetchallproducts')

 


