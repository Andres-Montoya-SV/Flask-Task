from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from PodcastFile import results, links, feed

app = Flask(__name__)
api = Api(app)

@app.route('/', methods=['GET', 'POST'])
def getPodcast():
    return jsonify(feed, links, results)

## Podcast filter finder function.
@app.route('/podcast/<string:podcast_name>')
def PodcastFilter(podcast_name):
    PodcastFound = [podcast for podcast in results if (podcast['name'] == podcast_name or podcast['artistName'] == podcast_name)]
    if (len(PodcastFound) > 0):
        return jsonify({"Podcast found": PodcastFound[0]})
    return jsonify({"Message": "Podcast not found or does not exist"})

if __name__ == "__main__":
    app.run(debug=True)