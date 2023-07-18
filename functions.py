from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

def header_df(df):
    df = df.iloc[2:]
    new_header = df.iloc[0]
    df = df[1:]
    df.columns = new_header

    df = df.reset_index(drop=True)
    return df


def freq_analysis(df, col):
    text = ''.join(df[col])
    text = text.lower()
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [w for w in tokens if not w in stop_words]
    freq_dist = FreqDist(tokens)
    for word, frequency in freq_dist.most_common(10):
        print(u'{};{}'.format(word, frequency))
    return freq_dist
