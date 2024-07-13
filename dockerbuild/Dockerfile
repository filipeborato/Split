FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y build-essential
# This will install Python, pip, pip3, and pip3.6.

RUN curl https://bootstrap.pypa.io/ez_setup.py -o - | python3.6 && python3.6 -m easy_install pip
RUN apt-get update
RUN apt-get install -y python3.6-venv

# Inorder to run pip3.6, run it the following way `python3.6 -m pip`
# Update Python & Install wheel
RUN python3.6 -m pip install pip --upgrade
RUN python3.6 -m pip install wheel

# TO Run
# docker build -t ubuntu1804