# Flask Stock Web Service

这是一个简单的 Flask Web 服务，用于获取股票数据。该项目使用 `pysnowball` 库从 [雪球](https://xueqiu.com/) 获取股票数据。

## 安装依赖

要运行此项目，请确保已安装以下依赖：

```bash
pip install Flask
pip install flask-cors
pip install pysnowball
```

## 使用方法
首先，将 xq_a_token 替换为你的雪球 API 令牌：
```
xq_a_token = "your_xq_a_token"
```
## 运行 Flask 服务器：
```
python your_script_name.py
```
通过浏览器或其他 HTTP 客户端访问以下 URL，将 stock_code 参数替换为你要查询的股票代码（例如：SH600000）：
```
http://localhost:5000/stock?code=stock_code
```
## 示例
请求 URL：
```
http://localhost:5000/stock?code=SH600000
```
返回数据：

```json
{
  "symbol": "SH600000",
  "current": 9.11,
  "percent": 0.44,
  "chg": 0.04
}
```

## 项目结构
```
your_script_name.py：Flask 服务器主文件，包含 Web 服务的路由和处理逻辑。
stock_get.py：包含 init() 和 get() 函数，用于初始化库并获取股票数据。
```

## 许可证
本项目采用 MIT 许可证。

请将 `your_script_name.py` 替换为你的 Flask 服务器脚本名称，并在需要的地方进行相应的修改。为了避免代码块嵌套问题，请删除两个反引号 `\```` 之间的反斜杠 `\`。
