![python version](https://img.shields.io/badge/python-3.5+-blue)
![demo version](https://img.shields.io/github/v/tag/GentleCP/cptools?color=orange)
![license](https://img.shields.io/github/license/GentleCP/cptools)
# cptools
我个人写代码过程觉得有用的小工具函数合集，目前包含：
- progress:下载进度条
- notify:各种通知工具，如`ServerChan`,`DingDing`,`Email`
- logger:日志打印与存储器

## Usage
```text
pip install -U cptools
```
### progress
- download_file(url, session, file_path, overwrite)   
    文件下载进度条，requests库的get方法默认是没有进度条的，使用该函数能够弥补这一点，效果如下图
    ![](img/download-file.png)

### notify
- ServerChan
```python
from cptools.notify import ServerChan
SJ = ServerChan()
SJ.token='your ServerChan token'  # your ServerChan token
SJ.send_text(text='This is a test.')

# or you can do this
SJ = ServerChan(token='your ServerChan token')  
SJ.send_text(text='This is a test.')
```
- DingDing
```python
from cptools.notify import DingDing
dd = DingDing()
dd.token='your DingDing assess_token'  
dd.send_text(text='[key word]This is a test.')  # your test should include the key word that you specify 

# or you can do this
dd = DingDing(token='your DingDing assess_token' )
dd.send_text(text='[key word]This is a test.')  # your test should include the key word that you specify 
```
- Email
```python
from cptools.notify import EmailSender
email = EmailSender(user='xx@qq.com',  
                    password_or_auth_code='auth code',  # depending on your email vendor
                    host='smtp.xx.com')  # you should use smtp serve
email.send_text(text='test', contents='this is a test mail', to=['xx@qq.com',])
```

- mac_notify  

```
from cptools.notify import mac_notify
mac_notify(title='Warning', text='This is a test')
```

result is something like this:

![image-20210120115105651](https://gitee.com/gentlecp/ImgUrl/raw/master/20210120115105.png)


### logger
- default LogHandler
```python
from cptools.logger import LogHandler

log = LogHandler('test')
log.info('this is a test msg')  # 2021-01-30 14:35:48,639 logger.py-[line:130] 【INFO】 this is a test msg
```

- LogHandler with different configuration
    - `name`: The name of LogHandler
    - `level`: Log level, default `INFO`
    - `steam`: If True, show log in terminal, default True
    - `file`: If True, save log to local file, defalut True
    - `log_path`: Where to save log, default `../log/`
    
```python
from cptools.logger import LogHandler

CRITICAL = 50
log = LogHandler(name='test',
                 level=CRITICAL,  # note that the level is a integer number
                 log_path='log/')
log.info("The level is critical, info message will not display!")
log.critical("Critical message will show!")
```
