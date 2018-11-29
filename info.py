import os

def returnDir():
    dirs = ['C:\\Recycler\\', 'C:\\Recycled\\', 'C:\\$Recycle.Bin\\']
        for recycleDir in dirs:
            if os.path.isdir(recycleDir):
                folder  = str(recycleDir)
                files = os.system('dir '+folder+ '/a')
                return files
        return None

def getUserInfo():	
    users = os.system('wmic useraccount get name')
    sid = os.system('wmic useraccount get sid')
    return users
    return sid

getUserInfo()
returnDir()

