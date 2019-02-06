FROM amd64/ubuntu:bionic

COPY build/* /tmp/

RUN     echo "***** Installing System Packages *****" && \
        apt-get update && \
        xargs -a /tmp/apt_install.txt apt-get install -y

RUN     echo "***** Installing PIP packages *****" && \
        pip install --upgrade pip && \
        pip2 install -r /tmp/pip_install.txt 


RUN     echo "***** Cleaning up Install ******" && \
        apt-get clean -y && \
        rm -rf \
                /tmp/* 

        ###### Installing Scripts ######
ADD    assets /app

ENTRYPOINT python /app/rabbit_consumer.py
