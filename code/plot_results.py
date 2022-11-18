import imp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

def read_results(file_name='results.csv'):
    data = pd.read_csv(file_name)
    return data

def plot_results(data):
    sns.set_theme(style='ticks')
    sns.lineplot(data=data, x= 'time', y = 'voltage', marker = 'o')

def run_plots():
    data = read_results()
    plot_results(data)
    plt.show()


run_plots()