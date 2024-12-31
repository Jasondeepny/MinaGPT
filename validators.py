import sys
from constants import HARDWARE_COMMAND_DICT, CONFIG_ITEMS, MODEL_MAPPING

class ConfigValidator:
    @staticmethod
    def validate_config():
        """验证配置项并返回验证后的配置字典"""
        # 检查必填项
        missing_configs = []
        for key, (value, desc) in CONFIG_ITEMS.items():
            if not value or value.isspace():
                missing_configs.append(f"{desc}({key})")
        
        if missing_configs:
            raise ValueError(
                "缺少必要的配置项:\n" + 
                "\n".join(f"- {item}" for item in missing_configs) +
                "\n请检查环境变量设置"
            )

        # 检查音箱型号是否支持
        sound_type = CONFIG_ITEMS["SOUND_TYPE"][0]
        if sound_type not in HARDWARE_COMMAND_DICT:
            supported_types = "\n".join(f"- {k}: {v}" for k, v in HARDWARE_COMMAND_DICT.items())
            raise ValueError(
                f"不支持的音箱型号: {sound_type}\n"
                f"支持的型号列表:\n{supported_types}"
            )
        
        # 检查模型是否支持
        model = CONFIG_ITEMS["MODEL"][0]
        if model not in MODEL_MAPPING:
            supported_models = "\n".join(f"- {k}: {v}" for k, v in MODEL_MAPPING.items())
            raise ValueError(
                f"不支持的模型: {model}\n"
                f"支持的模型列表:\n{supported_models}"
            )
        
        return {k: v[0] for k, v in CONFIG_ITEMS.items()}

    @staticmethod
    def get_validated_config():
        """获取经过验证的配置,如果验证失败则退出程序"""
        try:
            return ConfigValidator.validate_config()
        except ValueError as e:
            print("\033[91m错误:\033[0m")  # 红色错误提示
            print(str(e))
            sys.exit(1) 