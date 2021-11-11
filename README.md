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



0. 整体流程：
    目录文件扫描分类 => SQL注入模块 => XSS攻击模块 => 文件上传模块 => 弱口令爆破模块 => 生成报告
1. 目录文件扫描分类
    1.1 主动扫描策略
        - 整理字典
            目录名字典、文件名字典、文件后缀字典（使用clean.py过滤无效字典项，去重，去异）
        - 渗透扫描
            - 从首页（可能是显式的http(s)://[IP/domain]/index{.ext}或者隐式的http(s)://[IP/domain]/由中间件指定默认首页）开始
            - 抽取页面中所有herf的值，进行简单过滤得到该页面指向的其他目录，递归地请求所有herf指向的地址直到没有新的href加入列表为止（预期得到html/htm/xhtml/js）
            - 检查所有即得html上的<form>标签，抽取action的值得到form的请求连接,抽取name的值获得请求参数，由此构建一个请求URL
            - 检查所有即得html上的<script>标签或独立js代码，尝试从window.location方法中获得js请求的url（至此预期整理得到所有可能存在漏洞的点）
            [!] 此方法存在大量难以解决问题：
                1. 各个网页设计不同，难以找到统一的匹配策略抓取所有存在漏洞的URL
                2. js代码构造复杂，用python难以复刻真实的浏览场景（js中的直接跳转，ajax请求，参数和URL分离）
                3. 若请求中包含token或cookie等其他身份验证机制则可能导致扫描失败
        - 碰撞扫描（类似dirbuster）
            1. 扫描网站根目录存在的路径，对结果进行二次扫描，不断迭代直到没有新路径产生或者达到最大深度
            2. 对所有扫描出的路径中的文件进行扫描得到文件列表
            3. 对所有扫描出的文件的参数进行试验，得到请求参数名（至此预期整理得到所有可能存在漏洞的点）
            [!] 此方法存在的问题：
                1. 时间空间开销极大，时间问题可以考虑使用pyhton多进程、cython等方法进行优化（中型字典约4分钟扫描一次、小型字典约1-2分钟）
                2. **请求过快过多可能导致IP被封禁导致扫描中断**
                3. 网站真实目录名千变万化，该方法可能无法检出
                4. 字典选择极其重要，被污染的字典不仅成本大且不能得到预期结果（进行字典净化）
    1.2 被动扫描策略
        - 打开本地代理服务器，将浏览器连接到代理服务器（python pproxy模块）
        - 在浏览器中访问目标网站并进行操作，包括但不限于登录、点击、上传文件、提交信息等操作
        - pproxy在后台记录用户访问，写入outfile.txt，访问结束后关闭pproxy结束记录
        - 主进程读取outfile.txt抽取请求头和参数，token、cookie、用户名、密码等用于身份认证的必要信息（至此预期整理得到所有可能存在漏洞的点）
        - 将产生过的参数记入参数字典，以备不时之需
        - 将结果分类传入之后的模块，进行漏洞测试
        [!] 此方法存在的问题：
            1. python的http代理比较小众需要学习和尝试
            2. 浏览行为将产生大量无效数据，需要设计合理的过滤筛选策略
            3. 浏览结束行为可能需要用户手动中断代理进程
            4. 有些代码程序等用户可能无法触及（被代理记录），但存在漏洞点
            4. 自动化程度较主动扫描策略稍低
    1.3 主被动结合扫描策略（可能的最优策略）
        - 被动扫描
        - 在临时字典中去除已经扫描到的路径和文件以节省成本
        - 由被动扫描确定的后端编程语言简化文件爆破（主动扫描中可能需要用户自行输入判断的网站后端的语言类型）
        - 将两者的列表整合去重，传给其他模块
        [!] 此方法存在的问题：
            - 实现困难，开发流程长

2. SQL注入模块
    1. 接收URL列表
    2. 打开SQLmap server（python多线程）
    3. 向SQLmap server发送请求，开始对URL的扫描（二次多线程）
    4. 等待SQLmap server完成扫描
    5. 收集各线程的扫描结果并进行整理
    6. 关闭SQLmap server并将扫描结果传入报告生成模块
    [*] 此模块除二次多线外已实现
    [!] 此方法存在的问题：
        - 二次多线程实现困难
3. XSS攻击模块

4. 文件上传模块

5. 弱口令模块

6. 报告生成模块
    1. 传入各模块产生的扫描结果
    2. 统一写入report.txt
    格式如下：

