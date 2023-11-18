### 为什么要写这个程序

参考 https://github.com/x-dr/chatgptProxyAPI 可以实现使用cloudflare 搭建免费的 OpenAI api代理 。

但是！！！！最近cloudfare的出口ip进Openai的黑名单了, 中转已失效.

```
Sorry, you have been blocked
You are unable to access api.openai.com
Why have I been blocked?
```

为此实现了一个Python版本，最小成本、最简单的实现的代理功能。

支持流式输出。

### 如果对你有帮助, 可通过如下方式来表达

- 给仓库来个Star⭐️⭐️⭐️⭐️⭐️, 让更多人看到
- 或者鼓励一下

<p align="center">
  <img src="./images/zanshangma.jpg" width="200" height="200">
</p>


### 架构

```shell

用户  --> 应用/配置为代理的地址 --> 其他地区主机/部署ApiProxy --> OpenAi 

```

### 安装&运行

```shell
# pip3 freeze > requirements.txt
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

python3 app.py

```

### 测试

```shell
curl http://127.0.0.1/v1/chat/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer sk-YOUROPENAIKEY"   \
-d '{
    "model": "gpt-3.5-turbo",
    "stream": true,
    "messages": [
      {
        "role": "system",
        "content": "You are a helper."
      },
      {
        "role": "user",
        "content": "Hello."
      }
    ]
  }'
```

## 结果

```shell
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Hello! How can I assist you today?"
      },
      "finish_reason": "stop"
    }
```

## 广告位

- 多年运维工作经验, 有处理网络攻击、网络链路优化、网站功能优化等问题排查经验，如有需要，欢迎联系!
- Jun, QQ&&WX:1101292065

