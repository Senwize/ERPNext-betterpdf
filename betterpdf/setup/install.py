import subprocess
import os
app_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../")


class NoYarnException(Exception):
  def __init__(self, message):
    super().__init__("Cannot install because yarn is not installed: " + message)


class NoNodeException(Exception):
  def __init__(self, message):
    super().__init__("Cannot install because node is not installed: " + message)


class YarnException(Exception):
  pass


def check_node():
  result = subprocess.run(["node", "--version"],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  if result.returncode > 0:
    raise NoNodeException(result.stdout + result.stderr)


def check_yarn():
  result = subprocess.run(["yarn", "--version"],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  if result.returncode > 0:
    raise NoYarnException(result.stdout + result.stderr)


def before_install():
  print("Checking node")
  check_node()

  print("Checking yarn")
  check_yarn()

  print("Install yarn dependencies for html2pdf")
  dep_result = subprocess.run(
      ["yarn", "--frozen-lockfile"], cwd=os.path.join(app_path, "html2pdf"), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  if dep_result.returncode > 0:
    raise YarnException(str(dep_result.stdout))


def after_install():
  pass
