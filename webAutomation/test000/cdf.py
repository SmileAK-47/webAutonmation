#encoding = utf-8
def cdf():
    try:
        localpath = r'G:\KeyWordFromeWork\log\TestLogfile.log'
        newpath = r'G:\KeyWordFromeWork\log\new4.22.log'
        list = []
        file = open(localpath,mode='r',encoding='gbk')
        lines = file.readlines()
        with open(newpath,'w',encoding='utf-8'):
            for line in lines:
                if 'INFO' in line:
                    # print(line)
                    list.append(line)
                    # print(list)
            print(str(len(list)))
    except:
        print("zijian---- error")

if __name__ == '__main__':
    cdf()