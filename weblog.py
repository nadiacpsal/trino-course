import json
import random
import time

user_set = [
'John',
'XiaoMing',
'Cici',
'Tom',
'Machael',
'Zheng Hu',
'Zark',
'Tim',
'Andrew',
'Pick',
'Sean',
'Luke',
'Chunck'
]

web_set = [
'https://google.com',
'https://facebook.com?id=1',
'https://tmall.com',
'https://baidu.com',
'https://taobao.com',
'https://aliyun.com',
'https://apache.com',
'https://flink.apache.com',
'https://hbase.apache.com',
'https://github.com',
'https://gmail.com',
'https://stackoverflow.com',
'https://python.org'
]

def main():
while True:
if random.randrange(10) < 4:
url = random.choice(web_set[:3])
else:
url = random.choice(web_set)

log_entry = {
'userName': random.choice(user_set),
'visitURL': url,
'ts': time.time()
}

print(json.dumps(log_entry))
time.sleep(0.05)

if __name__ == "__main__":
    main()

