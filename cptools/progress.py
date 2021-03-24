'''
显示所有的进度信息，包括网页内容下载，运行训练过程等
'''
import requests
import os
from tqdm import tqdm

def download_file(url, session=None, file_path='new_file', overwrite = False):
    '''
    根据指定url下载文件
    :param url:
    :param session: 传入的会话参数，有的需要登录才能下载
    :param file_path: 文件存储路径，默认为当前目录下，存储文件为未命名文件
    :param overwrite: 是否覆盖同名文件，默认否
    :return: 正确下载返回True，否则False
    '''
    if session:
        res = session.get(url, stream = True)
    else:
        res = requests.get(url,stream=True)
    file_size = int(res.headers['content-length'])
    chunk_size = 1024
    if res.status_code == 200:
        if not overwrite and os.path.exists(file_path):
            return True
        else:
            progress_bar = tqdm(
                total=file_size,initial=0,unit='B',unit_scale=True,
            )
            with open(file_path,'wb') as f:
                for data in res.iter_content(chunk_size=chunk_size):
                    if data:
                        f.write(data)
                        progress_bar.update(chunk_size)
            progress_bar.close()
    else:
        return False

# if __name__ == '__main__':
#     url = "https://dl.360safe.com/360/inst.exe"
#     download_file(url)