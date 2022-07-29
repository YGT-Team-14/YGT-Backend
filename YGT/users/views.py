from pyexpat.errors import messages
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render
from .models import User
from .forms import CsRegisterForm
from django.views.generic import CreateView 

 
class CsRegisterView(CreateView):
    model = User
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
    return render(request,'login.html')