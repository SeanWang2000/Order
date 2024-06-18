import subprocess
import os

print("選擇操作方式:")
print("A: 突破買入")
print("B: 突破賣出")
print("C: 市價買入並設止損")
print("D: 市價賣出並設止損")

user_choice = input("請輸入選項: ")

if user_choice.upper() == 'A':
    try:
        os.startfile(r'C:\Users\GL63\Dropbox\直接下單\breakout_buy.exe')
    except Exception as e:
        print(f"打開 breakout_buy.exe 時出錯: {e}")
elif user_choice.upper() == 'B':
    try:
        os.startfile(r'C:\Users\GL63\Dropbox\直接下單\breakout_sell.exe')
    except Exception as e:
        print(f"打開 breakout_sell.exe 時出錯: {e}")
elif user_choice.upper() == 'C':
    try:
        os.startfile(r'C:\Users\GL63\Dropbox\直接下單\market_buy_with_stop.exe')
    except Exception as e:
        print(f"打開 market_buy_with_stop.exe 時出錯: {e}")
elif user_choice.upper() == 'D':
    try:
        os.startfile(r'C:\Users\GL63\Dropbox\直接下單\market_sell_with_stop.exe')
    except Exception as e:
        print(f"打開 market_sell_with_stop.exe 時出錯: {e}")
else:
    print("請重新選擇。")
