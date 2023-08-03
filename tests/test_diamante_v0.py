# -*- coding: utf-8 -*-
"""
First test to check readability of ER60 files using Pyecholab library

Created on Thu Jul 13 09:36:31 2023
@author: Susan Montero, Alejandro Ariza
"""

# import modules
from os.path import join, dirname
import glob
from echolab2.instruments import EK60
import matplotlib.pyplot as plt

# get data directory and raw files
ddir     = join(dirname(__file__), 'echosounder', 'bueno')
rawfiles = glob.glob(join(ddir, '*.raw'))

# load first raw file
ek60        = EK60.EK60()
firsrawfile = rawfiles[0]
ek60.read_raw(firsrawfile)
ek60.channel_ids

# get range, time and Sv data
d  = ek60.get_channel_data()[ek60.channel_ids[0]][0].get_Sv()
r  = d.range
t  = d.ping_time
Sv = d.data.T

# show echogram
plt.figure()
plt.pcolormesh(t, r, Sv, vmin=-80, vmax=-50)
plt.ylim(r[-1], r[0])
plt.xlabel('Ping time')
plt.ylabel('Depth')
plt.colorbar().set_label('Sv at 120 kHz (dB)')

