FROM continuumio/miniconda3

USER root
RUN  apt-get update && apt install libgl1-mesa-glx --yes

RUN mkdir /home/distributed
RUN mkdir /home/distributed/api
COPY requirements.txt home/distributed

RUN conda update conda
RUN conda config --append channels conda-forge
RUN conda install python=3.6

WORKDIR /home/distributed