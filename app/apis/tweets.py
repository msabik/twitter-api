from flask_restplus import Namespace, Resource, fields
<<<<<<< HEAD
from flask import abort
from app.models import Tweet
from app import db

api = Namespace('tweets')

json_tweet = api.model('Tweet', {
=======
from app.db import tweet_repository

api = Namespace('tweets')

tweet = api.model('Tweet', {
>>>>>>> df1b6b8718bfc5762252663c6cefef16e49a6ef1
    'id': fields.Integer,
    'text': fields.String,
    'created_at': fields.DateTime
})

<<<<<<< HEAD
json_new_tweet = api.model('New tweet', {
    'text': fields.String(required=True)
})

@api.route('')
@api.response(422, 'Invalid tweet')
class TweetsResource(Resource):
    @api.marshal_with(json_tweet, code=201)
    @api.expect(json_new_tweet, validate=True)
    def post(self):
        text = api.payload["text"]
        if len(text) > 0:
            tweet = Tweet(text=text)
            db.session.add(tweet)
            db.session.commit()
            return tweet, 201
        else:
            return abort(422, "Tweet text can't be empty")

@api.route('/<int:tweet_id>')
class TweetResource(Resource):
    @api.marshal_with(json_tweet)
    def get(self, id):
        tweet = db.session.query(Tweet).get(id)
        if tweet is None:
            api.abort(404, "Tweet {} doesn't exist".format(id))
        else:
            return tweet

    @api.marshal_with(json_tweet, code=200)
    @api.expect(json_new_tweet, validate=True)
    def patch(self, id):
        tweet = db.session.query(Tweet).get(id)
        if tweet is None:
            api.abort(404, "Tweet {} doesn't exist".format(id))
        else:
            tweet.text = api.payload["text"]
            return tweet

    def delete(self, id):
        tweet = db.session.query(Tweet).get(id)
        if tweet is None:
            api.abort(404, "Tweet {} doesn't exist".format(id))
        else:
            db.session.delete(tweet)
            db.session.commit()
            return None

    @api.marshal_with(json_tweet)
    @api.route('/list/<int:tweet_id>')
    def list(self):
        tweet = db.session.query(Tweet).all()
        if tweet is None:
            api.abort(404, "Tweet {} doesn't exist".format(id))
        else:
            tweet.text = api.payload["text"]
=======

@api.route('/<int:id>')
@api.response(404, 'Tweet not found')
@api.param('id', 'The tweet unique identifier')
class TweetResource(Resource):
    @api.marshal_with(tweet)
    def get(self, id):
        tweet = tweet_repository.get(id)
        if tweet is None:
            api.abort(404)
        else:
>>>>>>> df1b6b8718bfc5762252663c6cefef16e49a6ef1
            return tweet
