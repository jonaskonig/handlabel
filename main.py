# This is a sample Python script.
import random
import re

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import numpy as np
import time

FILENAME_Database = "databasedata.csv"
FILENAME_NEGATIVE = "alllist_shuffle.txt"
START = 0
END = 2


def readfiletolist(filename, start, end):
    thislist = []
    f = open(filename)
    lines = f.readlines()
    for i in range(start,end+1):
        thislist.append(re.sub(r"\n", "", lines[i]))
    return thislist
def readlist(rangb: int, rangend: int, filename1: str):
    list = pd.read_csv(filename1, nrows=END+1)
    sublist = list.loc[rangb:rangend]
    return sublist.to_dict('records')


def label(datbase, negative ):
    output = []
    print(len(datbase))
    newlist = datbase+negative
    random.shuffle(newlist)
    counter = 0
    for item in newlist:
        print(f"{counter}/{len(newlist)}")
        if type(item) == str:
            print(item)
        elif type(item) == dict:
            print(item["text"])
        else:
            continue
        x = input("Future referencing statement Y/N: ")
        print("")
        while x != "Y" and x != "N" and x != "y" and x != "n":
            print("Valid answer is Y or N")
            x = input("Future referencing statement Y/N: ")
        if x == "Y":
            answer = 1
        else:
            answer = 0

        if type(item) == dict:
            print(item["emotion"])
            x = input("Does emotion fit 0:not at all, 1: mostly , 2: totally: ")
            while int(x) != 1 and int(x) != 2 and int(x) != 0:
                print("Valid answer are 0,1,2")
                x = input("Does emotion fit 0:not at all, 1: mostly , 2: totally: ")
            emotion = x
            print(item["topic"])
            x = input("Does topic fit 0:not at all, 1: mostly , 2: totally: ")
            while int(x) != 1 and int(x) != 2 and int(x) != 0:
                print("Valid answer are 0,1,2")
                x = input("Does topic fit 0:not at all, 1: mostly , 2: totally: ")
            topic = x
            answers = {"text": item["text"], "emotion": item["emotion"], "topic": item["topic"],
                    "emotionhandlabel": emotion, "topichandlabel": topic, "futurehandlabel": answer, "bertlabel":1}
        else:
            answers = {"text": item, "emotion": None, "topic": None,
                    "emotionhandlabel": None, "topichandlabel": None, "futurehandlabel": answer, "bertlabel": 0}
        output.append(answers)
        counter += 1
    # df['diff'] = np.where(df['label'] == df['handlable'], 1, 0)
    df = pd.DataFrame(output)
    df.to_csv(f"handlabels-{START}-{END}.csv", index=False)
    # same =  df['diff'].sum()
    # accuracy = same/len(df)*100
    # print(f"The lable is {accuracy}%")

def getstats():
    df = pd.read_csv('handlables.csv')
    same = df['diff'].sum()
    accuracy = same / len(df) * 100
    print(f"The accuracy is {accuracy}%")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    label(readlist(START,END,FILENAME_Database),readfiletolist(FILENAME_NEGATIVE,START,END,))
    #getstats()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
