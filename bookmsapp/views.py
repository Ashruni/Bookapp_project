import os

from django.urls import path,reverse_lazy
from django.views import generic
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import*
from django.contrib.auth.models import User
import datetime
from datetime import timedelta
from django.contrib.auth.views import LogoutView


class register(generic.CreateView):
    form_class = regforms
    template_name ='registerpage.html'
    success_url =reverse_lazy('login')

class login(generic.View):
    form_class = logform
    template_name='login.html'
    def get(self,request):
        form= self.form_class
        return render(request,self.template_name,{'form':form})

    #going to give these data
    def post(self,request):
        if request.method == 'POST':  # post should be uppercase(case sensitive )
            a = logform(request.POST)
            if a.is_valid():
                em = a.cleaned_data["username"]
                ps = a.cleaned_data["password"]
                b = User.objects.all()
                for i in b:
                    if em == i.username  and ps == i.password:
                        return HttpResponse('login success')
                else:
                    return HttpResponse("login failed")
            return HttpResponse ("Invalid Credentials")
def showindex(request):
    return render(request,'index.html')
# class upload(generic.CreateView):
#     form_class=uploadform
#     template_name= 'bookupload.html'
#     success_url= reverse_lazy('upload')
#     def get(self,request):
#         a= uploadmodel1.objects.all()
#         # c = datetime.date.today()
#         bname=[]
#         bfile=[]
#         bauthor=[]
#         bdate=[]
#         bimage=[]
#         id1=[]
#         for i in a:
#             id=i.id
#             id1.append(id)
#             bnm=i.bookname
#             bname.append(bnm)
#             bfl=i.bookpdf
#             bfile.append(str(bfl).split('/')[-1])
#             bauth=i.author
#             bdt=i.bookdate
#             bdate.append(bdt)
#             bauthor.append(bauth)
#             bim=i.image
#             bimage.append(str(bim).split('/')[-1])  # split is str fun thats why converted to str
#             # request.session['bdt'] = bdt
#
#
#             # bfile.append(bfl)
#
#         mylist=zip(bname,bauthor,bfile,bimage,bdate,id1)
#         return render(request,self.template_name,{'mylist':mylist})
# class delete(generic.DeleteView):
#     model= uploadmodel1
#     template_name='deletepage.html'
#     success_url= reverse_lazy('upload')
#
#     # bookname
#     # bookpdf
#     # author
#     # bookdate
#     # image
# class update(generic.UpdateView):
#     model = uploadmodel1
#     template_name='updatebook.html'
#     # success_url ='upload'
#     fields = '__all__'
#     form_class = uploadform
#     def get(self,request, **kwargs):
#         id1 = kwargs.get('pk')
#         a = self.model.objects.get(id=id1)
#         bname = a.bookname
#         bauthor = a.author
#         # bdate = a.bookdate
#         bimage = str(a.image).split('/')[-1]
#         bpdf = str(a.bookpdf).split('/')[-1]
#         return render(request,'updatebook.html',{'bname':bname,'bpdf':bpdf,'bauthor':bauthor,'bimage':bimage})
#     def post(self,request,**kwargs):
#         id1 = kwargs.get('pk')
#         a = self.model.objects.get(id=id1)
#         if request.method == 'POST':
#             if len(request.FILES)!=0:
#                 if len(a.image)>0 :
#                     os.remove(a.image.path)
#                 a.image = request.FILES['image']
#                 if len(a.bookpdf)>0:
#                     os.remove(a.bookpdf.path)
#                 a.bookpdf =request.FILES['bookpdf']
#
#             # a.bookdate = request.session['bdt']
#             a.bookname = request.POST.get('bookname')
#             a.author = request.POST.get('author')
#             # a.bookdate = request.POST.get('bookdate')
#             a.save()
#             return redirect('http://127.0.0.1:8000/bookmsapp/upload')
# def profile1(request):
#     return render(request,'profile1.html')


class customlogout(LogoutView):
    next_page =reverse_lazy('index')

class uploaddisplay(generic.CreateView):
    form_class=uploadform
    template_name= 'bookupload.html'
    success_url=reverse_lazy('uploaddisplay')
    def get(self,request):
        a=uploaddisplaym.objects.all()
        bname=[]
        bpdf=[]
        bimage=[]
        bdate=[]
        bauth=[]
        uid=[]
        for i in a:
            id1=i.id
            uid.append(id1)
            bknm=i.bookname
            bname.append(bknm)
            bkpdf=str(i.bookpdf).split('/')[-1]
            bpdf.append(bkpdf)
            bkimg=str(i.bookimage).split('/')[-1]
            bimage.append(bkimg)
            bkdate=i.uploaddate
            bdate.append(bkdate)
            bkauth=i.bookauthor
            bauth.append(bkauth)
        mylist=zip(bname,bpdf,bimage,bdate,bauth,uid)
        return render(request,self.template_name,{'mylist':mylist})

class editbook(generic.UpdateView):
    form_class=uploadform
    template_name='updatebook.html'
    model=uploaddisplaym
    fields='__all__'
    def get(self,request,**kwargs):
        id1= kwargs.get('pk')
        a=self.model.objects.get(id=id1)
        name=a.bookname

        author=a.bookauthor
        pdf=str(a.bookpdf).split('/')[-1]
        image=str(a.bookimage).split('/')[-1]
        return render(request,'updatebook.html',{'name':name,'image':image,'author':author,'pdf':pdf})
    def post(self,request,**kwargs):
        id1=kwargs.get('pk')
        a = self.model.objects.get(id=id1)
        if request.method=='POST':
            if len(request.FILES)!=0:
                if len(a.bookimage)>0:
                    os.remove(a.bookimage.path)
                a.bookimage =request.FILES['bookimage']
                if len(a.bookpdf) > 0:
                    os.remove(a.bookpdf.path)
                a.bookpdf =request.FILES['bookpdf']
            a.bookname=request.POST.get('bookname')
            a.bookauthor=request.POST.get('bookauthor')
            a.save()
            return redirect('http://127.0.0.1:8000/bookmsapp/uploaddisplay')



class delete(generic.DeleteView):
    model= uploaddisplaym
    template_name='deletepage.html'
    success_url= reverse_lazy('uploaddisplay')
class dowloadpage(generic.ListView):
    model=uploaddisplaym
    template_name = 'downloadpage.html'


    def get(self, request):
        bkname=[]
        bkpdf=[]
        a = self.model.objects.all()
        for i in a:
            bookname= i.bookname
            bookpdf =str(i.bookpdf).split('/')[-1]
            bkname.append(bookname)
            bkpdf.append(bookpdf)
        mylist=zip(bkname,bkpdf)

        return render(request, 'downloadpage.html', {'mylist':mylist})

def profile1(request):
    return render(request,'profile1.html')







