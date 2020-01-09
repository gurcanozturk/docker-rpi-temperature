#!/usr/bin/python
# Minimalistic web application shows Raspberry Pi's internal temperature.
# Just run and check with your favorite browser at http://localhost:2020
#
# https://raspberrypi.stackexchange.com/a/8693


import tornado.ioloop
import tornado.web
import os


class MainHandler(tornado.web.RequestHandler):

    def getCPUtemperature(self):
        res = os.popen('vcgencmd measure_temp').readline()
        return(res.replace("temp=","").replace("'C\n",""))

    def get(self):
        self.write("Temperature: %s" % (self.getCPUtemperature()))

application = tornado.web.Application([(r"/", MainHandler), ])

if __name__ == "__main__":
    application.listen(2020)
    tornado.ioloop.IOLoop.instance().start()
