from flask_restplus import Namespace, Resource, fields
from flask import abort
from app.models import Tweet
from app import db

api = Namespace('tweets')

json_tweet = api.model('Tweet', {
    'id': fields.Integer,
    'text': fields.String,
    'created_at': fields.DateTime
})


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

    @api.marshal_with(json_tweet, code=200)
    def get(self):
        tweet = db.session.query(Tweet).all()
        if tweet is None:
            api.abort(404, "Tweet {} doesn't exist".format(id))
        else:
            tweet.text = api.payload["text"]
            return tweet


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

