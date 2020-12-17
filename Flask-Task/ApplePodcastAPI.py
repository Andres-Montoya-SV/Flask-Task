from flask import Flask, request, jsonify, json
from flask_restful import Api
from PodcastFile import results, links, feed
import os

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

## Update Podcast function.
@app.route('/podcast/<string:podcast_name>', methods=['PUT'])
def editPodcast(podcast_name):
    PodcastFound = [podcast for podcast in results if (podcast['name'] == podcast_name or podcast['id'] == podcast_name)]
    if(len(PodcastFound) > 0):
        PodcastFound[0]['name'] = request.json['name'],
        PodcastFound[0]['artistName'] = request.json['artistName'],
        PodcastFound[0]['id'] = request.json['id']
        return jsonify({"message": "Podcast information updated", "podcast": PodcastFound[0]})
    return jsonify({"Message": "Podcast not found or does not exist"})

## Delete Podcast Function
@app.route('/podcast/<string:podcast_name>', methods=['DELETE'])
def deletPodcast(podcast_name):
    PodcastFound = [podcast for podcast in results if (podcast['name'] == podcast_name or podcast['id'] == podcast_name)]
    if (len(PodcastFound) > 0):
        results.remove(PodcastFound[0])
        return jsonify({"Message": "Podcast Deleted", "podcast": results})
    return jsonify({"Message": "Podcast not found or does not exist"})

## Create JSON file function
@app.route('/podcast/Top', methods=['POST'])
def createJson():
    fh = open('Second-json.json', 'w')
    fh.write(json.dumps(results[:20]))
    fh.close()
    return 'Json file generated'


## Swap last 20 from first 20 function


if __name__ == "__main__":
    app.run(debug=True)