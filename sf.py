#!/usr/bin/env python
# -*- coding:utf8 -*-

import requests

class Sf:
    def __init__(self, appid, appkey):
        self.header = {"Content-Type": "application/json"}
        self.url_prefix = 'https://open-sbox.sf-express.com'
        self.appid = appid
        self.appkey = appkey

    def apply_access_token(self, transMessageId):
        data = {
            'head': {
                'transType': '301',
                'transMessageId': transMessageId,
            },
            'body': {},
        }
        url = self.url_prefix + '/public/v1.0/security/access_token/sf_appid/%s/sf_appkey/%s' % (
            self.appid, self.appkey)
        r = requests.post(url=url, data=data, headers=self.header)
        return r.json()

    def refresh_access_token(self, kwargs):
        data = {
            'head': {
                'transType': '302',
                'transMessageId': kwargs['transMessageId'],
            },
            'body': {},
        }
        url = self.url_prefix + '/public/v1.0/security/refresh_token/access_token/%s/refresh_token/%s/sf_appid/%s/sf_appkey/%s' % (
            kwargs['access_token'], kwargs['refresh_token'], self.appid,
            self.appkey)
        r = requests.post(url=url, data=data, headers=self.header)
        return r.json()

    def access_token(self, transMessageId):
        data = {
            'head': {
                'transType': '300',
                'transMessageId': transMessageId,
            },
            'body': {},
        }
        url = self.url_prefix + '/public/v1.0/security/access_token/query/sf_appid/%s/sf_appkey/%s' % (
            self.appid, self.appkey)
        r = requests.post(url=url, data=data, headers=self.header)
        return r.json()

    def filter_order(self, **kwargs):
        url = self.url_prefix + '/rest/v1.0/filter/access_token/%s/sf_appid/%s/sf_appkey/%s' % (
            kwargs['access_token'], self.appid, self.appkey)
        data = {
            'head': {
                'transType': '204',
                'transMessageId': kwargs['transMessageId'],
            },
            'body': {
                'filterType': kwargs['filterType']
                if 'filterType' in kwargs else '1',
                'consigneeAddress': kwargs['consigneeAddress'],
                'consigneeProvince': kwargs['consigneeProvince'],
                'consigneeCity': kwargs['consigneeCity'],
                'consigneeCounty': kwargs['consigneeCounty'],
                'consigneeCountry': kwargs['consigneeCountry']
                if 'consigneeCountry' in kwargs else '中国',
            },
        }
        r = requests.post(url=url, data=data, headers=self.header)
        return r.json()

    def create_order(self, **kwargs):
        url = self.url_prefix + '/rest/v1.0/order/access_token/%s/sf_appid/%s/sf_appkey/%s' % (
            kwargs['access_token'], self.appid, self.appkey)
        data = {
            'head': {
                'transType': '200',
                'transMessageId': kwargs['transMessageId'],
            },
            'body': {
                'orderId': kwargs['orderId'],
                'expressType': kwargs['expressType'],
                'payMethod': kwargs['payMethod'],
                'custId': kwargs['custId'],
                # 'isDocall': kwargs['isDocall'] if 'isDocall' in kwargs else '1',
                # 'isGenBillno': kwargs['isGenBillno'] if 'isGenBillno' in kwargs else '1',
                # 'isGenEletricPic': kwargs['isGenEletricPic'] if 'isGenEletricPic' in kwargs else '1',
                # 'payArea': kwargs['payArea'] if 'payArea' in kwargs else '',
                # 'sendStartTime': kwargs['sendStartTime'] if 'sendStartTime' in kwargs else '',
                # 'needReturnTrackingNo': kwargs['needReturnTrackingNo'] if 'needReturnTrackingNo' in kwargs else '',
                # 'remark': kwargs['remark'] if 'remark' in kwargs else '',
                'deliverInfo': {
                    'company': kwargs['deliverInfo']['company'] if 'company' in kwargs else '',
                    'contact': kwargs['deliverInfo']['contact'],
                    'tel': kwargs['deliverInfo']['tel'],
                    'province': kwargs['deliverInfo']['province'],
                    'city': kwargs['deliverInfo']['city'],
                    'county': kwargs['deliverInfo']['county'],
                    'address': kwargs['deliverInfo']['address']
                },
                'consigneeInfo': {
                    'company': kwargs['consigneeInfo']['company'],
                    'contact': kwargs['consigneeInfo']['contact'],
                    'tel': kwargs['consigneeInfo']['tel'],
                    'province': kwargs['consigneeInfo']['province'],
                    'city': kwargs['consigneeInfo']['city'],
                    'county': kwargs['consigneeInfo']['county'],
                    'address': kwargs['consigneeInfo']['address'],
                    # 'shipperCode': kwargs['consigneeInfo']['shipperCode'] if 'mobile' in kwargs else '',
                    # 'mobile': kwargs['consigneeInfo']['mobile'] if 'mobile' in kwargs else '',
                },
                'cargoInfo': {
                    'cargo': kwargs['cargoInfo']['cargo'],

                    # 'parcelQuantity': kwargs['cargoInfo']['parcelQuantity'] if 'parcelQuantity' in kwargs else '',
                    # 'cargoCount': kwargs['cargoInfo']['cargoCount'] if 'cargoCount' in kwargs else '',
                    # 'cargoUnit': kwargs['cargoInfo']['cargoUnit'] if 'cargoUnit' in kwargs else '',
                    # 'cargoWeight': kwargs['cargoInfo']['cargoWeight'] if 'cargoWeight' in kwargs else '',
                    # 'cargoAmount': kwargs['cargoInfo']['cargoAmount'] if 'cargoAmount' in kwargs else '',
                    # 'cargoTotalWeight': kwargs['cargoInfo']['cargoTotalWeight'] if 'cargoTotalWeight' in kwargs else '',
                },
                # 'addedServices': {
                #     'COD': kwargs['addedServices']['COD'] if 'COD' in kwargs else '',
                #     'CUSTID': kwargs['addedServices']['CUSTID'] if 'CUSTID' in kwargs else '',
                #     'INSURE': kwargs['addedServices']['INSURE'] if 'INSURE' in kwargs else '',
                #     'MSG': kwargs['addedServices']['MSG'] if 'MSG' in kwargs else '',
                #     'PKFREE': kwargs['addedServices']['PKFREE'] if 'PKFREE' in kwargs else '',
                #     'SINSURE': kwargs['addedServices']['SINSURE'] if 'SINSURE' in kwargs else '',
                #     'SDELIVERY': kwargs['addedServices']['SDELIVERY'] if 'SDELIVERY' in kwargs else '',
                #     'SADDSERVICE': kwargs['addedServices']['SADDSERVICE'] if 'SADDSERVICE' in kwargs else '',
                # }
            }
        }

        r = requests.post(url=url, data=data, headers=self.header)
        return r.json()

    def query_result(self, **kwargs):
        url = self.url_prefix + '/rest/v1.0/order/query/access_token/%s/sf_appid/%s/sf_appkey/%s' % (
            kwargs['access_token'], self.appid, self.appkey)
        data = {
            'head': {
                'transType': '203',
                'transMessageId': kwargs['transMessageId'],
            },
            'body': {
                'orderId': kwargs['orderId'],
            },
        }

        r = requests.post(url=url, data=data, headers=self.header)
        return r.json()

    def route_query(self, **kwargs):
        url = self.url_prefix + '/rest/v1.0/route/query/access_token/%s/sf_appid/%s/sf_appkey/%s' % (
            kwargs['access_token'], self.appid, self.appkey)
        data = {
            'head': {
                'transType': '501',
                'transMessageId': kwargs['transMessageId'],
            },
            'body': {
                'trackingType': kwargs['trackingType'],
                'trackingNumber': ','.join(kwargs['trackingNumber']),
                'methodType': kwargs['methodType']
                if 'methodType' in kwargs else '1',
            },
        }

        r = requests.post(url=url, data=data, headers=self.header)
        return r.json()

    def route_query_inc(self, **kwargs):
        url = self.url_prefix + '/rest/v1.0/route/inc/query/access_token/%s/sf_appid/%s/sf_appkey/%s' % (
            kwargs['access_token'], self.appid, self.appkey)
        data = {
            'head': {
                'transType': '504',
                'transMessageId': kwargs['transMessageId'],
            },
            'body': {
                'orderId': kwargs['orderId'],
            },
        }

        r = requests.post(url=url, data=data, headers=self.header)
        return r.json()

    def access_order_img(self, **kwargs):
        url = self.url_prefix + '/rest/v1.0/waybill/image/access_token/%s/sf_appid/%s/sf_appkey/%s' % (
            kwargs['access_token'], self.appid, self.appkey)
        data = {
            'head': {
                'transType': '205',
                'transMessageId': kwargs['transMessageId'],
            },
            'body': {
                'orderId': kwargs['orderId'],
            },
        }

        r = requests.post(url=url, data=data, headers=self.header)
        return r.json()
