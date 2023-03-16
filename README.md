# Text_analytics

Dataset contains Email Summary,Notes and Country about Investors to give better recommendations based on the data like a Financial Advisor.

Based on the dataset provided below, this a model to generate a short summary that accurately summarizes the main points and key insights (in negative and positive content). The summary should be concise, yet still, retain the essence of the original text. The summarization model should generate personalized summaries based on a set of user-specific keywords. Then, extend the summarization model to provide additional suggestions or recommendations based on the contents.

Steps involved in this ML model:
  
  1.Understand the data using basic and descriptive statistics.
  2.Pre-processing text data.
  3.Text analytics involve sentence tokenization,removing stop words,filter tokens,sentence score for each text summary.
  4.Metrics used in the model rough score for each data text summary.
  5.NLTK email summary based on rough score of each text data.
  6.Used Gensim implementation of TextRank extractive summarization algorithm.
  7.NLTK sentiment analysis based on nltk email summary and textrank email summary.
  8.After getting sentiment score make classification on text data.
  9.Named entity recognition and keyword extraction to give better recommendations.
