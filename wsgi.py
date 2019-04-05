from app import create_app
<<<<<<< HEAD
from app.apis.tweets import *
from flask import jsonify

application = create_app()

if __name__ == '__main__':
    application.run(debug=True)


@application.route('/api/v1/tweets/<int:tweet_id>', methods=['GET'])
def read_tweet(tweet_id):
    msg = TweetResource()
    return jsonify(msg.get(tweet_id))


@application.route('/api/v1/tweets', methods=['POST'])
def post_tweet():
    msg = Tweet()
    msg.post()
    return msg, 201


@application.route('/api/v1/tweets/<int:tweet_id>', methods=['DELETE'])
def delete_tweet(tweet_id):
    msg = TweetResource()
    msg.delete(tweet_id)
    return None




=======

application = create_app()
if __name__ == '__main__':
    application.run(debug=True)
>>>>>>> df1b6b8718bfc5762252663c6cefef16e49a6ef1
