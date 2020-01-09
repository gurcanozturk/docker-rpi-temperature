FROM armhf/alpine
MAINTAINER gurcan@gurcanozturk.com

COPY temperature.py /temperature.py

RUN apk update && \
	apk --no-cache add python py-tornado && \
	chmod +x /temperature.py && \
	rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /var/cache/distfiles/*

EXPOSE 2020

CMD [ "python", "./temperature.py" ]
