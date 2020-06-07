#--接口自动化，获取sign和token的方法，class半封装

import time
import hashlib
import requests

# account_id = ""
# code = ''
# il_id = ''
# question_id = ''
# q_id = ''
# para = {}
# secret_key = ''

class Basics():

    def __init__(self, account_id, code, secret_key, token_url):
        self.account_id = account_id
        self.code = code
        self.secret_key = secret_key
        self.token_url = token_url

    # 获取验证码
    # 获取sign_at
    def get_signed_at(self):
        t = time.time()
        signed_at = str(int(t))
        return signed_at



    # 获取sign
    # 需求：para参数，按照key的首字母大小排序，并前后拼接secret_key，md5转换后，输出sign
    def get_sign(self):
        self.para = {"from": "ios_pad", "account_id": self.account_id, 'signed_at': self.get_signed_at(),
                     "phone": '*******',
                     "code": self.code, "nickname": "guozhendeng1"}
        t = sorted(self.para.items(), key=lambda item: item[0])  # 进行字典排序
        re = ''
        for x in t:
            re += "".join(["".join(x)])
        signss = self.secret_key + re + self.secret_key
        m1 = hashlib.md5()  # md5转换
        m1.update(signss.encode(encoding='utf-8'))
        sign = m1.hexdigest()
        return sign

    # 获取token

    def get_p_token(self):
        # 获取token：调用get_token方法

        # token_url = "http://t-enjoy************/login"

        token_data = {"sign": self.get_sign(), "account_id": self.account_id, "from": "ios_pad",
                      'signed_at': self.get_signed_at(),
                      "phone": "******", "code": self.code, "nickname": "guozhendeng1"}
        h = requests.get(self.token_url, params=token_data)

        print
        h.text
        tokens = h.json()
        s = tokens['data']
        return s['token']
    # 获取il_id


if __name__ == '__main__':
    t = Basics("116", "123456", "********", " http://t-e***************th/login")
    print
    t.get_sign()
    print
    t.get_p_token()