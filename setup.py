from setuptools import setup
import setuptools
from pathlib import Path

about = {
    '__name__': "cptools",
    '__version__': '2.0.0',
    '__author__': 'GentleCP',
    '__author_email__': 'me@gentlecp.com',
    '__description__': 'Tools used by CP',
    '__url__': 'https://github.com/GentleCP/cptools',
}

with open("README.md", 'r', encoding='utf8') as f:
    long_description = f.read()

setup(
    name=about['__name__'],  # 包名称
    version=about['__version__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    description=about['__description__'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'requests >= 2.23',
        'tqdm >= 4.45',
    ],
    url=about['__url__'],
    packages=setuptools.find_packages(),  # 让setuptools自动发现包
    platforms='any',  # 包使用的平台
    classifiers=[
        'Programming Language :: Python :: 3',  # 采用编程语言
        'License :: OSI Approved :: GNU General Public License (GPL)',  # 采用的许可证协议
        'Operating System :: OS Independent',  # 操作系统
    ]
)
