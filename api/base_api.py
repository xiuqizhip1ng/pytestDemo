import requests

class BaseAPI:
    sess = requests.Session()

    # API接口基类
    def all_send_requests(self,**kwargs):
        res = BaseAPI.sess.request(**kwargs)
        return res.json()

baseapi = BaseAPI()