import os

# API 相关常量
LATEST_ASK_API = "https://userprofile.mina.mi.com/device_profile/v2/conversation?source=dialogu&hardware={hardware}&timestamp={timestamp}&limit=2"
COOKIE_TEMPLATE = "deviceId={device_id}; serviceToken={service_token}; userId={user_id}"

# 硬件型号映射
HARDWARE_COMMAND_DICT = {
    "LX06": "5-1",  # 小爱音箱Pro（黑色）
    "L05B": "5-3",  # 小爱音箱Play
    "S12A": "5-1",  # 小爱音箱
    "LX01": "5-1",  # 小爱音箱mini
    "L06A": "5-1",  # 小爱音箱
    "LX04": "5-1",  # 小爱触屏音箱
    "L05C": "5-3",  # 小爱音箱Play增强版
    "L17A": "7-3",  # 小爱音箱Sound Pro
    "X08E": "7-3",  # 红米小爱触屏音箱Pro
    "LX05A": "5-1", # 小爱音箱遥控版（黑色）
    "LX5A": "5-1",  # 小爱音箱遥控版（黑色）
    "L15A": "7-3",  # 小爱 AI二代
    # ...add more here
}

# 配置项
CONFIG_ITEMS = {
    "MI_USER": (os.getenv("MI_USER", ""), "小米账号"),
    "MI_PASS": (os.getenv("MI_PASS", ""), "小米账号密码"),
    "OPENAI_API_KEY": (os.getenv("OPENAI_API_KEY", ""), "OpenAI API Key"),
    "SOUND_TYPE": (os.getenv("SOUND_TYPE", ""), "音箱型号")
}

# GPT相关配置
SWITCH = True  # 是否开启chatgpt回答
PROMPT = "请尽量在300字以内回答，第一句一定不要超过10个汉字或5个单词，并且请快速生成前几句话"  # 限制回答字数在100以内 