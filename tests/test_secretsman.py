import pytest
from secretsman import Secrets

def test_local_secrets():
    env = 'local'
    s = Secrets(env, 'us-east-1')
    s.SetSecureParameter('/some/{}/password'.format(env), 'password123')
    assert s.GetPassword() == 'password123'

def test_dev_secrets():
    env = 'dev'
    s = Secrets(env, 'us-east-1')
    s.SetSecureParameter('/some/{}/password'.format(env), 'password123')
    assert s.GetPassword() == 'password123'