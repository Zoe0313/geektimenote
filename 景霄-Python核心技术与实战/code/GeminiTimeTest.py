import time
import datetime
current_time = datetime.datetime.now()
print(int(datetime.datetime.timestamp(current_time)*1000))
print(int(time.mktime(current_time.timetuple())*1000))

"""
知识点很多，整理一下。
1. 非对称加密：
    加密：公钥加密，私钥解密；
    签名：私钥签名，公钥验签。
2. hmac.new(key, str, digestmod)
    key是密钥；str是欲加密的串；digestmod是hmac加密算法
3. 最后一句打印语句可以写成如下看着更清晰：
    print(json.dumps(new_order, indent=4))
4. 在草稿纸上画出交互拓扑图
5. 如何设计符合RESTful特征的API
6. Keep-Alive: timeout=5, max=100

思考题：
测试了一下timestamp效果，代码如下：
import time
import datetime
current_time = datetime.datetime.now()
print(int(datetime.datetime.timestamp(current_time)*1000))
print(int(time.mktime(current_time.timetuple())*1000))

同样都是时间戳，timestamp是带毫秒的，具备单调递增、加密混乱的特质。
文中有句话是这么说的："当某个后来请求的nonce比上一个成功收到的请求的nonce小或者相等的时候，Gemini便会拒绝这次请求"。
说明Gemini不希望http请求在一秒内发生多次。应该是反爬用的吧~
用timestamp是可以精确到毫秒的，意味着每毫秒可以请求发送的nonce都不一样。

另外，作为taker第二次运行该代码就报出下面的错：
{
    "result": "error",
    "reason": "InsufficientFunds",
    "message": "Failed to place buy order on symbol 'BTCUSD' for price $3,633.00 and quantity 5 BTC due to insufficient funds"
}
"""
