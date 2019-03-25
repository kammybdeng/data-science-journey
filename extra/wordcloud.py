from wordcloud import WordCloud,STOPWORDS
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

def plot_wordcloud(text, figure_size=(15,8)):


    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(max_font_size=50,
                          max_words=100,
                          random_state = 9,
                          background_color="white",
                          stopwords=stopwords).generate_from_frequencies(text)


    plt.figure(figsize=figure_size)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

wordcloud_text = ['DATA SCIENCE', 'Machine Learning', 'Big Data', 'Python',
                  'Statistics', 'Research', 'Probability', 'Information',
                  'Analytics', 'Data Mining', 'Artificial Intelligence',
                  'Bayesian', 'Decision Tree', 'kNN', 'k-Means', 'Clustering',
                  'Pattern', 'Visualization', 'Database', 'Processing', 'Prediction',
                  'Programming', 'Deep Learning', 'Naive Bayes', 'Pruning',
                  'Gradient Descent', 'Cloud Computing', 'Warehouse', 'Algorithm',
                  'Metrics', 'Program', 'Detection', 'Wrangling', 'Logistic','Regression',
                  'NLP', 'Neural Network', 'Methodology', 'Tools', 'Researchers',
                  'Softwares', 'Projects', 'Bridge', 'AWS', 'Engineering',
                  'Consulting', 'Support', 'Knowledge']

df = pd.DataFrame(wordcloud_text, columns = ['text'])
word_cloud_dict = Counter(df['text'])
wordcloud =  plot_wordcloud(word_cloud_dict) 
