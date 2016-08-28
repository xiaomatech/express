#!/usr/bin/env python
# -*- coding:utf8 -*-

import requests
import simplejson as json
import hashlib
import base64
import uuid


class Sto:
    def __init__(self, partner_id):
        self.partner_id = partner_id
        self.url_prefix = 'http://japi.zto.cn/zto/api_utf8'
        self.headers = {'Accept-Charset': 'UTF-8',
                        'Content-Type': 'application/x-www-form-urlencoded'}

    def sign(self, **data):
        if type(data) is dict:
            data = json.dumps(data)
        sign_data = data + self.partner_id
        m = hashlib.md5()
        m.update(sign_data.encode("utf8"))
        return base64.encodestring(m.hexdigest())

    def uniqueid(self):
        return uuid.uuid1().get_hex()

    '''
        大头笔订单
        params = {
            "send_province": "上海",
            "send_city": "上海市",
            "send_district": "青浦区",
            "send_address": "华新镇1688号",
            "receive_province": "上海",
            "receive_city": "上海市",
            "receive_district": "青浦区",
            "receive_address": "华新镇1685号"
        }
    '''

    def traceable_mark(self, **params):
        sign = self.sign(params)
        req_data = {}
        unionCode = self.uniqueid()
        params["unionCode"] = unionCode
        req_data["msg_type"] = 'GETMARK'
        req_data['data'] = params
        req_data['data_digest'] = sign
        url = self.url_prefix + '/traceableMark'
        r = requests.post(url=url, data=req_data, headers=self.headers)
        return r.json()

    '''
        下物流单或更新物流单
        {
            "partnerCode": "130520142013234",
            "sender": {
                "name": "李琳",
                "company": "新南电子商务有限公司",
                "mobile": "13912345678",
                "phone": "021-87654321",
                "area": "上海市",
                "city": "上海市",
                "county": "青浦区",
                "address": "华新镇华志路123号",
                "zipcode": "610012"
            },
            "receiver": {
                "name": "杨逸嘉",
                "company": "逸嘉实业有限公司",
                "mobile": "13687654321",
                "phone": "010-22226789",
                "area": "四川省",
                "city": "成都市",
                "county": "武侯区",
                "address": "育德路497号",
                "zipcode": "610012"
            },
            "items": [ # items之后的都可省略
                {
                    "name": "迷你风扇",
                    "category": "电子产品",
                    "material": "金属",
                    "size": "12,11,23",
                    "weight": "0.752",
                    "unitprice": "79",
                    "quantity": "1",
                    "remark": "黑色大号"
                },
                {
                    "name": "USB3.0集线器",
                    "quantity": "1",
                    "remark": ""
                }
            ],
            "starttime": "2013-05-20 12:00:00",
            "endtime": "2013-05-20 15:00:00",
            "weight": 753,
            "size": "12,23,11",
            "quantity": 2,
            "price": 12650,
            "freight": 1000,
            "premium": 50,
            "packCharges": 100,
            "otherCharges": 0,
            "orderSum": 0,
            "collectMoneytype": "CNY",
            "collectSum": 1200,
            "remark": "请勿摔货"
        }
    '''

    def common_order(self, **params):
        sign = self.sign(params)
        req_data = {}
        req_data["msg_type"] = 'CREATE'
        req_data['data'] = params
        req_data['data_digest'] = sign
        req_data['company_id'] = self.partner_id
        url = self.url_prefix + '/commonOrder'
        r = requests.post(url=url, data=req_data, headers=self.headers)
        return r.json()

    '''
        [
            {
                "orderCode": "100000000001",
                "fieldName": "status",
                "fieldValue": "cancel",
                "reason": "客户取消订单"
            },
            {
                "orderCode": "100000000002",
                "fieldName": "status",
                "fieldValue": "cancel",
                "reason": "客户取消订单"
            }
        ]
    '''

    def cancel_order(self, **params):
        sign = self.sign(params)
        req_data = {}
        req_data["msg_type"] = 'UPDATE'
        req_data['data'] = params
        req_data['data_digest'] = sign
        req_data['company_id'] = self.partner_id
        url = self.url_prefix + '/commonOrder'
        r = requests.post(url=url, data=req_data, headers=self.headers)
        return r.json()

    '''
        查询价格和大概多久能到货
        { "sendProv": "湖北",
          "sendCity": "荆州市",
          "dispProv": "浙江",
          "dispCity": "金华市"
        }
    '''

    def price(self, **params):
        sign = self.sign(params)
        req_data = {}
        req_data["msg_type"] = 'GET_HOUR_PRICE'
        req_data['data'] = params
        req_data['data_digest'] = sign
        req_data['company_id'] = self.partner_id
        url = self.url_prefix + '/priceAndHourInterface'
        r = requests.post(url=url, data=req_data, headers=self.headers)
        return r.json()
