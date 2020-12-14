import subprocess
from invoke import task

SRC_DIR = "signal_interpreter_server"
TEST_DIR = "tests"
UNIT_DIR = "tests/unit"
INTEGRATION_DIR = "tests/integration"
COV_PATH = ".coveragerc"

@task
def style(_):
    cmd = f"pycodestyle {SRC_DIR} --ignore=E501"
    subprocess.call(cmd, shell=True)

@task
def style_test(_):
    cmd = f"pycodestyle {TEST_DIR} --ignore=E501"
    subprocess.call(cmd, shell=True)

@task
def lint(_):
    cmd = f"pylint {SRC_DIR}"
    subprocess.call(cmd, shell=True)

@task
def lint_test(_):
    cmd =  f"pylint {TEST_DIR}"
    subprocess.call(cmd, shell=True)

@task
def unit_test(_):
    cmd = f"python -m pytest {UNIT_DIR} --cov {SRC_DIR} --cov-config={COV_PATH}"
    subprocess.call(cmd, shell=True)

@task
def integration_test(_):
    cmd = f"python -m pytest {INTEGRATION_DIR} --cov {SRC_DIR} --cov-config={COV_PATH}  --cov-fail-under=75"
    subprocess.call(cmd, shell=True)