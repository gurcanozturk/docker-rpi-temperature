# docker-rpi-temperature
Dockerize version of a minimalistic web app written in Python-Tornado. Original python script; https://raspberrypi.stackexchange.com/a/8693


Build it.

docker build -t pi-temp .



Run it.

docker run -d -p 2020:2020 --name pi-temp pi-temp



Check it.

http://<docker_host_ip>:2020
