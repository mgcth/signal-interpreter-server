# -*- coding: utf-8 -*-
"""
DESCRIPTION

Created by CWENG at 2020-11-04
Current project: VeldiPython


"""
import logging.config
import os
import yaml


PATH = "\\".join(os.path.dirname(__file__).split("\\")[0:-1])
LOG_CONFIG_PATH = PATH + "\\cfg\\log_config.yaml"
# LOG_CONFIG_PATH = "..\\cfg\\log_config.yaml"
# print(LOG_CONFIG_PATH)


with open(LOG_CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)
