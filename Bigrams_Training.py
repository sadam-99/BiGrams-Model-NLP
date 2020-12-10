# <!-- // Code Author:-
# // Name: Shivam Gupta
# // Net ID: SXG190040
# // Natural Language Processing  (CS 6320.501) Assignment 2 (Question 3-Bigram Probabilities) -->

import sys
import os
import re
import json



Smoothing_Type = sys.argv[1]
# Smoothing_Type  can be "No", "Addone", "goodturing" (3 options from Command Line Input)

# Reading the Training File
Training_File = open("NLP6320_POSTaggedTrainingSet.txt", "r")
if Smoothing_Type == "Nosmoothing":
    Output_File=open("output_bigram_Nosmoothing.txt","w")
elif  Smoothing_Type == "Addone":
    Output_File=open("output_bigram_Addone.txt","w")
elif  Smoothing_Type == "Goodturing":
    Output_File=open("output_bigram_Good_turing.txt","w")
else:
    print("Please Enter the Correct Smoothing Type or enter Nosmoothing")
    exit()

#Getting sentences from the Training Text File
Sentences=Training_File.readlines()
Whole_Corpus=[]
Whole_Corpus_Dictionary=dict()

#Creating the Whole Training Corpus
for Sen in Sentences:
    words=Sen.split()

    for word in words:

        Transformed_Word = re.match("(.*)_(.*)", word).group(1)
        Transformed_Word = Transformed_Word.lower()
        Whole_Corpus.append(Transformed_Word)

        if Transformed_Word not in Whole_Corpus_Dictionary.keys():
            Whole_Corpus_Dictionary[Transformed_Word]=1
        else:
            Whole_Corpus_Dictionary[Transformed_Word] += 1

# print("Whole_Corpus_Dictionary", Whole_Corpus_Dictionary)
Total_Count_Words=len(Whole_Corpus)

Bigram_Model_Dict={}
# Creating a Bigram Model with their Frequencies
for Sen in Sentences:
    words = Sen.split()
    for i in range(len(words) - 1):
        Transformed_Word=re.match("(.*)_(.*)", words[i]).group(1).lower() + " " + re.match("(.*)_(.*)", words[i + 1]).group(1).lower()
        if Transformed_Word not in Bigram_Model_Dict.keys():
            Bigram_Model_Dict[Transformed_Word] = 1
        else:
            Bigram_Model_Dict[Transformed_Word] += 1


# Creating the Buckets for the Good-Turing Method
if Smoothing_Type=="Goodturing":
    Buckets_goodturing = {}
    for bigram in Bigram_Model_Dict.keys():
        Buckets_goodturing[Bigram_Model_Dict[bigram]] = Buckets_goodturing.get(Bigram_Model_Dict[bigram], [])
        Buckets_goodturing[Bigram_Model_Dict[bigram]].append(bigram)

    Sorted_Buckets_Dict={}
    for Bucket_ID in sorted(Buckets_goodturing.keys()):
        # print("Bucket_ID, Buckets_goodturing", Bucket_ID, Buckets_goodturing[Bucket_ID])
        Sorted_Buckets_Dict[Bucket_ID]=Buckets_goodturing[Bucket_ID]


    # print("============Sorted_Buckets_Dict====", Sorted_Buckets_Dict)
    # Calculating Probabilty based on C Star Values
    Probabilities_Cstar={}
    Probabilities_Cstar[0] = len(Sorted_Buckets_Dict[1])/len(Bigram_Model_Dict) # For 0 Count: The Probability = N1/N

    # Calculation of the C* and their Probabilities
    C_Star = {}
    for C in Sorted_Buckets_Dict.keys():
        # print("C", C)
        if (C+1) in Sorted_Buckets_Dict.keys():
            C_Star[C] = ((C+1) * len(Sorted_Buckets_Dict[C+1])/len(Sorted_Buckets_Dict[C]))
        else:
            C_Star[C] = 0 # As Sorted_Buckets_Dict[i+1] is not available
        Probabilities_Cstar[C] = C_Star[C] / len(Bigram_Model_Dict)
    
    # print("Probabilities_Cstar", Probabilities_Cstar)
# Writing the sentences and the bigrams probabilities into the Text output file.
for Sen in Sentences:
    Output_File.writelines("The sentence is:\n")
    Output_File.writelines (Sen+"\n")
    bigrams={}
    words=Sen.split()
    for c in range(len(words)-1):
        bigrams[re.match("(.*)_(.*)", words[c]).group(1).lower()+ " "+re.match("(.*)_(.*)", words[c+1]).group(1).lower()]=0
    Output_File.writelines("The bigrams of the sentance are:\n")
    Output_File.writelines("--------------------------------\n")
    for bi_Gr in bigrams:
        # print("bi_Gr", bi_Gr)
        bigramwords=bi_Gr.split()
        Output_File.writelines(bigramwords[0]+" "+bigramwords[1])
        if Smoothing_Type == "Nosmoothing":
            bigrams[bi_Gr]=(Bigram_Model_Dict[bi_Gr])/(Whole_Corpus_Dictionary[bigramwords[0]])
        elif Smoothing_Type == "Addone":
            bigrams[bi_Gr]=(Bigram_Model_Dict[bi_Gr]+1)/(Whole_Corpus_Dictionary[bigramwords[0]]+len(Whole_Corpus_Dictionary))
        elif Smoothing_Type == "Goodturing":
            x = Bigram_Model_Dict.get(bi_Gr, 0)
            bigrams[bi_Gr] = Probabilities_Cstar[x]
            # print("Probabilities_Cstar[x]", Probabilities_Cstar[x])
            # bigrams[bi_Gr] = C_Star[x]/Whole_Corpus_Dictionary[bigramwords[0]]
            

    Output_File.writelines("------------The probabilites of the bigrams in the sentance are:------------\n")
    Output_File.writelines(str(bigrams)+"\n")
    Sen_Probability=1
    Output_File.writelines("The probability of the whole sentance is:\n")

    for prob in (bigrams.values()):
        Sen_Probability*=prob
    Output_File.writelines(str(Sen_Probability)+"\n")

    Output_File.writelines("============================================================================================================\n")

# Creating The Folder for Saving Models
if not os.path.exists('Bigram_Model_Jsons'):
    os.makedirs('Bigram_Model_Jsons')


# print("Whole_Corpus_Dictionary", Whole_Corpus_Dictionary)

# Dumping the Whole Corpus into JSON
with open('Bigram_Model_Jsons/Whole_Corpus_Dictionary.json', 'w') as JS:
    json.dump(Whole_Corpus_Dictionary, JS)

# Dumping the Bigrams Count into JSON
with open('Bigram_Model_Jsons/Bigram_Model_Dict.json', 'w') as JS:
    json.dump(Bigram_Model_Dict, JS)

# Dumping the Probabilities_Cstar into JSON
if Smoothing_Type == "Goodturing":
    with open('Bigram_Model_Jsons/Probabilities_Cstar.json', 'w') as JS:
        json.dump(Probabilities_Cstar, JS)
print("==========Bigram Model training for Smoothing type:", Smoothing_Type, "Completed===========")
print("Please Open output text file for viewing the BiGrams and Probabilities in all the Sentences")