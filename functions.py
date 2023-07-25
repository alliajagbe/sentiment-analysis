from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import string
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def header_df(df):
    df = df.iloc[2:]
    new_header = df.iloc[0]
    df = df[1:]
    df.columns = new_header

    df = df.reset_index(drop=True)
    return df


def frequency_analysis(df, col):
    text = ''.join(df[col])
    text = text.lower()
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [w for w in tokens if not w in stop_words]

    # removing punctuation
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    stripped = [w for w in stripped if w.isalpha()]
    return stripped

def word_cloud(text, list_of_words):
    freq_dist = FreqDist(list_of_words)
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(freq_dist)
    plt.figure(figsize=(20, 10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig(text + '.png')
    plt.show()
