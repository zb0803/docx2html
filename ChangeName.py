# _*_ encoding: utf-8 -*-

##############################################################################
# 该脚本将doc转为html文件
##############################################################################

import shutil
import os
import sys

# 将某一个目录中的所有xml文件转换成md
def covert(srcdir, targetdir):
    count = 0
    if not os.path.exists(targetdir):
        os.mkdir(targetdir)

    for file in os.listdir(srcdir):
        filepath = os.path.join(srcdir, file)
        if os.path.isdir(filepath):
            dir1 = os.path.join(srcdir, file)
            count = count + covert(dir1, targetdir)
        else:
            # 获取文件后缀
            fileName, fileSuffix = os.path.splitext(file)
            if fileSuffix == '.html' or fileSuffix == '.xml' :

                b = False
                if file.find('用户协议') >= 0: # 找到用户协议文件
                    tName = os.path.basename(srcdir).lower() + "nb_agreement" + fileSuffix
                    d = os.path.join(targetdir, "agreement")
                    p = os.path.join(d, tName)
                    b = True
                elif file.find('隐私政策') >= 0: # 找到隐私政策文件
                    tName = os.path.basename(srcdir).lower() + "nb_privacy" + fileSuffix
                    d = os.path.join(targetdir, "privacy")
                    p = os.path.join(d, tName)
                    b = True

                if b:
                    if not os.path.exists(d):
                        os.mkdir(d)
                    try:
                        shutil.copy(filepath, p)
                        count = count + 1
                    except IOError as e:
                        print("Unable to copy file: %s" % e)
                    except:
                        print("Unexcepted error: %s" % e)

    return count


##############################################################################
# main方法执行
##############################################################################
if __name__ == '__main__':
    docDir = os.path.abspath(".") # 默认源文件存放目录为当前目录
    htmlDir = os.path.abspath(".") # 默认目标目录为当前目录

    if len(sys.argv) >= 2 : # 获取命令中源文件存放目录
        docDir = os.path.abspath(sys.argv[1])

        if len(sys.argv) >= 3 : # 获取命令中目标文件存放目录
            htmlDir = os.path.abspath(sys.argv[2])

    print("<- 开始修改文件名称 -> Source directory: " + docDir + ", Target directory: " + htmlDir)
    count = covert(docDir, htmlDir)

    if count <= 0:
        print("未成功找到html文件")
    else:
        print("成功转换 %d 个文件" % count)
    