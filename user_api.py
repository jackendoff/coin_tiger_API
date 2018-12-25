import time
from content_safe import APIKEY,APISECRET
import hashlib
import hmac


class UserApi(object):
    '''cointiger的api接口'''

    def __init__(self):
        self.apikey = APIKEY
        self.apisecret = APISECRET

    # 创建密钥
    # secret ="price" + price + "side" + side + "symbol" + symbol + "type" + type + "volume" + volume + "time" + nowtime + self.apisecret
    def get_sign(self,secret):
        return hmac.new( self.apisecret.encode("UTF-8"), secret.encode("utf-8"), hashlib.sha512).hexdigest()

