x = int(input("số phút gọi :"))
y = "số tiền cần thanh toán"
if x <= 100:
    y = x*1000
if x >= 101 and x <= 300:
    y = 100*1000 + (x-100)*800
if x > 300:
    y = 100*1000 + 200*800 + (x-300)*600
else:
    x = int(input("số phút gọi :"))
print(f"số tiền cần thanh toán là {y}")
