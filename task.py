# -*- coding: utf-8 -*-
"""
Assignment 1, week 3

Created at 2020-11-18
Current project: signal-interpreter-server


"""


@task
def style(_):
    cmd = f"pycodestyle {SRC_DIR} --ignore=E501"
subprocess.call(cmd, shell=True)