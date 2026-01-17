import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

def recommend_roles(user_skills):
    df = pd.read_csv("data/job_roles.csv")
    corpus = df["skills"].tolist()
    corpus.append(",".join(user_skills))

    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(corpus)

    similarity = cosine_similarity(vectors[-1], vectors[:-1])

    df["match_score"] = similarity[0] * 100
    return df.sort_values("match_score", ascending=False)
