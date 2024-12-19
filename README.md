# MINAGPT

## 简单介绍

本项目利用了OpenAI官方API的原生流式传输对话方式，无需等待，即刻对话！

_注意：本项目因采用了流式传输，暂时不支持LX04、L05B和L05C型号。如您的音箱是该型号，请使用[xiaogpt](https://github.com/yihong0618/xiaogpt)。_

## 使用技巧
1. 运行过程中，可用“打开/关闭高级对话"控制是否打开ChatGPT。
2. 当ChatGPT正在回答问题时，可用“闭嘴”或“停止”终止回答。
3. 可随时提问新的问题打断ChatGPT的回答。

## 部署
方法一：使用 Docker Compose (推荐)
# 1. 首先配置.env文件
  在.env文件中填写小米账号、密码、[API Key](https://platform.openai.com/account/api-keys)和音箱型号
  *** (项目代码使用DeepSeekAI API 完全适配openAPI库，需要使用openAI的自行修改,同时导入tiktoken库，通用模型 tokenizer使用transformers库)
  cp .env.example .env
  vim .env  # 编辑配置信息

# 2. 构建并启动服务
  docker-compose up -d

# 查看日志
  docker-compose logs -f

# 停止服务
  docker-compose down


方法二：直接使用 Docker
# 1. 构建镜像
  docker build -t migpt .

# 2. 运行容器
  docker run -d \
  --name migpt \
  --restart unless-stopped \
  -e MI_USER="你的小米账号" \
  -e MI_PASS="你的小米密码" \
  -e OPENAI_API_KEY="你的OpenAI API密钥" \
  -e SOUND_TYPE="你的音箱型号" \
  -v $(pwd)/data:/app/data \
  migpt

# 查看日志
  docker logs -f migpt


## 致谢引用
- @[yihong0618](https://github.com/yihong0618) 的 [xiaogpt](https://github.com/yihong0618/xiaogpt)
- @[acheong08](https://github.com/acheong08) 的 [ChatGPT](https://github.com/acheong08/ChatGPT)
- @[Yonsm](https://github.com/Yonsm) 的 [MiService](https://github.com/Yonsm/MiService)


