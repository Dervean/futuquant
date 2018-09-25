#-*-coding:utf-8-*-

from futuquant.trade.open_trade_context import *
from futuquant.quote.open_quote_context import *

class ModifyOrder(object):

    def test_us(self):
        host = '127.0.0.1'   #mac-kathy:172.18.6.144
        port = 21111
        trade_ = OpenUSTradeContext(host, port)
        ret_code_unlock_trade, ret_data_unlock_trade = trade_.unlock_trade(password='123123')
        print('unlock_trade  ret_code= %d, ret_data= %s' % (ret_code_unlock_trade, ret_data_unlock_trade))
        modify_order_op = ModifyOrderOp.CANCEL
        order_id = '5192778383921057258'
        qty = 2
        price = 214
        adjust_limit = 0
        trd_env = TrdEnv.REAL
        acc_id = 0
        acc_index = 0
        ret_code, ret_data = trade_.modify_order(modify_order_op, order_id, qty, price,adjust_limit,trd_env,acc_id,acc_index)   #, qty, price, adjust_limit=0, trd_env=TrdEnv.REAL, acc_id=acc_id
        print(ret_code)
        print(ret_data)

    def test_sh(self):

        host = '127.0.0.1'  # mac-kathy:172.18.6.144
        port = 11113
        trade_ctx_sh = OpenHKCCTradeContext(host, port)
        trade_ctx_sh.unlock_trade('123123')

        print(trade_ctx_sh.modify_order(modify_order_op= ModifyOrderOp.CANCEL, order_id= '4889665077392585169', qty = 0, price = 0.123, adjust_limit=0, trd_env=TrdEnv.REAL, acc_id=0))

    def test1(self):
        host = '172.18.7.65'
        port = 11111

        trade_hk = OpenHKTradeContext(host, port)
        trade_us = OpenUSTradeContext(host, port)
        trade_sh = OpenHKCCTradeContext(host,port)
        trade_sh_m = OpenCNTradeContext(host, port)
        trade_hk.unlock_trade('321321')
        print(trade_hk.modify_order(modify_order_op = ModifyOrderOp.CANCEL, order_id = 4889665077392585169, qty = 1000, price = 5.81, adjust_limit=0, trd_env=TrdEnv.REAL, acc_id=0))

if __name__ == '__main__':
    mo = ModifyOrder()
    mo.test1()