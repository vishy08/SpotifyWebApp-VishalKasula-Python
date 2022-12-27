import re
from flask import Flask, jsonify, request
from flask import send_file, redirect, url_for, render_template
import json, requests
import certifi

spotify_token = "BQDtxbPDRS41q6yisKUMWWiBfjqjQT0CtTrP0adlcPKqHDaQdM9C80oec7dnuQIlHhulyTowCzFoT5S-s9-JhO8JYz08Yb2a7iK9i9FzQhX9lxG4k-nAoKdCHjX7RQPECpkpU70ShrUIJVPAhIF8Hwue9nVn_qyU40NX3NbpQQKlw2hLmYsbJrdjK9EnHwIfmrdhjchRZGnH092UWEwQGR9NA0fLDIxVGREiAhys-S_GapaGGIYV-GNw9tdCXt6ECIpAhF_V9O-3fcUH"
#refresh_token = "AQBkNMTR67Z7B_aqbyrtW1K7GWeoR1Yb0JtdqwYQA_h4LlKulZtMr5vwwoe6yzG9osm2G6sCGReHWQvDlpepkskFHs-d6SO2BHuehTuWwjCSNqy36dYZclV8tXmbGzLWfNg"

app = Flask(__name__)

formData = {}

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == 'POST':
        playlistID = request.form['playlistId']
        offset = request.form['offset']
        formData['playlistID'] = playlistID
        formData['offset'] = str(offset)
        #return redirect(url_for('/me/top/<type>/<number>'))
        return send_file("second.html")
    else:
        return send_file("index.html")

@app.route("/me/top/<type>/<number>", methods=["GET"])
def topSongs(type, number):
    # find top song for given date
    #myHeader={"Authorization": "Bearer BQAZ0xp7yh7wCUU_8hVxfU0MVVGmJbFet9xdEuxEdxQOmNmjbBw-RjlhK-NqONiquBbYzaq7UhfFCxD071tttUTokQM_Q-JygygRtPVMjp5Bwse0oqDNtYviq9eOI16y-gnE1lsQjGHg06FOmc9TRd1_nTWdiOpnK1vMhTL3B4a-nYk6D1rc0DhTArRtZV3i5hDBY0wOioWttvUFt2pd-nAFZ3Y8FKtov3REI9bN11vCHZqwIiiapFygofI4v5FgHUb4XkILOqmBkqC-"}
    myHeader={"Content-Type": "application/json", "Authorization": "Bearer {}".format(spotify_token)}

    #myUrl = "https://api.spotify.com/v1/me/top/{}".format(type)
    myUrl = "https://api.spotify.com/v1/playlists/{}/tracks".format(type)

    response = requests.get(myUrl, headers=myHeader).json()
    intSize = 0
    fullnameList = ""
    nameArr = []
    for i in response["items"]:
        nameArr.append(i["track"]["name"])
        #fullnameList += i["track"]["name"]
    
    #for j in len(nameArr):
    stringPhrase = "Name song number {} as you requested: ".format(int(number))
    ret = {stringPhrase: nameArr[int(number)-1], "Now here are all songs on the playlist: ": nameArr}
    #ret = {'name': nameArr[number]}
    #return jsonify(ret)
    return jsonify(ret)

#@app.route("", methods=["POST"])
#def postRefresh():

if __name__ == '__main__':
    app.run(debug=True)