# asset_cms
asset_cms powered by python3.6_django

#### 1.首先肯定先使用git更新代码,项目是在python用户家目录下面的asset_estimate(git pull更新到最新)
#### 2.首先定义好数据库里面的FrontEndShow里面的一条数据.用于定义展示给学生的ip地址
#### 3.然后记得去修改PortType的端口,前提是如果冲突的话,如果不冲突可以不用管.
#### 4.手动去定义nginx配置位置,就是/etc/nginx/nginx.conf,定义好端口和ip,注意了,ip必须和上面第一个一一对应.不然就出错了.
#### 5.还有去修改好/home/python/www/html里面的index.html一些网址,也是改成对应好第2,4一样定义的ip地址.
#### 6.由于python无法使用低于1000端口的问题,所以,要么在nginx,要么在apache启动多一个服务,设置一个页面去跳转到x.x.x.x:8000
####   我自己建议是使用nginx,然后我放了一个文件在/home/python/asset_estimate/nginx_html/index.html,修改一下指定要跳转的页面就可以了.
#### 7.最后是启动项目,先cd到asset_estimate里面,然后直接python mange.py runserver x.x.x.x:8000,注意,前面的ip也是和前面的2,4,5一样的ip地址.
#### 8.暂时没有想到其他了.!
