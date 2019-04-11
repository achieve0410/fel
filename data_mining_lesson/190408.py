
'''

plotTree는 각자 알아서 하는 것으로

'''

import matplotlib
import matplotlib.pyplot as plt

ax = plt.subplot(111)
plt.annotate("This is arrow", xy=(2, 2), xytext=(6, 7), arrowprops=dict(facecolor='black', shrink=.05), )
plt.show()
