from django.shortcuts import render,HttpResponse,redirect
#from django.http import request

# Create your views here.

#import this module for creating verify code
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
import math,string

def index(request):

    return render(request,'login/index.html')

def index_show(request):

    #return render(request,'login/index_show.html')
    return redirect("login/")

#定义验证码
def verify_code(request):
    bgcolor = (random.randrange(20,100),random.randrange(20,100),100)
    width = 100
    height = 25
    #创建画面对象
    im = Image.new('RGB',(width,height),bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0,100):
        xy = (random.randrange(0,width),random.randrange(0,height))
        fill = (random.randrange(0,255),255,random.randrange(0,255))
        draw.point(xy,fill=fill)

    #定义验证码的备选值
    str1 = 'QWERTYUIOPASDFGHJKLZXCVBNM1234567890'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0,4):
        rand_str += str1[random.randrange(0,len(str1))]

    #构造字体对象,centos的字体位置
    font = ImageFont.truetype('static/msyh.ttc',20)
    #构造字体颜色
    fontcolor = (255,random.randrange(0,255),random.randrange(0,255))
    #绘制4个字
    draw.text((5,1),rand_str[0],font=font,fill=fontcolor)
    draw.text((25,2),rand_str[1],font=font,fill=fontcolor)
    draw.text((50,3),rand_str[2],font=font,fill=fontcolor)
    draw.text((75,1),rand_str[3],font=font,fill=fontcolor)

    #释放画笔
    del draw

    #存入session,用于提交表单的时候,验证是否非机器人

    request.session['verifycode'] = rand_str
    #内存文件操作

    #python3里面没有cStingIO,改为IO
    import io
    buf = io.BytesIO()
    #将图片保存在内存中,文件类型为png
    im.save(buf,'png')
    #讲内存中的图片数据返回给客户端,MIME类型为图片png
    return HttpResponse(buf.getvalue(),'image/png')

##验证登录的所有信息
##包括账号密码
def check_login(request):
    
    pass