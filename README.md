# docx2html
将Docx文件转化为Html文件。该工具使用pydocx工具，遍历目录中所有的doc文件，并将其转化为html文件。

## 前置条件
- 安装pywin32库
- 安装docx库，使用如下命令安装
  > pip3 install pydocx

## 使用说明
> python3 doc2html  _[Doc files directory path]_  _[Outputs files directory path]_

---

# ChangeName
将docx2html脚本生产的html文件拷贝并修改成可以导入米家滑板车插件中的html文件

## 使用说明
> python3 ChangeName.py  _[Html_files_directory_path]_  _[Outputs files directory path]_
