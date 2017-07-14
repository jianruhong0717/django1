# coding=utf-8
from django.shortcuts import render, redirect
from django.http import JsonResponse
from models import UserInfo
from hashlib import sha1
import datetime
import user_decorators
# Create your views here.


def register(request):
    context = {'title': '注册', 'top': '0'}
    return render(request, 'ttsx_user/register.html', context)


def register_handle(request):
    # 接收用户注册请求
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('user_pwd')
    ucpwd = post.get('user_cpwd')
    uemail = post.get('user_email')


    # 密码加密
    s1 = sha1()
    s1.update(upwd)
    upwd_sha1 = s1.hexdigest()
    # 向数据库中保存数据
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd_sha1
    user.umail = uemail
    user.save()

    # 重定向到登录页面
    return redirect('/gaga/login/')


def register_valid(request):
    # 接收用户名
    uname = request.GET.get('uname')
    # 查询用户名当前的个数
    data = UserInfo.objects.filter(uname=uname).count()
    # 返回json{'valid':1或0}
    context = {'valid': data}
    return JsonResponse(context)


def login(request):
    uname = request.COOKIES.get('uname', '')
    context = {'title': '登录', 'uname': uname, 'top': '0' }
    return render(request, 'ttsx_user/login.html', context)


def login_handle(request):
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    ujz = post.get('user_jz', 0)  # 0表示不用记住用户名

    s1 = sha1()
    s1.update(upwd)
    upwd_sha1 = s1.hexdigest()

    context = {'title': '登录', 'uname': uname, 'upwd': upwd, 'top': 1}

    # 如果没有查到数据则返回[],如果查询到数据返回[UserInfo]
    result = UserInfo.objects.filter(uname=uname)
    if len(result) == 0:
        # 用户名不存在
        context['error_name'] = '用户名错误'
        return render(request, 'ttsx_user/login.html', context)
    else:
        if result[0].upwd == upwd_sha1:

            # 登录成功
            response = redirect('/gaga/')
            request.session['uid'] = result[0].id
            request.session['uname'] = result[0].uname

            # 记住用户名
            if ujz == '1':
                response.set_cookie('uname', uname, expires=datetime.datetime.now() + datetime.timedelta(days=14))
            else:
                response.set_cookie('uname', '', max_age=-1)
            return response
        else:
            # 密码错误
            context['error_pwd'] = '密码错误'
            return render(request, 'ttsx_user/login.html', context)
            # context用来接收登录的数据


def logout(request):
    # 登出功能
    # 清除session
    request.session.flush()
    return redirect('/gaga/login/')


@user_decorators.user_islogin
def center(request):
    user = UserInfo.objects.get(pk=request.session['uid'])
    context = {'user': user}
    return render(request, 'ttsx_user/center.html', context)


@user_decorators.user_islogin
def order(request):
    context = {}
    return render(request, 'ttsx_user/order.html', context)


@user_decorators.user_islogin
def site(request):
    user = UserInfo.objects.get(pk=request.session['uid'])
    if request.method == 'POST':
        post = request.POST
        ushou = post.get('ushou')
        uaddress = post.get('uaddress')
        ucode = post.get('ucode')
        uphone = post.get('uphone')

        user.ushou = ushou
        user.uaddress = uaddress
        user.ucode = ucode
        user.uphone = uphone
        user.save()

    context = {'user': user}
    return render(request, 'ttsx_user/site.html', context)

