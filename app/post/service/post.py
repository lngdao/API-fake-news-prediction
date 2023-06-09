from app.post.model.post import Post
from typing import List
import connection
from datetime import datetime
from bson import ObjectId
from joblib import load
import os
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
import re
import pandas as pd
from deta import Drive

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

drive = Drive("chunks")

model_path = os.path.join(os.getcwd(), "model.joblib")
model = load(model_path)

vectorizer = TfidfVectorizer()
porter_stemmer = PorterStemmer()

try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")

from nltk.corpus import stopwords


def stemming(content):
    stemmed_content = re.sub("[^a-zA-Z]", " ", content)
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    stemmed_content = [
        porter_stemmer.stem(word)
        for word in stemmed_content
        if word not in stopwords.words("english")
    ]
    stemmed_content = " ".join(stemmed_content)
    return stemmed_content


news_dataset = pd.read_csv(drive.get("train.csv"))

news_dataset.shape

news_dataset.head()
news_dataset.isnull().sum()

news_dataset = news_dataset.fillna("")
news_dataset["content"] = news_dataset["author"] + " " + news_dataset["title"]

X = news_dataset.drop(columns="label", axis=1)
Y = news_dataset["label"]

news_dataset["content"] = news_dataset["content"].apply(stemming)

X = news_dataset["content"].values
Y = news_dataset["label"].values

Y.shape

vectorizer.fit(X)

class PostService:
    def __init__(self):
        ...

    async def get_post_list(self) -> List[Post]:
        data = connection.db["post"].find()
        data = [
            {
                "_id": str(item["_id"]),
                "title": item["title"],
                "image": item["image"],
                "description": item["description"],
                "created_at": item["created_at"],
            }
            for item in data
        ]

        return data

    async def get_post_detail(self, post_id) -> Post:
        post = connection.db["post"].find_one({"_id": ObjectId(post_id)})
        post["_id"] = str(post["_id"])
        post["created_at"] = post["created_at"].isoformat()

        return post

    async def create_post(self, req_data) -> Post:
        current_time = datetime.now()
        result = connection.db["post"].insert_one(
            {
                "title": req_data.title,
                "description": req_data.description,
                "content": req_data.content,
                "created_at": current_time,
                "image": req_data.image,
            }
        )

        inserted_id = result.inserted_id
        post = Post(
            id=str(inserted_id),
            title=req_data.title,
            description=req_data.description,
            content=req_data.content,
            created_at=current_time,
            image=req_data.image,
        )

        return post

    async def prediction_post_content(self, req_data) -> Post:
        content = req_data.content

        processed_content = stemming(content)
        X_vector = vectorizer.transform([processed_content])
        prediction = model.predict(X_vector)

        return 0 if prediction[0] == 0 else 1

    async def delete_post(self, post_id):
        post = connection.db["post"].find_one({"_id": ObjectId(post_id)})

        if not post:
            raise HTTPException(
                status_code=403, detail="the post does not exist in the system"
            )

        connection.db["post"].delete_one({"_id": ObjectId(post_id)})

        return True
