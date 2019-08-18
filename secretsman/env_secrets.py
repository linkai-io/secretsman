import os 

class EnvSecrets(object):
    def __init__(self, env):
        self.env = env 

    def GetSecureParameter(self, key):
        path = key.replace('/','_')
        return os.getenv(path, None)

    def SetSecureParameter(self, key, value):
        path = key.replace('/','_')
        os.environ[path] = value
