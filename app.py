from flask import Flask, request, jsonify
from flask_cors import CORS
import stock_get

app = Flask(__name__)
CORS(app)  # 启用 CORS

stock_get.init()

@app.route('/')
def hello():
    return 'Hello, Flask Web Service!'

@app.route('/stock', methods=['GET'])
def get_stock():
    stock_code = request.args.get('code')
    if stock_code:
        stock_data = stock_get.get(stock_code)
        return jsonify(stock_data)
    else:
        return jsonify({'error': 'No stock code provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
