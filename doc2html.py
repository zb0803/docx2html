# _*_ encoding: utf-8 -*-

##############################################################################
# 该脚本将doc转为html文件
##############################################################################

from pydocx import PyDocX
import os
import sys

# Doc转换成Html文件
def doc2html(docPath, htmlPath):
    html = PyDocX.to_html(docPath)
    f = open(htmlPath, 'w', encoding="utf-8")
    f.write(html)
    f.close()

# 将某一个目录中的所有xml文件转换成md
def covert(srcdir, targetdir):
    # print("Source:" + srcdir)
    # print("Target:" + targetdir)
    count = 0
    if not os.path.exists(targetdir):
        os.mkdir(targetdir)

    for file in os.listdir(srcdir):
        filepath = os.path.join(srcdir, file)
        if os.path.isdir(filepath):
            dir1 = os.path.join(srcdir, file)
            dir2 = os.path.join(targetdir, file)
            count = count + covert(dir1, dir2)
        else:
            # print("<- Bill -> filepath:" + filepath)
            # 获取文件后缀
            fileName, fileSuffix = os.path.splitext(file)
            if fileSuffix == '.doc' :
                # 将doc文件转换为docx文件
                print("Found doc file, Need convert docx(" + filepath + ")")
            elif fileSuffix == '.docx':
                count = count + 1
                htmlPath = os.path.join(targetdir, fileName) + ".html"
                print("转化 " + htmlPath)

                doc2html(filepath, htmlPath)
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

    print("<- 开始转化 -> Doc directory: " + docDir + ", Html directory: " + htmlDir)
    count = covert(docDir, htmlDir)

    if count <= 0:
        print("未成功找到doc文件")
    else:
        print("成功转换 %d 个文件" % count)
    