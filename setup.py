from setuptools import setup
import setuptools


with open("README.md", 'r', encoding='utf8') as f:
    long_description = f.read()

setup(
    name = 'cptools',  # 包名称
    version = '1.1.1',  # 版本号，我个人喜欢从1开始
    author = 'GentleCP',
    author_email = '574881148@qq.com',
    description = 'Tools used by CP',
    long_description = long_description,
    long_description_content_type="text/markdown",
    install_requires = [
        'requests >= 2.23',
        'tqdm >= 4.45',
    ],
    url = 'https://github.com/GentleCP/cptools',   # 包的主页，如果你发布在了github就填写github链接
    packages = setuptools.find_packages(),  # 让setuptools自动发现包
    platforms = 'any',  # 包使用的平台
    classifiers = [
        'Programming Language :: Python :: 3',  # 采用编程语言
        'License :: OSI Approved :: MIT License',  # 采用的许可证协议
        'Operating System :: OS Independent',  # 操作系统
    ]
)