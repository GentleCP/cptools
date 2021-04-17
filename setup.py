from setuptools import setup
import setuptools

__name__ = "cptools"
__version__ = '1.4.3'
__author__ = 'GentleCP'
__author_email__ = '574881148@qq.com'
__description__ = 'Tools used by CP'
__url__ = 'https://github.com/GentleCP/cptools'


with open("README.md", 'r', encoding='utf8') as f:
    long_description = f.read()

setup(
    name = __name__,  # 包名称
    version = __version__,
    author = __author__,
    author_email = __author_email__,
    description = __description__,
    long_description = long_description,
    long_description_content_type="text/markdown",
    install_requires = [
        'requests >= 2.23',
        'tqdm >= 4.45',
        'DingtalkChatbot >= 1.5.2',
        'yagmail >= 0.11.224',
    ],
    url = __url__,
    packages = setuptools.find_packages(),  # 让setuptools自动发现包
    platforms = 'any',  # 包使用的平台
    classifiers = [
        'Programming Language :: Python :: 3',  # 采用编程语言
        'License :: OSI Approved :: GNU General Public License (GPL)',  # 采用的许可证协议
        'Operating System :: OS Independent',  # 操作系统
    ]
)