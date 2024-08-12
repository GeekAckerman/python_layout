## 命令

```sh
python3 setup.py build
```

```sh
python3 setup.py develop
```

```sh
pip3 install lib_name
pip3 uninstall lib_name
```

## python 项目结构

```
/res/ 下面放所有的 yaml 配置文件，我用 yaml 来保存项目配置信息，例如数据库访问路径和其他 token
/src/ 目录存放所有的源码
/src/common/ 目录存放工具函数和整个项目要使用的小模块
/src/component/ 目录存放项目要使用的工具类，我将数据库相关的功能例如 SQLAlchemy 这些库做了二次封装。
/src/dao/ 目录存放直接操作数据库的类
/src/entity/ 存放各种数据对象的定义，我把所有的 Python 字典用 typing 库做了 TypedDict 数据类型描述，这样在开发的时候不容易出错，避免动态类型语言难以重构的通病
/src/route/ 下保存 FastAPI 的 API 入口函数，类似于 SpringBoot 的 Controller
/src/service/ 下存放各种实现业务逻辑的服务类
/src/app.py FastAPI 的 APP 定义脚本
/src/run.py 执行 app.py 的脚本
/test/ 目录存放测试用例
/main.py 在项目根目录下的入口脚本文件。每次启动项目从这里开始就行了，简单方便。这个脚本直接调用 /src/run.py
/pyproject.toml poetry 使用的项目配置文件
/Dockerfile.base 生成 Docker 依赖的镜像
/Dockerfile.build 打包项目源码的镜像
```
