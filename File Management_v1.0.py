import sys

user_file = '' #用户文件地址
f = '0' #用户的文件
user_writing = [0] #用户写入的内容
help = '' #帮助手册

def file(a):
    global user_file
    a = input('很好，一切的开始，请继续输入进行文件操作，当前位置:file->?')
    if a == 'open':
        user_file = input('请输入文件的绝对路径，当前软件位置file->open')

def read(): #read 模块 命令支持 exit退出  all 读取所有内容 line读取指定行数
    global user_file
    a = input('警告！继续使用该命令会丢失\'change\'命令中已更改的内容，键入\'ok\'继续，其他键返回')
    if a != 'ok':
        return
    a = input('请继续输入，目前在read->?')
    print(r'可能展示出的内容中有\'/n\'的内容，/n为换行符')
    f = open(user_file,'r')
    if a == 'exit':
        f.close
        sys.exit()
    if a == 'all':
        temp_read = f.readlines()
        for i in temp_read:
            print(temp_read)
        print('---以上是文档---,已回到首页')
        f.close()
        return
    if a == 'line':
        a = input('请继续输入行号(多个行号用空格分隔)，目前在read->line->?')
        temp_read = f.readlines()
        a = a.split()
        for i in a:
            print(temp_read[int(i)])
        f.close
        return
    else:
        print('你可能输入了错误的命令，重试')
        return

def setting(): #seeting模块 命令支持 information版本信息 help帮助手册
    global help
    a = input('请继续输入，目前在setting->?')
    if a == 'information':
        print('当前版本：1.0')
        return
    if a == 'help':
        print(help)
        return

def seach(): #seach模块 未制作
    print('当前版本不支持 检索 功能')

def change():
    global user_file
    while True:
        a = input('请继续输入，目前在change->?')
        if a == 'add': #添加
            while True:
                user_writing = []
                if len(user_file) == 0: #文件添加性检查
                    print('你还没有打开文件,请先运行 file->open')
                    break
                f = open(user_file,'a')
                temp_write = input('请输入追加内容(写完一行按回车)，输入//exit//保存退出,退出要把前后的斜杠带上,目前在change->add')
                if temp_write == '//exit//': #退出
                    a = input('是否保存y/n')
                    if a == 'y': #保存
                        for i in user_writing:
                            f.write(i)
                            f.write('\n')
                        print('已保存')
                        user_writing = []
                        break
                    if a == 'n': #不保存
                        f.close()
                        break
                user_writing.append(temp_write)
            return
        if a == 'remove':
            a = input('请输入删除行数')
            user_writing.remove(user_writing[temp])
        if a == 'exit':
            temp = input('你可能未保存，是否保存一次？ Y/N')
            if temp == 'y' or 'Y':
                f.write(user_writing)
                f.close()
                print('操作成功')
            sys.exit()
        if a == 'chang':
            print(user_writing)
            temp = input('以上是你正在编辑的内容，请输入编辑行号')
            temp = int(temp)
            temp_write = input('请输入更改内容')
            user_writing[temp] = temp_write
            print('操作成功')
            print(user_writing)
            print('以上是操作后的结果，如需保存，请输入 change save and exit 或者 change save')
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
    if temp == 'seeting':
        setting()
