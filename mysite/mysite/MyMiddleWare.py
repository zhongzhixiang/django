from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

black_ip_list = ["172.16.15.109"]
class MyMiddleware(MiddlewareMixin):
    def process_request(self,request):
        print("执行了MyMiddleware中的process_request方法")
        ip = request.META.get("REMOTE_ADDR")
        print(ip)
        if ip in black_ip_list:
            return HttpResponse("<h1>你的ip被限制了</h1>")

