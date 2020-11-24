# -*- coding: utf-8 -*-
"""
Assignment 1, week 3

Created at 2020-11-18
Current project: signal-interpreter-server


"""
from invoke import task
import subprocess
import os

CURR_DIR = r"./"
SRC_DIR = os.path.join(CURR_DIR, "signal_interpreter_server")
TEST_DIR = os.path.join(CURR_DIR, "tests")


@task
def style(_):
    """
    Make sure to fix all style issues so that it follows the PEP 8 to 100%
    :param _:
    :return:
    """
    toIgnore = "E501"
    cmd = f"pycodestyle {SRC_DIR} --ignore={toIgnore}"
    subprocess.call(cmd, shell=True)


@task
def lint(_):
    # SRC_DIR = r"*.py"
    cmd = f"pylint {SRC_DIR}"
    subprocess.call(cmd, shell=True)
