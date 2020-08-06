FROM centos:7
ARG PROJECT_NAME

##
# Deps nativas
RUN yum update -y && yum clean all && \
    yum -y install \
    make autoconf automake gcc cc gcc-c++ binutils glibc \
    postgresql-devel zlib zlib-devel \
    openssl openssl-devel \
    which patch readline readline-devel \
    libyaml-devel libffi-devel pcre-devel.x86_64 \
    libtool bison iconv-devel \
    epel-release wget tar bzip2 bzip2-devel git zip \
 && yum clean all

##
# Python 3.6, pip and venv built-in
RUN mkdir -p /opt/supplai/runtime/python36 && \
    cd /tmp && \
    wget --no-check-certificate https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tgz && \
    tar -zxf Python-3.6.8.tgz && \
    cd Python-3.6.8 && \
    ./configure --prefix=/opt/supplai/runtime/python36 --with-ensurepip=install && \
    make && make altinstall

RUN cd /opt/supplai/runtime/python36/ && \
    /opt/supplai/runtime/python36/bin/pip3.6 install wheel && \
    /opt/supplai/runtime/python36/bin/python3.6 -m venv /$PROJECT_NAME

RUN ln -s /opt/supplai/runtime/python36/bin/python3.6 /opt/supplai/runtime/python36/bin/python && \
    ln -s /opt/supplai/runtime/python36/bin/pip3.6 /opt/supplai/runtime/python36/bin/pip && \
    ln -s /opt/supplai/runtime/python36/bin/easy_install-3.6 /opt/supplai/runtime/python36/bin/easy_install

##
# nvm (node, npm)
ENV NODE_VERSION v8.11.4
RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.2/install.sh | bash
RUN source ~/.nvm/nvm.sh && nvm install ${NODE_VERSION}
RUN source ~/.nvm/nvm.sh && nvm use --delete-prefix ${NODE_VERSION} && npm install -g yarn


##
#  app
RUN cd /opt/supplai && mkdir -p releases conf/$PROJECT_NAME logs/$PROJECT_NAME


##
# Redis
RUN mkdir -p /opt/supplai/redis/bin/ \
    && curl http://download.redis.io/releases/redis-2.8.12.tar.gz > redis-2.8.12.tar.gz \
    && tar zxvf redis-2.8.12.tar.gz \
    && cd redis-2.8.12 \
    && make \
    && cp src/redis-server /opt/supplai/redis/bin/ \
    && cp src/redis-cli /opt/supplai/redis/bin/ \
    && cd /opt/supplai/redis/bin/ \
    && chmod 755 *


##
# Setup ansible
RUN /opt/supplai/runtime/python36/bin/python3.6 -m venv /opt/supplai/ansible_venv \
    && source /opt/supplai/ansible_venv/bin/activate \
    && pip3.6 install ansible

RUN mkdir /etc/ansible/
RUN echo "[local]" >> /etc/ansible/hosts && \
    echo "localhost" >> /etc/ansible/hosts


ENV ANSIBLE_HOST_KEY_CHECKING false
COPY entrypoint.sh /entrypoint.sh
WORKDIR /home/$PROJECT_NAME

ENTRYPOINT ["/entrypoint.sh"]
