# coding=utf-8

import unicodedata
import re
import pandas as pd

if __name__ == '__main__':

    counter=0
    df = pd.read_csv("RemoodRawComments.csv", delimiter=";", encoding="UTF-8")
    
    #print(df.head())

    texts = []
    cleantexts = []

    for i in df.message:
        texts.append(str(i))

        
    for i in texts:
        emoji_pattern = re.compile("["
                                     u"\U0001F600-\U0001F64F"  # emoticons
                                     u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                     u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                     u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                     u"\U00002500-\U00002BEF"  # chinese char
                                     u"\U00002702-\U000027B0"
                                     u"\U00002702-\U000027B0"
                                     u"\U000024C2-\U0001F251"
                                     u"\U0001f926-\U0001f937"
                                     u"\U00010000-\U0010ffff"
                                     u"\u2640-\u2642"
                                     u"\u2600-\u2B55"
                                     u"\u200d"
                                     u"\u23cf"
                                     u"\u23e9"
                                     u"\u231a"
                                     u"\ufe0f"  # dingbats
                                     u"\u3030"
                                     "]+", re.UNICODE)
        if counter < 80176:
            cleantexts.append(emoji_pattern.sub(r'', texts[counter]))  # no emoji
            text = cleantexts[counter]
            df1.at[counter,"message"]=text
        counter = counter + 1
