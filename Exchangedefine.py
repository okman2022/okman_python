from .commDefine import *

EXCHANGE_BUY  = "buy"
EXCHANGE_SELL = "sell"

class ExchangeNew():
    def __init__(self,key,sec):
        self.m_exchangeName =""
        self.m_klineMap     = dict()
        self.m_apikey       = key
        self.m_secretkey    = sec

    def initKLineDefine(self):
        pass

    def getKLineDefine(self, klineTime):
        kDefine = self.m_klineMap.get(klineTime, "")
        if kDefine == "":
            print("get KLine erro:",klineTime)
        return self.m_klineMap.get(klineTime, "")

    #获取深度数据
    def get_depth(self,symbol):
        pass

    #获取K线数据
    def get_kline(self, coinPair, KLineTime, limit=None):
        pass

    #获取账户信息
    def get_balance(self,acct_id = None):
        pass

    #获取点卡信息
    def get_balance_point(self):
        pass

    #下订单
    def make_order(self,tradeSide,symbol,price,amount):
        pass

    #获取当前所有未成交订单
    def get_current_order(self,symbol):
        pass

    #获取单一订单的
    def get_order_info(self,order_id,symbol=""):
        pass

    #获取最近成交的
    def get_recent_trade(self,symbol):
        pass

    #取消订单
    def cancel_order(self,order_id,symbol = ""):
        pass

    #获取全部ticker
    def get_ticker(self):
        pass

    #获取特定的ticker
    def get_specific_ticker(self,symbol):
        pass

    #获取指定币种的交易规则
    def get_symbol_info(self,symbol):
        pass
