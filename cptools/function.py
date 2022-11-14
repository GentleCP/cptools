#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Common tool functions

- `read_json(file_path)`: Read json data into python dict
- `write_json(content, file_path)`: Write dict into json file
- `read_pickle(file_path)`: Read content of pickle file
- `write_pickle(content, file_path)`: Write content to pickle file
- `execute_cmd(cmd)`: Execute given shell command
- `gen_md5(string_or_file_path)`: Generate md5 value of a given file path or a string
- `download_file(url, save_path)`: Download file for a given link
"""

import json
import pickle as pkl
import subprocess
import hashlib
import requests

from collections import OrderedDict
from typing import Union
from pathlib import Path
from tqdm import tqdm


def read_json(file_path: Union[str, Path], by_line: bool = False, **kwargs) -> OrderedDict:
    """Read json data into python dict
    Args:
        file_path: file save path
        by_line: if True, read data line by line
        **kwargs: other parameters used in open()
    Returns:
        json content
    """
    file_path = Path(file_path)
    with file_path.open('rt', **kwargs) as handle:
        if by_line:
            for line in handle:
                yield json.loads(line)
        else:
            return json.load(handle, object_hook=OrderedDict)


def write_json(content: dict, file_path: Union[str, Path], by_line: bool = False, **kwargs):
    """Write dict into json file
    Args:
        content: data dict
        file_path: file save path
        by_line: if True, write data line by line
        **kwargs: other parameters used in open()
    Returns:
        None
    """
    file_path = Path(file_path)
    with file_path.open('wt', **kwargs) as handle:
        if by_line:
            for line_data in content:
                handle.write(line_data + '\n')
        else:
            json.dump(content, handle, indent=4, sort_keys=True)


def read_pickle(file_path: Union[str, Path], **kwargs) -> object:
    """Read content of pickle file
    Args:
        file_path: file save path
        **kwargs: other parameters used in open()
    Returns:
        content of pickle file

    """
    file_path = Path(file_path)
    with file_path.open('rb', **kwargs) as handle:
        return pkl.load(handle)


def write_pickle(content: object, file_path: Union[str, Path], **kwargs):
    """Write content to pickle file
    Args:
        content: python object
        file_path: file save path
        **kwargs: other parameters used in open()
    Returns:
        None
    """
    file_path = Path(file_path)
    with file_path.open('wb', **kwargs) as handle:
        pkl.dump(content, handle)


def execute_cmd(cmd: Union[str, list], timeout: int = 900) -> dict:
    """Execute given shell command
    Args:
        cmd: command, could be a list or string. e.g., ['ls', '-l'] or 'ls -l'
        timeout:

    Returns:
        A dict of execute result, including errcode and errmsg(if errcode==0, errmsg is output)
    """
    try:
        p = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                           timeout=timeout)

    except subprocess.TimeoutExpired as e:
        return {
            'errcode': 401,
            'errmsg': 'timeout'
        }
    return {
        'errcode': p.returncode,
        'errmsg': p.stdout.decode()
    }


def gen_md5(string_or_file_path: Union[str, Path]) -> str:
    """Generate md5 value of a given file path or a string

    Args:
        string_or_file_path: string literal or a file path

    Returns:
        md5

    """
    if Path(string_or_file_path).is_file():
        with open(string_or_file_path, 'rb') as f:
            m = hashlib.md5()
            chunk = f.read(4096)
            while chunk:
                m.update(chunk)
                chunk = f.read(4096)
    else:
        m = hashlib.md5()
        m.update(string_or_file_path.encode())
    return m.hexdigest()


def download_file(url: str, save_path: Union[str, Path] = "download_file", **kwargs) -> bool:
    """Download file for a given link

    Args:
        url: download link
        save_path: file save path
        **kwargs: `session`(option): if provide, download link from session

    Returns:
        download result: True if download success else False
    """
    session = kwargs.get('session', requests)
    if session:
        res = session.get(url, stream=True)
    else:
        res = requests.get(url, stream=True)
    file_size = int(res.headers['content-length'])
    chunk_size = 1024
    if res.status_code == 200:
        progress_bar = tqdm(
            total=file_size, initial=0, unit='B', unit_scale=True,
        )
        with open(save_path, 'wb') as f:
            for data in res.iter_content(chunk_size=chunk_size):
                if data:
                    f.write(data)
                    progress_bar.update(chunk_size)
        progress_bar.close()
        return True
    else:
        return False
