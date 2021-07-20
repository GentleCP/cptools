![python version](https://img.shields.io/badge/python-3.5+-blue)
![pypi version](https://img.shields.io/pypi/v/cptools?color=orange&style=plastic)
![license](https://img.shields.io/github/license/GentleCP/cptools)
# cptools
`cptools`is a tool repository which is used to save the useful python code when  I learned python. 
Please feel free to use them. If it is useful for you, give a star for this repository and let more people to know about it, thanks a lot.

Now, it includes:
- progress: to show progress bar when waiting for the running program
- notify: notify yourself when your program has done something right or wrong
- logger: make log print easier
- function: record useful code which is frequently used

> try to type the following code and see what will happen.
```python
from cptools import hello

hello()
```

# Usage
```text
pip install -U cptools
```
## progress
- download_file(url, session, file_path, overwrite):download file with a progress bar.
![](https://gitee.com/gentlecp/ImgUrl/raw/master/20210324085156.png)
  
```python
from cptools.progress import download_file
# from cptools import download_file  # both will work

download_url = "https://dl.360safe.com/360/inst.exe"
if download_file(download_url,file_path='360.exe', overwrite=True):
    print('download success')
```

## notify
- ServerChan: notify yourself on your wechat with [ServerChan](http://sc.ftqq.com/?c=code)
  - old version: will offline soon, know more things by click [here](http://sc.ftqq.com/?c=code)
  ```python
  from cptools.notify import ServerChan
  # from cptools import ServerChan  # both will work
  
  SJ = ServerChan()
  SJ.token='your ServerChan token'  # your ServerChan token
  SJ.send_text(text='This is a test.', desp='This is description.')
  
  # or you can do this
  SJ = ServerChan(token='your ServerChan token')  
  SJ.send_text(text='This is a test.', desp='This is description.')
  ```
  - new version: require enterprise wechat, know more things by click [here](https://sct.ftqq.com/), the only difference in cptools is the parameter `text` change to `title`
  ```python
  from cptools.notify import ServerChan
  # from cptools import ServerChan  # both will work
  
  SJ = ServerChan()
  SJ.token='your ServerChan token'  # your ServerChan token
  SJ.send_text(title='This is a test.', desp='This is description.')
  
  # or you can do this
  SJ = ServerChan(token='your ServerChan token')  
  SJ.send_text(text='This is a test.', desp='This is description.')
  ```
- DingDing: notify everyone in your dingTalk group by [dingTalk_bot](https://developers.dingtalk.com/document/app/before-you-start)
> after `v.1.4.5`, cptools will not install `DingtalkChatbot` automatically, you have to install it by running `pip install DingtalkChatbot` manually
```python
from cptools.notify import DingDing

dd = DingDing()
dd.token='your DingDing assess_token'  
dd.send_text(text='[key word]This is a test.')  # your test should include the key word that you specify 

# or you can do this
dd = DingDing(token='your DingDing assess_token' )
dd.send_text(text='[key word]This is a test.')  # your test should include the key word that you specify 
```
- Email: notify people by sending an email
- [x] 163 email
- [x] qq email
- [ ] others, haven't tested
> after `v.1.4.5`, cptools will not install `yagmail` automatically, you have to install it by running `pip install yagmail` manually

```python
from cptools.notify import EmailSender
email = EmailSender(user='xx@qq.com',  
                    password_or_auth_code='auth code',  # depending on your email vendor
                    host='smtp.xx.com')  # you should use smtp serve
email.send_text(text='test', contents='this is a test mail', to=['xx@qq.com',])
```

- mac_notify: show a message on your mac, it could be really nice when you have a mac.

```python
from cptools.notify import mac_notify

mac_notify(title='Warning', text='This is a test')
```

result is something like this:

![](https://gitee.com/gentlecp/ImgUrl/raw/master/20210120115105.png)


## logger
> logger is used to print log in your program, it can reduce the amount of time you spend on configuring logging 
- LogHandler: you shall start with a simple LogHandler

```python
from cptools.logger import LogHandler

log = LogHandler("the name of LogHandler")  # by default, the name will be the __name__
log.info('this is a test msg')  # 2021-01-30 14:35:48,639 logger.py-[line:130] 【INFO】 this is a test msg
```

- LogHandler with different configuration
    - `name`: The name of LogHandler
    - `level`: Log level, default `INFO`
    - `steam`: If True, show log in terminal, default `True`
    - `file`: If True, save log to local file, defalut `False`
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

## function
- `is_unique(seq)`: judge whether a giving sequence has repeating elements or not
```python
from cptools import is_unique

a = [1,2,3]
b = [4,4,5]
print(is_unique(a))  # True
print(is_unique(b))  # False
```
- `chunk_list(lst, size)`: split a list into num chunks by specifying the chunk size
```python
from cptools import chunk_list

a = [1,2,3,4,5]
print(list(chunk_list(a, 2)))  # [[1,2], [3,4], 5]
```
- `flatten_seq(seq)`: flatten a deep sequence into a single one
```python
from cptools import flatten_seq

a = [[1,2],[[3,4]],5]
print(list(flatten_seq(a)))  # [1,2,3,4,5]
```