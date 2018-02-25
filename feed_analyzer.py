import sys
import argparse
import nltk

def tweet_analyze(tweet):
    impact_list = []
    tokens = nltk.word_tokenize(tweet)
    tagged = nltk.pos_tag(tokens)
    #print (tagged)
    for word, tag in tagged:
        if tag == "RB" or tag == "NNP" or tag == "NN" or tag == "VB" or tag == "VBZ":
            if len(word) > 2 and "https" not in word and ".co" not in word:
                try:
                    impact_list.append(word.encode('ascii'))
                except UnicodeEncodeError:
                    pass
    return impact_list

if __name__ == "__main__":
    sentence = sys.argv[1]
    impact = tweet_analyze(sentence)
    print (impact)
