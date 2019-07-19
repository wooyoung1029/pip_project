## 安装pip上传工具 twine
    pip install twine

## 本地打包项目
     cd 到存放setup.py文件的目录，生成dist/yytest-1.0.0.tar.gz
     python setup.py sdist 

## 上传项目到pypi
    在上传前，要建一个文件，$HOME/.pypirc（因为不能使用python setup.py register进行上传，使用这个上传会报一个410的错误。所以要使用.pypirc文件保存你的PyPi用户信息，这时使用下载的twine就可以直接上传了）
    [distutils]
    index-servers = pypi

    [pypi]
    username:PyPi用户名
    password:PyPi密码

    上传好打包的pip安装包:
    twine upload dist/yytest-1.0.0.tar.gz
    
## 下载
    pip install yytest
