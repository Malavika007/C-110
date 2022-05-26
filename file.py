from cv2 import mean
import pandas as pd
import random
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics

df = pd.read_csv('data.csv')
data = df["temp"].tolist()

# fig = ff.create_distplot([data], ["temp"], show_hist=False)
# fig.show#

# population_mean = statistics.mean(data)
# std_deviation = statistics.stdev(data)

# print("population mean:", population_mean)
# print("std_ deviation :", std_deviation)

# fig.add_trace(go.Scatter(x = [population_mean, population_mean], y = [0,1], mode = "lines", name = "MEAN"))
# fig.show()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ["temp"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
    fig.show()


def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    
    mean = statistics.mean(mean_list)
    print("Mean of sampling distribution :-",mean )

setup()

#std_deviation = statistics.stdev(data_set)
#print("mean of sample: ", mean)
#print("std deviation of sample: ", std_deviation)