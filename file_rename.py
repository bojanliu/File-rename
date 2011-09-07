#coding:utf-8
#filename:file_rename.py
#批量修改文件名

import os

def main():
    file_path=raw_input(u'请输入文件所在路径：').decode('gb2312')#中文编码问题
    if os.path.exists(file_path):#判断给出的路径是否存在
        a=os.walk(file_path)#walk函数得到的是一个元祖(路径,目录,文件名)
        for root, dirs, files in a:
            i=0
            file_name=raw_input('请输入您想要的文件前缀名：').decode('gb2312')
            file_num=len(files)#文件个数
            num=len(str(file_num))#根据文件个数决定编号位数
            for file in files:
                index=file.rfind('.')#'.'号的索引号
                suffix=file[index:len(file)]#保留后缀名
                os.rename(
                    os.path.join(root,file),#文件重命名函数
                    os.path.join(root,u'%s%s%s'%(file_name,str(i).zfill(num),suffix))
                          )#zfill函数用0补全位数
                i+=1
        print 'ok'
    else:
        print 'sorry, but the path is not exist!'

if __name__=='__main__':
    main()
