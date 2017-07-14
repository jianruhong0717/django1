# coding=utf-8

from django.shortcuts import redirect


def user_islogin(func):
    def func1(request, *args, **kwargs):
        # 判断是否登录
        if request.session.has_key('uid'):
            # 如果登录 执行func函数
            return func(request, *args, **kwargs)
        # 如果不登录 转到login视图/gaga/login/
        else:
            return redirect('/gaga/login/')

    return func1