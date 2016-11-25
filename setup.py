import time

from setuptools import find_packages

from distutils.core import setup

patch_level = int(time.time())

ver = "0.1.9" + str(patch_level)[3:]

setup(
  name = 'slackbot_cttc',
  packages = find_packages(),
  version = ver,
  description = 'Python Code for Slackbot Tech Training Demo',
  author = 'CapTech Ventures',
  author_email = 'wmills@captechventures.com',
  url = 'https://github.com/wray/slack_cttc',
  download_url = 'https://github.com/wray/slack_cttc/tarball/'+ver,
  keywords = ['slackbot', 'RPi', 'AWS'],
  classifiers = [],
)
