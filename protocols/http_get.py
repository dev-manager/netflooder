from threading import Thread
from requests import get
from random import choice


class Get:
    def __init__(self, dst):
        self.dst = dst
        self.is_running = False
        self.result = 400
        self.thread = None
    
    def run(self, log_f, p_bar):
        data = get(self.dst, header={"User-Agent": choice(["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.115 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.115 Safari/537.36"])[0]})
        self.result = data.status_code
        log_f(f"상태 코드 {self.result}, {self.intercount}개의 패킷을 전송했습니다")
        p_bar.setProperty("value", limit // self.intercount)
        self.intercount += 1

    def threadf(self, log_f, p_bar, limit):
        while self.is_running:
            self.run(log_f, p_bar)
            if self.intercount > limit:
                return
    
    def start(self, log_f, p_bar, limit):
        self.is_running = True
        self.thread = Thread(target=self.threadf, args=[log_f, p_bar, limit])
