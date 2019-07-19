from setuptools import setup, find_packages

setup(
    name="yytest",  # pip项目发布的名称
    version="1.0.6",  # 版本号
    keywords=("piptest"),
    description="time and path tool",
    long_description="time and path tool",
    license="MIT Licence",

    url="https://github.com/wooyoung1029/test",   # 项目相关文件地址，一般github
    author="wooyoung",
    author_email="1021218480@qq.com",

    packages=find_packages('../yytest'),
    include_package_data=True,
    platforms="any",
    install_requires=[]  # 需要的第三方库
)
