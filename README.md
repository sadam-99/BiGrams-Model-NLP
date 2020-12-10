# <!-- // Code Author:-
# // Name: Shivam Gupta
# // Net ID: SXG190040
# // Natural Language Processing  (CS 6320.501) Assignment 2 (Question 3-Bigram Probabilities) -->

## Implementation of Bigram Model Probability

        
## How to Use the Scripts:
 For No Smoothing: Select option =  Nosmoothing
 For Add-One Smoothing: Select option = Addone
 For Good_Turing Smoothing:Select option = Goodturing



## Compiling and Running the Code:

## TRAINING
For Running For No-Smoothing Smoothing:: Run command:- ```python Bigrams_Training.py Nosmoothing ``` on UTD CS Linux Servers / Anaconda Prompt/Command Prompt

For Running For Add-One Smoothing:: Run command:- ```python Bigrams_Training.py Addone ``` on UTD CS Linux Servers / Anaconda Prompt/Command Prompt

For Running For Good-Turing Discounting based Smoothing:: Run command:- ```python Bigrams_Training.py Goodturing ``` on UTD CS Linux Servers / Anaconda Prompt/Command Prompt



## TESTING
For Running For No-Smoothing Smoothing:: Run command:- ```python Bigrams_Testing.py Nosmoothing "Test Sentence" ``` on UTD CS Linux Servers / Anaconda Prompt/Command Prompt

For Running For Add-One Smoothing:: Run command:- ```python Bigrams_Testing.py Addone "Test Sentence" ``` on UTD CS Linux Servers / Anaconda Prompt/Command Prompt

For Running For Good_Turing Discounting based Smoothing:: Run command:- ```python Bigrams_Testing.py Goodturing "Test Sentence"  ``` on UTD CS Linux Servers / Anaconda Prompt/Command Prompt

# Note: you can Choose any sentence and put in Quotes for example: Use "Test Sentence"  like this "Construction_NN of_IN the_DT plant_NN will_MD begin_VB this_DT month_NN and_CC should_MD be_VB completed_VBN"



## Results
 # The Results Can be seen on the Output Console after running the Testing Python File

 Training_File is ```NLP6320_POSTaggedTrainingSet.txt```
# Output Files(For all the Sentences):

```output_bigram_Nosmoothing.txt```: For "Nosmoothing"
```output_bigram_Addone.txt```: "Addone"
```output_bigram_Good_turing.txt```: "Goodturing"

Folder name ```Bigram_Model_Jsons``` Will be generated after training the Models:
```Bigram_Model_Dict.json``` : Contains Dictionary for the Bigram Count
```Probabilities_Cstar.json``` : Contains Dictionary for Probabilities w.r.to the Bucket IDs.
```Whole_Corpus_Dictionary.json```   : Contains Dictionary for the Unigram Count
    

