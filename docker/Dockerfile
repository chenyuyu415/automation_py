FROM ubuntu:22.04
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

# Only for China, change apt sources list
RUN sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list

# Ignore timezone and apt update
ENV DEBIAN_FRONTEND=noninteractive
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get upgrade -y

# Install required packages
RUN apt-get install -y \
apt-utils \
vim \
git \
iputils-ping \
traceroute \
net-tools \
telnet \
curl \
wget \
zip \
python3 \
python3-pip \
tftp-hpa \
automake \
libtool \
libsnmp-dev \
bison \
make \
gcc \
flex \
libglib2.0-dev \
libfl-dev \
libperl-dev

# Set default python as python3
RUN ln -s /usr/bin/python3.10 /usr/bin/python

# Install netsnmp
RUN wget https://sourceforge.net/projects/net-snmp/files/net-snmp/5.9.2-pre-releases/net-snmp-5.9.2.pre1.tar.gz/download -O /tmp/net-snmp-5.9.2.pre1.tar.gz && \
tar zxf /tmp/net-snmp-5.9.2.pre1.tar.gz -C /tmp/ && \
rm /tmp/net-snmp-5.9.2.pre1.tar.gz && \
cd /tmp/net-snmp-5.9.2.pre1 && \
./configure --with-default-snmp-version="2" \
--with-sys-contact="@@no.where" --with-sys-location="Unknown" \
--with-logfile="/var/log/snmpd.log" --with-persistent-directory="/var/net-snmp" && \
make && \
make install && \
cd /tmp/net-snmp-5.9.2.pre1/python/ && \
python setup.py install && \
cd && \
rm -rf /tmp/net-snmp-5.9.2.pre1
#cp /usr/local/lib/libnetsnmp.so.40 /usr/lib/

# Install docsis
RUN cd /tmp && \
git clone https://github.com/rlaager/docsis.git && \
cd docsis && \
./autogen.sh && \
./configure && \
make && \
make install && \
cd &&\
rm -rf /tmp/docsis

# Install chrome and chromedriver
RUN echo "nameserver 8.8.8.8" > /etc/resolv.conf && \
wget http://www.linuxidc.com/files/repo/google-chrome.list -P /etc/apt/sources.list.d/ && \
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub  | apt-key add - && \
apt-get update && apt-get -y install google-chrome-stable

# Install chromedriver
RUN LATEST=$(wget -q -O - http://chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
wget https://chromedriver.storage.googleapis.com/$LATEST/chromedriver_linux64.zip -O /tmp/chromedriver_linux64.zip && \
unzip /tmp/chromedriver_linux64.zip -d /tmp/ && \
chmod +x /tmp/chromedriver && \
mv /tmp/chromedriver /usr/bin/ && \
rm /tmp/chromedriver_linux64.zip

# Only for China, change pip source
RUN pip config set global.index-url https://pypi.mirrors.ustc.edu.cn/simple/

# Add python library
COPY requirements.txt /tmp/

# Install python library
RUN pip install -r /tmp/requirements.txt && rm /tmp/requirements.txt
