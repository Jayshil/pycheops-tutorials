import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec as gd
import batman
import catwoman

# Batman model
params = batman.TransitParams()

params.t0 = 0.
params.per = 2.72403380
params.rp = 0.07070261
params.a = 4.71779818

bb = 0.42912952
aa = 4.71779818
inc = np.arccos(bb/aa)*(180/np.pi)

params.inc = inc
params.ecc = 0.
params.w = 90.
params.limb_dark = 'quadratic'
params.u = [0.4951, 0.0545]

t = np.linspace(-0.2, 0.2,1000)
m = batman.TransitModel(params, t)
fl_bat = m.light_curve(params)

# catwoman model
p1 = catwoman.TransitParams()

p1.t0 = 0.
p1.per = 2.72403380
p1.rp = 0.07070261
p1.rp2 = 0.07070261 + 0.0005
p1.a = 4.71779818
p1.inc = inc
p1.ecc = 0.
p1.w = 90.
p1.limb_dark = 'quadratic'
p1.u = [0.4951, 0.0545]
p1.phi = -30.

mo = catwoman.TransitModel(p1, t)
fl_cat = mo.light_curve(p1)

## Plotting the results

fig = plt.figure(figsize = (8,10))
gs = gd.GridSpec(2, 1, height_ratios = [4,2])

ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1], sharex = ax1)

ax1.plot(t, fl_bat, c='orangered', alpha=0.5, label='batman model')
ax1.plot(t, fl_cat, c='cornflowerblue', alpha=0.5, label='catwoman model')
ax1.legend()
ax1.set_ylabel('FLux')

ax2.plot(t, (fl_bat - fl_cat)*1e6, c='k')
ax2.set_ylabel('Residuals (ppm)')
ax2.set_xlabel('Phase')

plt.show()
