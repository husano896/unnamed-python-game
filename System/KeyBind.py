Keys = {}

def RegisterKey(keyName, DefaultButton = None):
    global Keys
    Keys[keyName] = DefaultButton

def GetKey(keyName)
    global Keys
    #不用Get是為了確保Key在沒有被註冊時會回傳錯誤
    return Keys[keyName]

def IsKeyRegistered(keyName):
    global Keys
    
    return Keys.has_key(key)
