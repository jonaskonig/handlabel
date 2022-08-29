import pandas as pd
import numpy as np


def printstatistik():
    df = pd.read_csv("allhandlabels.csv")
    future = df['handlable'].value_counts()[1]
    nofuture = df['handlable'].value_counts()[0]
    print("Handlabeling")
    print(f"There are {future} future labels and {nofuture} nonfuture labels.")
    print(f"in percent there are {future / len(df) * 100}% future labels.")


def evalstatic1filter():
    df = pd.read_csv("statements_static1.csv", usecols=['tense'])
    future = df['tense'].value_counts()[1]
    nofuture = df['tense'].value_counts()[0]
    print("Static filter 1")
    print(f"There are {future} future labels and {nofuture} nonfuture labels. The leght is {len(df)}")
    print(f"in percent there are {future / len(df) * 100}% future labels.")
    df2 = df.iloc[:601]
    future = df2['tense'].value_counts()[1]
    nofuture = df2['tense'].value_counts()[0]
    print("Direckt compare Static filter 1")
    print(f"There are {future} future labels and {nofuture} nonfuture labels.")
    print(f"in percent there are {future / len(df2) * 100}% future labels.")
    df = pd.read_csv("allhandlabels.csv")
    df2['diff'] = np.where(df2['tense'] == df['handlable'], 1, 0)
    same = df2['diff'].sum()
    accuracy = same / len(df) * 100
    print(f"The accuracy filter 1 handöabel is {accuracy}%")
    df3 = pd.read_csv("static_filter_2_classified.csv", usecols=['future_dom'])
    future = df3['future_dom'].value_counts()[1]
    nofuture = df3['future_dom'].value_counts()[0]
    print("Static filter 2")
    print(f"There are {future} future labels and {nofuture} nonfuture labels. The leght is {len(df3)}")
    print(f"in percent there are {future / len(df3) * 100}% future labels. ")
    del df2
    df2 = df3.iloc[:601]
    df2['diff'] = np.where(df2['future_dom'] == df['handlable'], 1, 0)
    same = df2['diff'].sum()
    accuracy = same / len(df) * 100
    future = df2['future_dom'].value_counts()[1]
    nofuture = df2['future_dom'].value_counts()[0]
    print("Direckt compare Static filter 1")
    print(f"There are {future} future labels and {nofuture} nonfuture labels.")
    print(f"The accuracy filter 2 handöabel is {accuracy}%")


def createnewcsv(filename):
    df = pd.read_csv(filename, index_col=False)
    df["futureright"] = np.where(df['futurehandlabel'] == df["bertlabel"], 1, 0)
    df["falsepositive"] = np.where(df['futurehandlabel'] - df["bertlabel"] == -1, 1, 0)
    df["falsenegative"] = np.where(df["bertlabel"] - df['futurehandlabel'] == -1, 1, 0)
    df["futurerightstatic"] = np.where(df['futurehandlabel'] == df["tense"], 1, 0)
    df["falsepositivestatic"] = np.where(df['futurehandlabel'] - df["tense"] == -1, 1, 0)
    df["falsenegativestatic"] = np.where(df["tense"] - df['futurehandlabel'] == -1, 1, 0)
    df["bertandstatic"] = np.where(df['bertlabel'] == df["tense"] , 1, 0)
    df.to_csv("nowreadyforallwithstatic.csv", index=False)

def combint():
    df = pd.read_csv("handlabels-0-99.csv", index_col=False)
    df = pd.concat([df, pd.read_csv("handlabels-100-199 (1).csv", index_col=False)])
    df = pd.concat([df, pd.read_csv("handlabels-200-299.csv", index_col=False)])
    df.to_csv("allhandlabelcombined.csv", index=False)

def evalthis(filename):
    df = pd.read_csv(filename, index_col=False)
    print(df.head())
    rightcount = df["futureright"].value_counts()[1]
    wrongcount = df["futureright"].value_counts()[0]
    falsepositive = df["falsepositive"].value_counts()[1]
    falsenegative = df["falsenegative"].value_counts()[1]
    rightcountstatic = df["futurerightstatic"].value_counts()[1]
    wrongcountstatic = df["futurerightstatic"].value_counts()[0]
    falsepositivestatic = df["falsepositivestatic"].value_counts()[1]
    falsenegativestatic = df["falsenegativestatic"].value_counts()[1]
    topic_right = df["topichandlabel"].value_counts()[2]
    topic_mostly_right =  df["topichandlabel"].value_counts()[1]
    topic_wrong = df["topichandlabel"].value_counts()[0]
    emotion_right = df["emotionhandlabel"].value_counts()[2]
    emotion_mostly_right = df["emotionhandlabel"].value_counts()[1]
    emotion_wrong = df["emotionhandlabel"].value_counts()[0]
    bertandstatic = df["bertandstatic"].value_counts()[1]
    totoal = len(df)
    print(f"{rightcount/totoal*100}% where right future classified by bert")
    print(f"of the {wrongcount/totoal*100}% {falsenegative/wrongcount*100}% where false negativ and {falsepositive/wrongcount*100}% were false positive.")
    print(f"{topic_right/300*100}% topics were classified right. {topic_mostly_right/300*100} topic were classified mostly right and {topic_wrong/300*100}% were classified wrong.")
    print(f"{emotion_right/300*100}% emotions were classified right. {emotion_mostly_right/300*100} emotions were classified mostly right and {emotion_wrong/300*100}% were classified wrong.")
    print("")
    print("-----------------------------------------------------------------------------------")
    print("")
    print(f"{rightcountstatic/totoal*100}% were classified right by the static filter")
    print(f"of the {wrongcountstatic/totoal*100}% {falsepositivestatic/wrongcountstatic*100}% where false negativ and {falsenegativestatic/wrongcountstatic*100}% were false positive.")
    print(f"in {bertandstatic/totoal*100}% Bert and the static filter tought the same.")
if __name__ == '__main__':
    # df = pd.read_csv("statements_sh_bal_cleaned_classified_only_future.csv", engine="c")
    # df = df.drop_duplicates(subset=['text'])
    # df.to_csv("statements_sh_bal_cleaned_classified_only_future_no_dub.csv", index=False)
    # print(len(df))
    # printstatistik()
    # evalstatic1filter()
    evalthis("nowreadyforallwithstatic.csv")
    #createnewcsv("statements_tenses.csv")
