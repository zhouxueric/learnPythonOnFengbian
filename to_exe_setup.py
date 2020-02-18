# -*- coding: utf-8 -*-
#  文 件 名：to_exe_setup.py
# 功能描述：cx_freeze封装Python脚本的配置文件
#
# 作者：zhouxu    日期：2020/02/04
#
# 版权：可以使用、传播，但请保留出处；如需修改，请告知作者。
# environment in which the script runs
#
# Run the build process by running the command 'python to_exe_setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the script without Python

# import sys
from cx_Freeze import setup, Executable

_script = "My_labrary.py" # 生成可执行文件的主文件
_targetName = "labrary.exe" # 可执行文件的名称
_icon = None #"jin.ico" # 可执行文件的ico图标，要icon的话，_targetName不能有中文
base = None
# if sys.platform == 'win32':
#     base = 'Win32GUI'
# 配置封装的参数
#             (script, initScript = None, base = None,
#             targetName = None, icon = None, shortcutName = None,
#             shortcutDir = None, copyright = None, trademarks = None)
executables = [Executable(script=_script, base=base, targetName=_targetName, 
                          icon=_icon,
              )]
# 设置安装时软件包的描述信息
setup(name = "app",
      version = "0.1",
      description = "My python labrary",
      author = "zhouxu",
      executables = executables
      )

# 这里可以编写客户化的封装后处理代码。例如：临时数据的清除，数据包的发布等
import time
info = time.strftime('%Y-%m-%d %H:%M:%S ',time.localtime()) + '%s封装成功,可执行文件名称为%s,请在build\\exe.win-amd64-3.7中查看\n'%(_script, _targetName)
with open('to_exe_log.txt', 'a', encoding='utf-8') as f:
      f.writelines(info)

print(info)
# print('%s封装成功,可执行文件名称为%s,请在build\\exe.win-amd64-3.7中查看'% (_script, _targetName))

# cleanup namespace
# del setup, Executable, time
# 到此，整个setup脚本已经完成。
