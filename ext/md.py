from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect

class MyMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path_info=="/users/login/":
            return
        if request.path_info=="/home/":
            return
        if request.path_info=="/users/signup/":
            return

        #获取user_session
        user_session = request.session.get('user_session')
        if user_session:
            request.user_session = user_session
            return
        #将user_session 赋值给request，方便以后使用

        return redirect("/users/login/")

