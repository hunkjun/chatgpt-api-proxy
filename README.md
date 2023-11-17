### 为什么要写这个程序

参考 https://github.com/x-dr/chatgptProxyAPI 可以实现使用cloudflare 搭建免费的 OpenAI api代理 。

但是最近cloudfare的出口ip进Openai的黑名单了, 还是无法解决网络无法访问问题.

```
Sorry, you have been blocked
You are unable to access api.openai.com
Why have I been blocked?
```

为此实现了一个Python版本，本地部署的代理。支持流式输出。

## 架构

```mermaid

用户  --> 应用(your domain) --> Api Proxy ---> OpenAi 

```

## 安装&运行

```shell
# pip3 freeze > requirements.txt
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

python3 app.py

```

## 测试

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