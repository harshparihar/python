#
# Matplotlib Date example by geophysique.be
# tutorial 01

"""
Using : Offical mean prices of petroleum-products, last 8 years. Belgien Statistics Office.
            (http://statbel.fgov.be/fr/statistiques/chiffres/energie/prix/moyen_8/, in French)
"""

import matplotlib.pyplot as plt
import numpy as np
import datetime

somedates, e95, e95vatx, e98, e98vatx, dies, diesx = np.loadtxt('carburants.txt',skiprows=1,unpack=True)

xdates = [datetime.datetime.strptime(str(int(date)),'%Y%m') for date in somedates]

fig = plt.figure()
ax = plt.subplot(111)
plt.plot(xdates, e95,'o-',label='E95')
plt.plot(xdates, e98,'o-',label='E98')
plt.plot(xdates, dies,'o-',label='Diesel')
plt.legend(loc=4)
plt.ylabel('Price (Euro)')
plt.xlabel('Year')
plt.grid()
# plt.savefig('dates-tutorial01.png')
plt.show()

# 200701  1.274   1.0529  1.292   1.0678  1.0563  0.866
# 200702  1.274   1.0747  1.292   1.0839  1.0479  0.8584
# 200703  1.3004  1.0427  1.3116  1.0518  1.0386  0.8247
# 200704  1.2617  1.0583  1.2726  1.0679  0.9978  0.8395
# 200705  1.2806  1.1047  1.2922  1.1123  1.0158  0.8586
# 200706  1.3367  1.142   1.3458  1.1493  1.0389  0.8802
# 200707  1.3819  1.1735  1.3907  1.1811  1.065   0.8826
# 200708  1.42    1.1702  1.4291  1.1853  1.0679  0.8974
# 200709  1.4159  1.1633  1.4343  1.1896  1.0859  0.907
# 200710  1.4076  1.1331  1.4394  1.164   1.0975  0.8983
# 200711  1.3711  1.1437  1.4084  1.1579  1.087   0.9212
# 200712  1.3839  1.1726  1.4011  1.1868  1.1146  0.9447