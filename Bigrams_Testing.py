# <!-- // Code Author:-
# // Name: Shivam Gupta
# // Net ID: SXG190040
# // Natural Language Processing  (CS 6320.501) Assignment 2 (Question 3-Bigram Probabilities) -->

import sys
import os
import json
import re

Smoothing_Type = sys.argv[1]
# Smoothing_Type  can be "No", "Addone", "goodturing" (3 options from Command Line Input)
Test_Sentence = sys.argv[2]
# Test_Sentence= "Construction_NN of_IN the_DT plant_NN will_MD begin_VB this_DT month_NN and_CC should_MD be_VB completed_VBN"
## The test Setence."


# Loading the Models based on the Turing Method
with open('Bigram_Model_Jsons/Whole_Corpus_Dictionary.json') as json_file:
    Whole_Corpus_Dictionary = json.load(json_file)
with open('Bigram_Model_Jsons/Bigram_Model_Dict.json') as json_file:
    Bigram_Model_Dict = json.load(json_file)
if  Smoothing_Type == "Goodturing":
    if not os.path.exists('Bigram_Model_Jsons/Probabilities_Cstar.json'):
        print("====Please Train The Model first for Good Turing before Testing ======")
        exit()
    with open('Bigram_Model_Jsons/Probabilities_Cstar.json') as json_file:
        Probabilities_Cstar = json.load(json_file)


Test_Bigrams={}
TestWords=Test_Sentence.split()
Test_Words = []
for word in TestWords:
    Transformed_Word = re.match("(.*)_(.*)", word).group(1).lower()
    Test_Words.append(Transformed_Word)
for k in range(len(Test_Words)-1):
    Test_Bigrams[Test_Words[k].lower()+ " "+Test_Words[k+1].lower()]=0

print("==========The bigrams of the sentance for Smoothing Type", Smoothing_Type," are:===========\n")

#  Calculating the Bigrams and their Probabilities
for Bi_GR in Test_Bigrams:
    Bigrams_Words=Bi_GR.split()
    
    bi_G_count=Bigram_Model_Dict.get(Bi_GR,0)
    if Smoothing_Type == "Nosmoothing":
        if Bigrams_Words[0] not in Whole_Corpus_Dictionary.keys():
            Test_Bigrams[Bi_GR] = 0
        else:
            Test_Bigrams[Bi_GR]=(bi_G_count)/(Whole_Corpus_Dictionary[Bigrams_Words[0]])
    elif  Smoothing_Type == "Addone":
        if Bigrams_Words[0] not in Whole_Corpus_Dictionary.keys():
            Test_Bigrams[Bi_GR]=((bi_G_count)+1)/( 0 +len(Whole_Corpus_Dictionary))
        else:
            Test_Bigrams[Bi_GR]=((bi_G_count)+1)/(Whole_Corpus_Dictionary[Bigrams_Words[0]]+len(Whole_Corpus_Dictionary))
            

    elif  Smoothing_Type == "Goodturing":
        if str(bi_G_count) in Probabilities_Cstar.keys():
            Test_Bigrams[Bi_GR]=Probabilities_Cstar[str(bi_G_count)]
        else:
            Test_Bigrams[Bi_GR]=Probabilities_Cstar[0] # Because that bucket has O item so the probability will be prob[0] = N1/N
    else:
        print("Please Enter the Correct Smoothing Type or enter Nosmoothing For Testing")
        exit()
    print(Bigrams_Words[0]+" "+Bigrams_Words[1])


print("The probabilites of the bigrams in the Test Sentence:", Test_Sentence,  "are:\n")
print("===================================\n")
print(Test_Bigrams)
Test_Sen_Prob=1
print("The probability of the Sentence is:\n")

# Calculating The overall Probability of the Test Sentence
for prob in Test_Bigrams.values():
    Test_Sen_Prob*=prob
print(str(Test_Sen_Prob)+"\n")

print("=======================================================TESTING COMPLETED==============================================================\n")