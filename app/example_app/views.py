from django.shortcuts import render,redirect,HttpResponse
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from bi_servers.models import CategoryModels, SubCategoryModels
# Create your views here.
def logout_view(request):
    
    logout(request)
    return redirect("html/login.html")
class LoginView(View):
    def get(self,request):            
        return render(request, "html/login.html")
    def post(self,request):
        users_datas = User.objects.filter().all().values() 
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request=request,username=username, password=password)
            if user is not None:
                login(request,user)
                
                
                return redirect("home-page")
                
            else:
                messages.error(request, message="Username or password is mismatch")    
                
                return render(request, "html/login.html")

class HomeView(View):
    def get(self,request):
        categorys = CategoryModels.objects.filter().values()
        subcategorys = SubCategoryModels.objects.filter(Active=True).values()
        
        for i in  categorys:
            for n  in subcategorys:
                if i["id"] == n["category_id"]:
                    n
      
        
        return render(request, 'html/home.html',context={"subcategorys": subcategorys, "categorys": categorys})
    def post(self,request):
        return render(request, 'html/home.html')
    

