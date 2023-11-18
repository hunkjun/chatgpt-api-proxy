### 为什么要写这个程序

- 最近封IP有些严重，hk区域所有ip基本被淹没了

- 参考 https://github.com/x-dr/chatgptProxyAPI 可以实现使用cloudflare 搭建免费的 OpenAI api代理 。

但是！！！！最近cloudfare的出口ip进Openai的**黑名单**了, 测试发现此项目的**中转功能**已失效.

```
Sorry, you have been blocked
You are unable to access api.openai.com
Why have I been blocked?
```

为此实现了一个Python版本的openai/chatgpt中转，最小成本、最简单方式的实现代理。

支持流式输出。

备注: 需要有一个其他区域的主机，可以找云厂商开一个最小配置的主机，成本在30-40元/月.

### 如果对你有帮助, 可通过如下方式来表达

- 给仓库来个Star⭐️⭐️⭐️⭐️⭐️, 让更多人看到这个项目。
- 或者鼓励一下

<p align="center">
  <img src="./images/zanshangma.jpg" width="200" height="200">
</p>


### 架构

```shell

用户  --> 应用/配置为代理的地址 --> 新增其他地区主机/部署ApiProxy代理 --> OpenAi 

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

- 具备多年运维实战经验，包括网络攻击防范、网络链路优化以及网站功能提升。
- 无论您遇到什么问题，都欢迎与联系，我将乐意提供帮助！「有偿或无偿」
- QQ&&WX：1101292065
- Jun

