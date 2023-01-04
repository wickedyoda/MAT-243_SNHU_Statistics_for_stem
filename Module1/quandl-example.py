# loads the necessary libraries
import quandl
import matplotlib.pyplot as plt

# creates a data frame containing TGT stock data
tgt = quandl.get('WIKI/TGT')

# title
plt.title('Target (TGT) closing stock prices', fontsize=20)

# x and y axis labels
plt.xlabel('Year');
plt.ylabel('Stock price (USD)');

# plot
plt.plot(tgt.index, tgt['Adj. Close'])

# saves the image
plt.savefig("tgtstocklinechart.png")