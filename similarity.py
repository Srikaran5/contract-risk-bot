from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

RISKY_CLAUSES = [
    "Either party may terminate without notice",
    "A heavy penalty shall be imposed",
    "The service provider shall indemnify fully"
]

def check_similarity(text):
    corpus = RISKY_CLAUSES + [text]
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(corpus)
    similarities = cosine_similarity(tfidf[-1], tfidf[:-1])
    return similarities.max()