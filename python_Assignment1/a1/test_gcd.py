from gcd import gcd
def gcd_test():
	assert gcd(12,13) == 1
	assert gcd(12,48) == 12
	assert gcd(12,'s') == "TypeError"
	assert gcd(13.4,'s') == "TypeError"
	assert gcd(1,-1) == "ValueError"
	assert gcd(-9,3) == "ValueError"
	assert gcd(-7,-1) == "ValueError"
	assert gcd('p',6) == "TypeError"
if __name__ == "__main__":
	gcd_test()
