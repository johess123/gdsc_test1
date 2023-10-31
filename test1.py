# 先導入後面會用到的套件
import requests # 請求工具
import datetime # 取得日期
import time # 用來暫停程式

# 要爬的股票
stock = ["1101","2330"]
# 取得現在時間
date = datetime.datetime.today().strftime("%Y%m%d")
for i in range(len(stock)): # 迴圈依序爬股價
    # 現在處理的股票
    stockid = stock[i]
    # 網址塞入股票編號 & 日期
    url = "https://www.twse.com.tw/rwd/zh/afterTrading/STOCK_DAY_AVG?date="+date+"&stockNo="+stockid+"&response=json&_=1697638279385"
    # 發送請求，並將回應轉成 Json 格式
    r = requests.get(url)
    result = r.json()
    # 回報的訊息 (可自訂)
    message = "股票 "+str(stockid)+" 今日的收盤價為 "+result["data"][-2][1]
    # 用 telegram bot 回報股價
    # bot token
    token = "你的 bot token"
    # 使用者 id
    chat_id="你的 telegram id"
    # bot 送訊息
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url)
    # 每次都停 3 秒
    time.sleep(3)
