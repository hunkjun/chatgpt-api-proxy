### 为什么要写这个程序

参考 https://github.com/x-dr/chatgptProxyAPI 可以实现使用cloudflare 搭建免费的 OpenAI api代理 。

但是最近cloudfare的出口ip进Openai的黑名单了, 还是无法解决网络无法访问问题.

```
Sorry, you have been blocked
You are unable to access api.openai.com
Why have I been blocked?
```

为此实现了一个Python版本，本地部署的代理。支持流式输出。

## 安装&运行

## 测试

```shell
curl http://127.0.0.1/v1/chat/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer sk-YouKey"   \
-d '{
    "model": "gpt-3.5-turbo",
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

