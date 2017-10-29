FROM alpine
MAINTAINER fananran https://github.com/fan807017570/
COPY  start.sh /opt/
RUN apk update && \
    apk upgrade && \
    apk add  python2 python2-dev py2-pip py2-yaml gcc musl-dev tzdata openntpd
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \


CMD ["/opt/start.sh"]
