# Made by AquaJaite 2022.07.05

def hello():
	print("Hello world!")

# 縮排很重要喔!

def tryit():
	print("這邊可以自己嘗試看看")

def store(a, b, c):
	# 小小商店
	apple = int(a)
	banana = int(b)
	cabbage = int(c)
	# 設定好產品數量

	print("歡迎來到 Tim 的小小商店")
	buy_apple = int(input("你需要多少蘋果呢?\n"))
	if buy_apple > apple:
		print("我沒有那麼多蘋果欸，來看看別的商品吧")
		buy_apple = 0
	else:
		apple = apple - buy_apple
		print("你買了", buy_apple, "顆蘋果，還剩下", apple, "顆")

	buy_banana = int(input("你需要多少香蕉呢?\n"))
	if buy_banana > banana:
		print("我沒有那麼多香蕉欸，來看看別的商品吧")
		buy_banana = 0
	else:
		banana = banana - buy_banana
		print("你買了", buy_banana, "根香蕉，還剩下", banana, "根")

	buy_cabbage = int(input("你需要多少高麗菜呢?\n"))
	if buy_cabbage > cabbage:
		print("我沒有那麼多高麗菜欸，來看看別的商品吧")
		buy_cabbage = 0
	else:
		cabbage = cabbage - buy_cabbage
		print("你買了", buy_cabbage, "顆高麗菜，還剩下", cabbage, "顆")
	
	buy = buy_apple + buy_banana + buy_cabbage

	return buy 	# 合計並回傳總共買了多少東西