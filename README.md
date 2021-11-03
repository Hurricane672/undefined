# undefined

## 0. 要求

SQL注入、XSS、文件上传、命令执行、CSSRF和弱口令漏洞扫描中的至少两个，必须包含SQL注入

扫描结果自动生成报告

对其它所有组的网站进行扫描至少检测出一个漏洞，四个以上有加分

尝试对扫描出的漏洞进行修复



爬取页面解析表单寻找攻击点

Payload构造

发送请求、获取响应、判断漏洞是否存在

SQL必含：报错、布尔、时间、联合

XSS：反射、存储

对DVWA、sql-labs等漏洞平台扫描，检测所有漏洞类型，要求每种类型均能扫描出漏洞；对自建网站或其他组的网站扫描，检测所有漏洞类型，至少扫描出一个漏洞

## 1. 几个开源扫描器调研

### 1.1[web_vul_scan](https://github.com/youmengxuefei/web_vul_scan)

web_vul_scan是基于爬虫的多线程web漏洞扫描器

用法如下：

    python run.py --help
    Usage: run.py [options]
    
    Options:
      -h, --help            show this help message and exit
      -d DOMAIN, --domain=DOMAIN
                            Start the domain name
      -t THREAD_NUM, --thread=THREAD_NUM
                            Numbers of threads
      --depth=DEPTH         Crawling dept
      --module=MODULE       vulnerability module(sql,xss,rfi)
      --policy=POLICY       Scan vulnerability when crawling: 0,Scan vulnerability
                            after crawling: 1
      --log=LOGFILE_NAME    save log file

支持多线程，爬虫深度，漏洞模块设置。
目前写好了sql注入，xss，文件包含三个模块。

SQL注入模块：



XSS模块：

```python
def Xss_scan(self):
    XSS_PAYLOAD	= [
        '<script>alert(1);</script>',
        '<script>prompt(1);</script>',
        '<script>confirm(1);</script>',
        '<scr<script>ipt>alert(1)</scr<script>ipt>',
        '<object data="data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTs8L3NjcmlwdD4=">',
        '<svg/onload=prompt(1);>',
        '<marquee/onstart=confirm(1)>/',
        '<body onload=prompt(1);>',
        '<select autofocus onfocus=alert(1)>',
        '<textarea autofocus onfocus=alert(1)>',
        '<keygen autofocus onfocus=alert(1)>',
        '<video><source onerror="javascript:alert(1)">'		
    ]
    for test in XSS_PAYLOAD:
        r = requests.get(url=self.url+urlencode(test),headers=HEADER)
        #if ( 'alert(1)' or 'prompt(1)' or 'confirm(1)' ) in r.text:
        if test in r.text:
            return 1
    return 0
```



>   该项目疑似python2所作若使用需转换为python3，其中多线程机制可以借用， 

以sql XSS为主

首先从sqli-labs入手

## 2. 扫描流程

### 2.0 信息提取

-   服务器中间件
-   服务器系统
-   服务器前端框架（可选）
-   服务器后端语言（php、python、node.js，以php为主）
-   服务器数据库种类和版本（可用sqlmap实现）
-   Linux / Apache / PHP7+ / Mysql5

### 2.1 url爬取

从首页（127.0.0.1或其他url）开始，提取get响应中的下列元素

```
<xxx href="xxx"></xxx> => (?<=href=")[^"]*(?=")
window.location.href = "xxx" => (?<=href= ")[^"]*(?=")
<form action="xxx" >
<script>$.ajax({url:"signin.php",type:"GET",async:false,data:{name:nam,password:passwd},xxx})</script>
```

### 2.2 数据清洗（重中之重）

-   删除url列表中无法正常访问的url
-   将php、html、js分开，检测html中对php的请求参数，保存并准备构建payloads

### 2.3 代入sqlmap

将准备好的url和payload代入SQLmap

## 3. sqli

每个文件对应一个同名的json文件，格式如下

```json
{
    "js":["JS/core.js","JS/query.js"],
    "url":["./add.html","./edit.php","index.html"]
}
```

每个文件的注入参数可能都是id=\*



## DVWA

-   默认账号密码：admin/password
-   默认数据库账号密码：dvwa/root

## Bwapp

-   默认账号密码：bee/bug

## Webug

-   默认账号密码：admin/admin
-   mysql：root/root

