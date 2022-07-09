# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import numpy as np
import time

FILENAME = "/mnt/ceph/storage/data-tmp/teaching-current/jk76qufi/classified/statements_sh_bal_cleaned.csv"
START = # TODO Set as you wish
END = # TODO Set as you wish


def readlist(rangb: int, rangend: int, filename: str):
    list = pd.read_csv(filename)
    sublist = list.loc[rangb:rangend]
    return sublist

def label(df):
    answer = []
    counter = 0
    for index, row in df.iterrows():
        print(f"{counter}/{len(df)}")
        print(row["text"])
        x = input("Future referecencing statement Y/N: ")
        print("")
        #time.sleep(5)
        while x != "Y" and x != "N":
            print("Valid answer is Y or N")
            x = input("Future referecencing statement Y/N: ")
        if x == "Y":
            answer.append(1)
        else:
            answer.append(0)
        counter +=1

    df["handlable"] = answer
    df['diff'] = np.where(df['label'] == df['handlable'], 1, 0)
    df.to_csv("handlables.csv")
    same =  df['diff'].sum()
    accuracy = same/len(df)*100
    print(f"The lable is {accuracy}%")

def getstats():
    df = pd.read_csv('handlables.csv')
    same = df['diff'].sum()
    accuracy = same / len(df) * 100
    print(f"The accuracy is {accuracy}%")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    label(readlist(START,END,FILENAME))
    #getstats()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
