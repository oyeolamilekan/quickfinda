from django.db.models import Q
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from findit.models import Feedback,Products
from .models import Sub
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                    
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def stream(request):
    query = request.GET.get('q')
    user_sub_list = []
    user = User.objects.get(username=request.user)
    sub = Sub.objects.filter(user=request.user).exists()
    sub_list = Sub.objects.filter(user=user)
    for subb in sub_list:
        user_sub_list.append(subb.lisert)
    if sub:
        all_products = Products.objects.order_by('?').filter(genre__in=[subb.lisert for subb in sub_list])[:20]
    else:
        all_products = Products.objects.order_by('?')[:20]
    if query:
        all_products = Products.objects.all()
        query = query.strip()
        all_products = all_products.filter(
                   Q(name__icontains=query)|
                   Q(name__iexact=query)|
                   Q(price__icontains=query)|
                   Q(price__iexact=query)
        ).distinct()
    context = {'products':all_products,'sub_list':user_sub_list}
    return render(request,'accounts/stream.html',context)

def subscribe(request):
    sub = request.GET.get('sub')
    if Sub.objects.filter(lisert=sub).exists():
        Sub.objects.filter(lisert=sub).delete()
        print('hi')
    else:
        sub = Sub.objects.create(user=request.user,lisert=sub)
        sub.save()
    return HttpResponse('ok')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            authenticated_user = authenticate(username=new_user.username,password=request.POST['password'])
            login(request,authenticated_user)
            #create_action(request.user,'just signed up')
            # Create the user profile
            # profile = Profile.objects.create(user=new_user)
            return redirect('/adengine/index/')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})
