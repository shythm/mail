FROM ubuntu:18.04
ENV LC_ALL=C.UTF-8
EXPOSE 80 5000

RUN mkdir app && cd app

WORKDIR /app

# apt-get update&upgrade...
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils

# python install & version settings
RUN apt-get -y install python3.7 && update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1
# python pip & install
RUN apt-get -y install python3-pip
RUN pip3 install flask && pip3 install requests && pip3 install beautifulsoup4 && pip3 install lxml

# install git
RUN apt-get -y install git

# clone git & run flask app
RUN git clone https://github.com/raculus/mail.git && cd mail