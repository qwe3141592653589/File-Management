import sys

user_file = '' #用户文件地址
f = '0' #用户的文件
user_writing = [0] #用户写入的内容
help = 'file类：exit退出 open打开文件地址  read类：exit退出  all 读取所有内容 line读取指定行数  setting类：information版本信息 help帮助手册 change类：add添加内容 seach类：敬请期待' #帮助手册

def file(): #file 模块 命令支持 exit退出 open打开文件地址 已完成(整个模块)
    global user_file
    a = input('很好，一切的开始，请继续输入进行文件操作，当前位置:file->?')
    if a == 'open':
        user_file = input('请输入文件的绝对路径，当前位置file->open(此位置并非当前选中位置，仅为状态)')
        print('输入已完成，更改地址请重新运行file->open')
        print('已回到首页')
        return
    if a == 'exit':
        return
    

def read(): #read 模块 命令支持 exit退出  all 读取所有内容 line读取指定行数 已完成(整个模块)
    global user_file
    a = input('警告！继续使用该命令会丢失\'change\'命令中已更改的内容，键入\'ok\'继续，其他键返回')
    if a != 'ok':
        return
    a = input('请继续输入，目前在read->?')
    if a == 'exit':
        return
    print(r'可能展示出的内容中有/n的内容，/n为换行符')
    if len(user_file) == 0:
        print('请先运行file')
        return
    f = open(user_file,'r')
    if a == 'exit':
        f.close
        return
    if a == 'all':
        temp_read = f.read()
        print(temp_read)
        print('---以上是文档---,已回到首页')
        f.close()
        return
    if a == 'line':
        a = input('请继续输入行号(多个行号用空格分隔)，目前在read->line->?')
        temp_read = f.readlines()
        a = a.split()
        for i in a:
            print(f'第{i}行：'+str(temp_read[int(i)-1]))
        f.close
        return
    else:
        print('你可能输入了错误的命令，重试')
        return

def setting(): #setting模块 命令支持 information版本信息 help帮助手册 已完成(整个模块)
    global help
    a = input('请继续输入，目前在setting->?')
    if a == 'information':
        print('当前版本：1.0')
        return
    if a == 'help':
        print(help)
        return

def seach(): #seach模块 未制作 已完成(整个模块)
    print('当前版本不支持 检索 功能')

def change(): #change模块 命令支持 add添加内容
    global user_file
    while True:
        a = input('请继续输入，目前在change->?')
        if a == 'add': #添加
            if len(user_file) == 0: #文件添加性检查
                print('你还没有打开文件,请先运行 file->open,add命令不适用新建文件')
                break
            f = open(user_file,'r')
            temp_read = f.read()
            f.close()
            user_writing = []
            while True:
                print(temp_read)
                for i in user_writing:
                    print(i)
                print('以上是当前文件内容 空行前是你之前的文件内容，空行后是你之后的文件内容')
                temp_write = input('请输入追加内容(写完一行按回车)，输入//exit//保存退出,退出要把前后的斜杠带上,目前在change->add')
                if temp_write == '//exit//': #退出
                    a = input('是否保存y/n')
                    if a == 'y': #保存
                        f = open(user_file,'a')
                        for i in user_writing:
                            f.write(i)
                            f.write('\n')
                        f.close()
                        print('已保存')
                        user_writing = []
                        break
                    if a == 'n': #不保存
                        break
                user_writing.append(temp_write)
            return

while True:
    temp = input('请输入命令头部分(如read [行号]中仅输入\'read\')')
    if temp == 'exit':
        sys.exit()
    if temp == 'change':
        change()
    if temp == 'read':
        read()
    if temp == 'seach':
        seach()
    if temp == 'file':
        file()
    if temp == 'setting':
        setting()
