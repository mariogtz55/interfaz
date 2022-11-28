import datetime
import nidaqmx
from nidaqmx.constants import AcquisitionType
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.dates as md
import pandas as pd
from DB_mangeloc.lectura import *
import keyboard



def get_datos():
    sample_rate = 25600
    samples_to_acq = 6
    channel_name = 'Dev1/ai0'
    cont_mode = AcquisitionType.CONTINUOUS
    units_g = nidaqmx.constants.AccelUnits.G
    last=get_last_index()
    last=list(last)
    with nidaqmx.Task() as task:
    
    # Create accelerometer channel and configure sample clock and trigger specs
        task.ai_channels.add_ai_accel_chan(channel_name, units = units_g)
        task.timing.cfg_samp_clk_timing(sample_rate, sample_mode = cont_mode, samps_per_chan=samples_to_acq)
        ydata=[]
        ini = datetime.datetime.now()
        start = pd.Timestamp(ini)
        # Reading data from sensor and generating time data with numpy
        ydata = task.read(number_of_samples_per_channel=samples_to_acq)
        fin = datetime.datetime.now()
        end = pd.Timestamp(fin)
        xdata = t = np.linspace(start.value, end.value, samples_to_acq)
        xdata = pd.to_datetime(xdata)
        df = pd.DataFrame(list(zip(xdata, ydata)),
        columns =['Date-time', 'Accel'])
        #insertar(tuples)
        #execute_many(df,'cnc')
        df.index=range(last[0]+1,(last[0]+samples_to_acq)+1) 
    return df