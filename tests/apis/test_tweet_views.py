from flask_testing import TestCase
<<<<<<< HEAD
from app import create_app, db
from app.models import Tweet

=======
from app import create_app
from app.models import Tweet
from app.db import tweet_repository
>>>>>>> df1b6b8718bfc5762252663c6cefef16e49a6ef1

class TestTweetViews(TestCase):
    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
<<<<<<< HEAD
        app.config['SQLALCHEMY_DATABASE_URI'] = f"{app.config['SQLALCHEMY_DATABASE_URI']}_test"
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_tweet_show(self):
        first_tweet = Tweet(text="First tweet")
        db.session.add(first_tweet)
        db.session.commit()
=======
        return app

    def setUp(self):
        tweet_repository.clear() # Upgrade the TweetRepository.__clear() method to public!

    def test_tweet_show(self):
        first_tweet = Tweet("First tweet")
        tweet_repository.add(first_tweet)
>>>>>>> df1b6b8718bfc5762252663c6cefef16e49a6ef1
        response = self.client.get("/tweets/1")
        response_tweet = response.json
        print(response_tweet)
        self.assertEqual(response_tweet["id"], 1)
        self.assertEqual(response_tweet["text"], "First tweet")
        self.assertIsNotNone(response_tweet["created_at"])
<<<<<<< HEAD

    def test_tweet_create(self):
        response = self.client.post("/tweets", json={'text': 'New tweet!'})
        created_tweet = response.json
        self.assertEqual(response.status_code, 201)
        self.assertEqual(created_tweet["id"], 1)
        self.assertEqual(created_tweet["text"], "New tweet!")

    def test_tweet_update(self):
        first_tweet = Tweet(text="First tweet")
        db.session.add(first_tweet)
        db.session.commit()
        response = self.client.patch("/tweets/1", json={'text': 'New text'})
        updated_tweet = response.json
        self.assertEqual(response.status_code, 200)
        self.assertEqual(updated_tweet["id"], 1)
        self.assertEqual(updated_tweet["text"], "New text")

    def test_tweet_delete(self):
        first_tweet = Tweet(text="First tweet")
        db.session.add(first_tweet)
        db.session.commit()
        self.client.delete("/tweets/1")
        self.assertIsNone(db.session.query(Tweet).get(1))
=======
>>>>>>> df1b6b8718bfc5762252663c6cefef16e49a6ef1
