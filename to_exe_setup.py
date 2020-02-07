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


from cx_Freeze import setup, Executable

# 配置封装的参数
#  (script, initScript = None, base = None,
#             targetName = None, icon = None, shortcutName = None,
#             shortcutDir = None, copyright = None, trademarks = None
executables = [Executable(
                          # 生成可执行文件的主文件
                          script = "16_time.py",

    # 生成可执行文件及一些依赖文件的目录
    # targetDir = r"D:\桌面\python",
    # 可执行文件的名称
    # targetName = "Food_menu.exe",
    # 可执行文件的ico图标
    # icon = "",

    # includes = includes,
    # excludes = excludes,
    # packages = packages,

    # 是否需要压缩模块的字节码
    # compress = True,

    # 是否拷贝依赖文件到目标目录
    # copyDependentFiles = True,

    # 是否附加脚本模块到执行文件
    # appendScriptToExe = True,
    # 是否添加脚本模块到共享库
    # appendScriptToLibrary = False,

    # 设置快捷方式的路径及名称
    # shortcutDir = "",
    # shortcutName = ""

)]
# 设置安装时软件包的描述信息
setup(name = "test",
      version = "0.1",
      description = "My first python program",
      author = "zhouxu",
      executables = executables
      )


# 这里可以编写客户化的封装后处理代码。例如：临时数据的清除，数据包的发布等



# 到此，整个setup脚本已经完成。
