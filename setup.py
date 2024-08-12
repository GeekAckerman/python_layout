from setuptools import setup, find_packages

__version__ = "0.1.0"  # 版本号
requirements = open("./requirements.txt").readlines()  # 依赖文件

setup(
    name="python-layout",  # 在pip中显示的项目名称
    version=__version__,
    author="",
    author_email="",
    url="",
    description="",
    packages=find_packages(
        exclude=("tests", "docs")
    ),  # 项目中需要拷贝到指定路径的文件夹
    python_requires=">=3.7.0",
    install_requires=requirements,  # 安装依赖
)
