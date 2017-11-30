#!/usr/bin/env python

import sys

if len(sys.argv) != 4:
	print "Usage: {} [risk in percent] [price/share] [number of shares]".format(sys.argv[0])
	sys.exit(2)

risk = float(sys.argv[1])
price = float(sys.argv[2])
numOfShares = float(sys.argv[3])

stopLossPrice = price - (price * risk)
loss = risk * (numOfShares * price)

print "Stop-Loss-Target: {}\nPotential Loss: {}".format(stopLossPrice,loss)