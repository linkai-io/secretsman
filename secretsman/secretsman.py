from .env_secrets import EnvSecrets
from .ssm_secrets import SSMSecrets

class Secrets(object):
    """
    Custom Secrets Manager
    """
    def __init__(self, env, region):
        """
        Constructor for our secrets manager, sets environment
        specific implementations (os env vars for local/testing)
        AWS SSM for dev/prod etc.
        """
        self.env = env
        self.region = region
        if env == 'local':
            self.impl = EnvSecrets(env)
        else:
            self.impl = SSMSecrets(env, region)
        
    def GetSecureParameter(self, key):
        """
        Calls the secrets implementation to securely get value for
        the defined key.
        """
        return self.impl.GetSecureParameter(key)

    def SetSecureParameter(self, key, value):
        """
        Calls the secrets implementation to securely set value for
        the defined key.
        """
        self.impl.SetSecureParameter(key, value)

    def GetPassword(self):
        """
        Example of retrieving password from our secrets implementation 
        Add other methods to this class for uniform access to secrets,
        regardless of environment.
        """
        path = '/some/{}/password'.format(self.env)
        return self.impl.GetSecureParameter(path)