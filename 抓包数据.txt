HTTP header
POST /uploads/jianshi HTTP/1.1 
Content-Type: application/x-www-form-urlencoded 
Content-Length: 65 
Host: 60.205.216.178:8080 
Connection: Keep-Alive 
Accept-Encoding: gzip 
User-Agent: okhttp/3.3.1 



POST http://sdk.cferw.com/api.php?z=3286&appkey=528ab6a566564a96a0b7646586f3c017&deviceId=863970024695496&sw=1080&sh=1920&osver=17
使用丄一步返回的count_url
POST http://api.cferw.com/reapi.php?s=Nzg4NDM0fDUxNHwzMjg2fDd8NDMzfDM0MHwxLjE5OS4yMDguMTE=;28778262f3ed79f69db62a876b61db11;1&getImageTJ=1507775529&key=528ab6a566564a96a0b7646586f3c017&ref=863970024695496&lrdst=0473762c90338331f77d86eb73811de8085b1b5bf27e5ab485b2a48758ba9fe7

POST http://60.205.216.178:8080/bulletins/bulletin
GET http://60.205.216.178:8080/focuss/focus
GET http://60.205.216.178:8080/version/version
POST http://60.205.216.178:8080/PromptController/queryPrompt

获取任务列表
POST http://60.205.216.178:8080/tasks/task

点击任务
POST http://60.205.216.178:8080/uploads/jianshi
taskname=天天快报&username=ZZR152011
任务未做过
{"code":"200","jianshi":0,"message":"可以做此任务！"}
做过下载未做分享
{"code":"200","jianshi":1,"message":"做过下载，可以做一下分享！"}
做过分享未做下载
{"code":"200","jianshi":2,"message":"做过分享，可以做一下下载！"}
当前任务已完成
{"code":"200","jianshi":3,"message":"所有任务都做了！"}
试玩任务完成
POST http://60.205.216.178:8080/uploads/fenxiang
money=0.8&username=ZZR152011&yuliu2=3&taskname=新郎微博2&taskid=312
分享任务完成
money=0.3&username=ZZR153514&yuliu2=2&taskname=新郎微博2&taskid=330
====================抓包数据======================
POST http://60.205.216.178:8080/uploads/fenxiang HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 94
Host: 60.205.216.178:8080
Connection: Keep-Alive
Accept-Encoding: gzip
User-Agent: okhttp/3.3.1

money=0.4&username=ZZR152011&yuliu2=3&taskname=%E5%A4%A9%E5%A4%A9%E5%BF%AB%E6%8A%A5&taskid=161
---------------------自己数据----------------------
POST http://60.205.216.178:8080/uploads/fenxiang HTTP/1.1
Accept-Encoding: identity
Content-Type: application/x-www-form-urlencoded
Content-Length: 94
Host: 60.205.216.178:8080
User-Agent: Python-urllib/3.6
Connection: close

money=0.4&username=ZZR152011&yuliu2=2&taskname=%E5%A4%A9%E5%A4%A9%E5%BF%AB%E6%8A%A5&taskid=161
==========================================

完成后返回数据包
{"code":"200","jianshi":2,"message":"做过分享，可以做一下下载！"}
{"code":"200"}
完成后发送到服务器查询包
POST http://60.205.216.178:8080/uploads/jianshi
taskname=天天快报&username=ZZR152011