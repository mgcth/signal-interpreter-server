import subprocess
from invoke import task

SRC_DIR = "signal_interpreter_server"
TEST_DIR = "tests/unit"
COV_PATH = ".coveragerc"

@task
def style(_):
    cmd = f"pycodestyle {SRC_DIR} --ignore=E501"
    subprocess.call(cmd, shell=True)

@task
def lint(_):
    cmd =  f"pylint {SRC_DIR}"
    subprocess.call(cmd, shell=True)

@task
def unit_test(_):
    cmd = f"python -m pytest {TEST_DIR} --cov {SRC_DIR} --cov-config={COV_PATH}"
    subprocess.call(cmd, shell=True)