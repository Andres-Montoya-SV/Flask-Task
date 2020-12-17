from flask import Flask, request, jsonify, json, make_response
from flask_restful import Api
from PodcastFile import results, links, feed
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
api = Api(app)

app.config['SECRET_KEY'] = 'bic9bksmnx091yuhx'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'Message': 'Token is missing'}), 403
        try:
            data  = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify(({'Message': 'Token is not valid or is missing'})), 403
        return f(*args, **kwargs)
    return decorated

@app.route('/', methods=['GET', 'POST'])
def getPodcast():
    return jsonify(feed, links, results)

## Podcast filter finder function.
@app.route('/podcast/<string:podcast_name>')
@token_required
def PodcastFilter(podcast_name):
    PodcastFound = [podcast for podcast in results if (podcast['name'] == podcast_name or podcast['artistName'] == podcast_name)]
    if (len(PodcastFound) > 0):
        return jsonify({"Podcast found": PodcastFound[0]})
    return jsonify({"Message": "Podcast not found or does not exist"})

## Update Podcast function.
@app.route('/podcast/update/<string:podcast_name>', methods=['PUT'])
@token_required
def editPodcast(podcast_name):
    PodcastFound = [podcast for podcast in results if (podcast['name'] == podcast_name or podcast['id'] == podcast_name)]
    if(len(PodcastFound) > 0):
        PodcastFound[0]['name'] = request.json['name'],
        PodcastFound[0]['artistName'] = request.json['artistName'],
        PodcastFound[0]['id'] = request.json['id']
        return jsonify({"message": "Podcast information updated", "podcast": PodcastFound[0]})
    return jsonify({"Message": "Podcast not found or does not exist"})

## Delete Podcast Function
@app.route('/podcast/delete/<string:podcast_name>', methods=['DELETE'])
@token_required
def deletPodcast(podcast_name):
    PodcastFound = [podcast for podcast in results if (podcast['name'] == podcast_name or podcast['id'] == podcast_name)]
    if (len(PodcastFound) > 0):
        results.remove(PodcastFound[0])
        return jsonify({"Message": "Podcast Deleted", "podcast": results})
    return jsonify({"Message": "Podcast not found or does not exist"})

## Create JSON file function
@app.route('/podcast/Top', methods=['POST'])
@token_required
def createJson():
    fh = open('Second-json.json', 'w')
    fh.write(json.dumps(results[:20]))
    fh.close()
    return 'Json file generated'


## Swap last 20 function



## Auth module
@app.route('/login')
def login():
    auth = request.authorization
    if auth and auth.password == 'password':
        token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=120)}, app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8')})
    return make_response('UNAUTHORIZED', 401, {'WWW-Authenticate': 'Basic realm = "Login Required"'})


if __name__ == "__main__":
    app.run(debug=True)