import matplotlib.pyplot as plt
import auction
import numpy as np
import sys

increase = 100.0

# lastLastRevenue = -np.inf
# lastRevenue = -np.inf
bestRevenue = 0
bestReserve = 0

# option = ["auction.py", "--loglevel", "debug", "--num-rounds", "48", "--perms", "1", "--iters", "200", "--reserve", str(reserve), "--seed", "2", "--mech=GSP", "AngelSlavBB,5"]

# while abs(curRevenue - lastRevenue) > 10:
# 	sys.argv = option
# 	result = auction.main(sys.argv)
# 	# lastLastRevenue = lastRevenue
# 	lastRevenue = curRevenue
# 	curRevenue = result[0]
# 	print("==== curRevenue = " + str(curRevenue) + " ==== " + str(reserve) + " ====")
# 	if curRevenue < lastRevenue:
# 		increase = -0.25*increase
# 	if increase < 0:
# 		reserve += min(-1, int(increase))
# 	else:
# 		reserve += max(1, int(increase))

# 	option = ["auction.py", "--loglevel", "debug", "--num-rounds", "48", "--perms", "1", "--iters", "200", "--reserve", str(reserve), "--seed", "2", "--mech=GSP", "AngelSlavBB,5"]

results = []

# for i in range(64, 101):
# 	reserve = i
# 	option = ["auction.py", "--loglevel", "debug", "--num-rounds", "48", "--perms", "1", "--iters", "200", "--reserve", str(reserve), "--seed", "2", "--mech=GSP", "AngelSlavBB,5"]
# 	sys.argv = option
# 	result = auction.main(sys.argv)
# 	curRevenue = result[0]
# 	print("="*50)
# 	print("==== curRevenue = " + str(curRevenue) + " ==== " + str(reserve) + " ====")
# 	print("="*50)
# 	if curRevenue > bestRevenue:
# 		bestRevenue = curRevenue
# 		bestReserve = reserve

for i in range(0, 150, 10):
	reserve = i
	option = ["auction.py", "--loglevel", "debug", "--num-rounds", "48", "--perms", "1", "--iters", "200", "--reserve", str(reserve), "--seed", "2", "--mech=VCG", "Truthful,5"]
	sys.argv = option
	result = auction.main(sys.argv)
	curRevenue = result[0]
	results.append((reserve, curRevenue))
	print("="*50)
	print("==== curRevenue = " + str(curRevenue) + " ==== " + str(reserve) + " ====")
	print("="*50)
	if curRevenue > bestRevenue:
		bestRevenue = curRevenue
		bestReserve = reserve

print("Revenue per reserve price:\n" + str(results))

# print("Optimal Revenue = " + str(bestRevenue) + ", and reserve price for this revenue is <<" + str(bestReserve) + ">>.")













