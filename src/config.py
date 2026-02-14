import yaml

with open("config.yaml") as f:
    config = yaml.safe_load(f)

MODEL_NAME = config["model_name"]
SOURCE_LANG = config["source"]["lang"]
SOURCE_CODE = config["source"]["code"]
TARGET_LANG = config["target"]["lang"]
TARGET_CODE = config["target"]["code"]

