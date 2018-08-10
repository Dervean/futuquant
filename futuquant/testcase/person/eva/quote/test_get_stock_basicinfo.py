#-*-coding:utf-8-*-

from futuquant import *
import pandas

class GetStockBasicinfo(object):
    #获取股票信息 get_stock_basicinfo

    def __init__(self):
        pandas.set_option('max_columns', 100)
        pandas.set_option('display.width', 1000)
    #     # 启动协议加密
    #     SysConfig.set_init_rsa_file('E:/test/testing/conn_key.txt')
    #     SysConfig.enable_proto_encrypt(True)

    def test1(self):
        quote_ctx = OpenQuoteContext(host='127.0.0.1',port=11111)
        market = Market.US
        stock_type = SecurityType.STOCK
        ret_code,ret_data = quote_ctx.get_stock_basicinfo(market,stock_type)
        print(ret_code)
        print(ret_data)
        # for data in ret_data.iterrows():
        #     print(data)

        # stock_codes = ret_data['code'].tolist()
        # print( 'HK.00001'in stock_codes)
        quote_ctx.close()




if __name__ == '__main__':
    gsb = GetStockBasicinfo()
    gsb.test1()