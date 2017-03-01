import os

h_filter = ['.h','.hpp']
c_filter = ['.c','.cpp']

def HFilter(name):
    ext = os.path.splitext(name)[1]
    print(ext)
    if ext in h_filter:
        return name
    else:
        return None

def CFilter(name):
    ext = os.path.splitext(name)[1]
    if ext in c_filter:
        return name
    else:
        return None

def walkDir(path):
    for i in os.walk(path):
        pathDistance = os.path.relpath(i[0],path)
        files = i[2]
        aaa = map(HFilter,files)
        print(list(aaa))

if __name__=='__main__':
    path = r"C:\Users\zfliu\Desktop\srs\trunk"
    walkDir(path)