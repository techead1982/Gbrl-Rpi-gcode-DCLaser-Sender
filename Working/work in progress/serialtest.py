import queue
import threading
import serial
import sys
import glob
import time
import SerialClass


class Serailset(threading.Thread):

    def __init__(self, write_queue, command_queue, reply_queue, gbVersion):

        self.rq = reply_queue.Queue()
        self.rq.start()
        self.cq = command_queue.Queue() #"command_queue"
        self.cq.start()
        self.wq = write_queue.Queue()
        self.rq.start()


        self.grbl_version_q = gbVersion
        self.ser = serial.Serial()
        self.portlist = []# self.qtest = queue.Queue()
        self.grbl_version_q.put("Grbl Not Detected")

    def SerailQ(self):
        self.rq.put(5)
        self.val = self.rq.get()
        print(self.val)




    def Serailrun(self):
        # Getting Ports
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i+1)for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')
        result = []
        for port in ports:
            self.ser.port = port
            self.ser.baudrate = 9600

            # print("after serial")
            try:
                # print(port)
                # print("Yes1")
                self.ser.open()
                # print("Yes2")
                self.ser.close()
                # print("Yes3")

                result.append(port)
            except(OSError, serial.SerialException):
                pass
        self.portlist = result

