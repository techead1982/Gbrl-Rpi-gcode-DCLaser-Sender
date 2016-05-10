import queue
import threading
import serial
import sys
import glob
import time


class SerialClass(threading.Thread):

    def __init__(self, write_queue, command_queue, reply_queue):
        super(SerialClass, self).__init__init()
        self.serial_setup(None, 115200, None, None, None, None)
        self.rq = reply_queue
        self.cq = command_queue
        self.wq = write_queue
        self.testqueue = queue.Queue()
        self.grbl_version = "Grbl Not Detected"
        self.ser = serial.Serial()
        self.portList = []
        # threading.Thread.__init__(self)

    def run(self):
        self.autoports()
        self.ser.open()
        while self.ser.is_open:
            if self.cq.not_empty:
                textout = self.cq.get()
                self.ser.write(bytearray(textout, 'ascii'))
                time.sleep(0.2)
            while self.wq.not_empty:
                if self.cq.not_empty:

                    # switch{}
                        # case up;
                            # write (gcode+[2])
                        # case down;


                    textout = self.cq.get()
                    self.ser.write(bytearray(textout, 'ascii'))
                    time.sleep(0.2)
                    self.wq.empty()
                else:
                    textout = self.wq.get()
                    self.ser.write(bytearray(textout, 'ascii'))
                    time.sleep(0.2)

    def serial_setup(self, comport, baud_rate, byte_size, parity_bits, stop_bits, time_out):  # port setup

        self.ser._port = comport

        if baud_rate is not None:
            self.ser._baudrate = baud_rate

        if byte_size is not None:
            self.ser._bytesize = byte_size

        if parity_bits is not None:
            self.ser._parity = parity_bits

        if stop_bits is not None:
            self.ser._stopbits = stop_bits

        if time_out is not None:
            self.ser._timeout = time_out

        # def Stored_serial_Setup(self):
        # with open('SerialConfig.py','r',encoding='ascii') as f:

    def autoports(self):
        self.portList = self.serial_ports()
        self.auto_find_grbl()

    def serial_ports(self):  # Finds open serial ports on Computer
        # print("find ports")
        # print(sys.platform)
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
            self.serial_setup(port, self.ser.baudrate, None, None, None, None)

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
        self.portList = result
        return result

    def auto_find_grbl(self):  # finds what port grbl is on and sets it to serial setup
        available_ports = self.serial_ports()
        # print("port start")
        i = 0
        p = ''
        for port in available_ports:
            # print(port)
            self.serial_setup(port, self.ser.baudrate, None, None, None, None)
            try:
                self.ser.open()

                time.sleep(3)
                # test.write(self,'$I')

                while self.ser.inWaiting():
                    data = self.ser.readline().strip().decode('ascii')
                    # print(data)
                    if data.find('Grbl') < 0:
                        # print("No data")
                        u = 1
                    else:
                        self.grbl_version = data
                        # print(data)
                        i = 1
                        p = port
                        break
                self.ser.close()

            except (OSError, serial.SerialException):
                # print("dam")
                pass
            if i == 1:
                break