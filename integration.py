import subprocess

print("選擇操作方式:")
print("A: 突破買入")
print("B: 突破賣出")
print("C: 市價買入並設止損")
print("D: 市價賣出並設止損")

user_choice = input("請輸入選項: ")

if user_choice.upper() == 'A':
    subprocess.run(['python', 'breakout_buy.py'])
elif user_choice.upper() == 'B':
    subprocess.run(['python', 'breakout_sell.py'])
elif user_choice.upper() == 'C':
    subprocess.run(['python', 'market_buy_with_stop.py'])
elif user_choice.upper() == 'D':
    subprocess.run(['python', 'market_sell_with_stop.py'])
else:
    print("請重新選擇。")
