import pysnowball as ball
import snowtoken

def init():
    settoken = 'xq_a_token=' + snowtoken.xq_a_token
    ball.set_token(settoken)

def get(stock_code):
    result = ball.quotec(stock_code)
    data = result['data'][0]

    price_data = {
        'symbol': data['symbol'],
        'current': data['current'],
        'percent': data['percent'],
        'chg': data['chg']
        # 'open': data['open'],
        # 'last_close': data['last_close'],
        # 'high': data['high'],
        # 'low': data['low'],
        # 'avg_price': data['avg_price'],
        # 'current_year_percent': data['current_year_percent']
    }

    print(price_data)
    return price_data

init()
get('SH600000')
