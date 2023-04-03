# Flask 股票 Web 服务

基于 Flask 实现的股票 Web 服务，使用 [pysnowball](https://github.com/lierabbit/pysnowball) 获取实时股票数据。

## 使用方法

1. 安装依赖：

pip install flask flask-cors pysnowball


1. 创建一个名为 `snowtoken.py` 的文件，包含以下内容：

```python
xq_a_token = 'your_xq_a_token_here'
将其中的 your_xq_a_token_here 替换为你的雪球 token。
```
