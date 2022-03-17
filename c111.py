import statistics
import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas as pd
import random

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

population_mean = statistics.mean(data)
print("Population mean is", population_mean)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data) - 1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["Reading Time"], show_hist=False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0, 100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)

    mean = statistics.mean(mean_list)
    std_deviation = statistics.stdev(mean_list)
    print(f"Mean is {mean}")
    print(f"Standard deviation is {std_deviation}")

    first_std_deviation_start, first_std_deviation_end = mean - std_deviation, mean + std_deviation
    second_std_deviation_start, second_std_deviation_end = mean - (2 * std_deviation), mean + (2 * std_deviation)
    third_std_deviation_start, third_std_deviation_end = mean - (3 * std_deviation), mean + (3 * std_deviation)

    df = pd.read_csv("data.csv")
    data = df["reading_time"].tolist()

    mean_of_sample1 = statistics.mean(data)
    print("Mean of data is", mean_of_sample1)
    
    fig = ff.create_distplot([mean_list], ["Reading Time"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.04], mode="lines", name="MEAN"))
    fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 0.04], mode="lines", name="MEAN OF SAMPLE 1"))
    fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.04], mode="lines", name="STANDARD DEVIATION ONE START"))
    fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.04], mode="lines", name="STANDARD DEVIATION ONE END"))
    fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.04], mode="lines", name="STANDARD DEVIATION TWO START"))
    fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.04], mode="lines", name="STANDARD DEVIATION TWO END"))
    fig.add_trace(go.Scatter(x=[third_std_deviation_start, third_std_deviation_start], y=[0, 0.04], mode="lines", name="STANDARD DEVIATION THREE START"))
    fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.04], mode="lines", name="STANDARD DEVIATION TREE END"))
    fig.show()

    zscore = (mean_of_sample1 - mean)/std_deviation
    print(f"The z score is {zscore}")

setup()