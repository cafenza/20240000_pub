from django.contrib.auth import authenticate, login#검증과 로그인
from django.shortcuts import render, redirect
from .forms import UserForm
# Create your views here.
def main(request):

    return render(request, 'member/main.html') #member의 밑의 main.html로 들어감

def signup(request):#signup함수를 만들어줌
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/member/main')
    else:
            form = UserForm()
    return render(request, 'member/signup.html', {'form':form})#signup에 보냄