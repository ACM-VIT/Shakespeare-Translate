#The link to the dataset has been provided in the dataset section already. You can find all the Shakespearean novels there. 
#Each novel is represented by two text files. The files named "original" contain the novels in original Shakespearean format line by line. 
#The same novel with name "modern" contains the whole novel in modern english format. 
#In this way, the same line in a novel can be extracted in Shakespearean format from the "original" file and in modern format from the "modern" file.

#Preprocessing starts:-

def toLowerCase(corpus) 
{
	#since we will be dealing majorly with alphabets, convert all the text to lowercase. 
}

def sentence_tokenize(corpus) 
{
	#tokenize a text file into a list of sentences.
}

def word_tokenize(sentence) #tokenize a sentence into a bag of words.
{
	#Hint:Use nltk.RegexpTokenizer() as this will remove punctuation(.,?,!) from the sentence besides tokenising it.
}

def listOfAlphabets(sentence) 
{
	#convert a sentence into an equivalent list of characters without punctuation(.,?,!)
}

#Converting the sentences into vectors:-

def vectorize(sentence) 
{
	#Convert a sentence into a numpy array. Since the length of each sentence varies, find the length of the longest sentence first(this length becomes the length of the training vectors) and zero pad the sentences smaller in length that the longest.
}

#Building the model:-

def model()
{
	#Build the model
}

#Training and accuracy:-

def train(data)
{
	#Train you model and plot results using matplotlib.
}

#Find ways to improve the model and increase accuracy.
