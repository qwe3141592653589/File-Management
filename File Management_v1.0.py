import sys

user_file = '' #用户文件地址
f = '0' #用户的文件
user_writing = [0] #用户写入的内容
user_file_read = '' #用户以读取
help = '' #帮助手册

def file(a):
    global user_file_read;user_file;user_file_read;help;user_writing
    if a == 'open':
        user_file = input('请输入文件的绝对路径')
        f = open(user_file,'+','utf-8')
        user_file_read = f.readlines()
        user_writing = user_file_read

def read(a):
    global user_file_read;user_file;user_file_read;help
    if a == 'exit':
        f.close()
        sys.exit()
    if a == 'all':
        for i in user_file_read:
            print(i)

def setting(a):
    global user_file_read;user_file;user_file_read;help
    if a == 'information':
        print('当前版本：1.0')
    if a == 'help':
        print(help)

def seach(a):
    global user_file_read;user_file;user_file_read;help
    print('当前版本不支持 检索 功能')

def change(a):
    global user_file_read;user_file;user_file_read;help
    if a == 'add':
        while True:
            if len(user_writing) == 0:
                print('你还没有打开文件,请先运行 file open')
                return 
            temp_write = input('请输入追加内容(写完一行按回车)，输入//exit//退出')
            if temp_write == '//exit//':
                break
            user_writing.append(temp_write)
    if a == 'remove':
        temp = input('请输入删除行数')
        temp = int(temp)
        user_writing.remove(user_writing[temp])
    if a == 'save':
        f.write(user_writing)
        f.close()
        f = open(user_file,'+','utf-8')
        user_file_read = f.readlines()
        user_writing = user_file_read
        print('操作成功')
    if a == 'save and exit':
        f.write(user_writing)
        f.close()
        sys.exit()
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
    temp_i = 0
    temp_cmd = []
    temp = input('请输入命令')
    if temp == 'exit':
        sys.exit()
    for i in range(len(temp)):
        if temp[i] == ' ':
            temp_i = i
            break
    temp_cmd.append(temp[:temp_i])
    temp_cmd.append(temp[temp_i+1:])
    if temp_cmd[0] == 'change':
        change(temp_cmd[1])
    if temp_cmd[0] == 'read':
        read(temp_cmd[1])
    if temp_cmd[0] == 'seach':
        seach(temp_cmd[1])
    if temp_cmd[0] == 'file':
        file(temp_cmd[1])
    if temp_cmd[0] == 'seeting':
        setting(temp_cmd[1])
