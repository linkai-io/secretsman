import boto3
from botocore.exceptions import ClientError
import logging 

class SSMSecrets(object):
    def __init__(self, env, region):
        """
        Create the boto3 ssm client for the specified environment and region
        """
        self.env = env 
        self.region = region
        self.session = boto3.Session(region_name=region)
        self.client = self.session.client('ssm')

    def GetSecureParameter(self, key):
        """
        Returns the decrypted parameter value from the specified key
        """
        try: 
            parameter = self.client.get_parameter(Name=key, WithDecryption=True)
            return parameter['Parameter']['Value']
        except ClientError as e:
            logging.error('failed to get key {}'.format(e.response['Error']['Code']))

    def SetSecureParameter(self, key, value):
        """
        It is not recommended to use this method, use an external lambda/custom resource
        as part of your deployment process.
        """
        try:
            self.client.put_parameter(Name=key, Value=value, Type='SecureString', Overwrite=True)
        except ClientError as e:
            logging.error('failed to set key {}'.format(e.response['Error']['Code']))