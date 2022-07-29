from pyexpat.errors import messages
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render
from .models import User
from .forms import CsRegisterForm
from django.views.generic import CreateView
from django.contrib import auth
from django.contrib.auth.models import User

 
class CsRegisterView(CreateView):
    model = User
    template_name = 'signup.html'
    form_class = CsRegisterForm

    def get(self, request, *args, **kwargs):
        if not request.session.get('agreement', False):
            raise PermissionDenied
        request.session['agreement'] = False
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(self.request, "회원가입 성공.")
        return redirect('users:login')

    def form_valid(self, form):
        self.object = form.save()
        return redirect(self.get_success_url())

def login(request):
    if request.method == "POST":
        user_id = request.POST["user_id"]
        password = request.POST["password"]
        user = auth.authenticate(request, user_id=user_id, password=password)

        if user is not None:
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
        else: 
            #잘못된 로그인
            return render(request, 'home.html')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['student_id']:
            #회원가입
            user = User.objects.create_user(
                user_id=request.POST['user_id'], 
                school=request.POST['school'], 
                major=request.POST['major'], 
                student_id=request.POST['student_id'])
            #로그인
            auth.login(request, user)
            #홈리다이렉션
            return redirect('home')
    else:
        form=CsRegisterForm
        return render(request,'signup.html', {'form':form})