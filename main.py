from flask import Flask, jsonify, request
from flask import send_file
import json, requests
import certifi

spotify_token = "BQA5lG7hMb5NsCGVAmDlhVEE-dd9bHd1uUSJnFg8x3itOgzQUdLvdgrHJYts0GJG9hrDB1k5dFAjIlmz6gs_1Bir7p8GmJSb_35gOdu4H7cj-9Sk3TrDiSlvaqrUcbQT-Qcg0zFAq1G3DhLbhwH6c9r2uwXlqCWS9KZaX5-aBbuH7CG8Zf8DCjWesqm8gVGWODPHdaOQJoc9Mzkfv9AUG_qx8XuwGFhgNlRpg3PBH8rFP4t-K90lOCvsnDPCe4iJPO8bUdhIXJq14XXE"
#refresh_token = "AQBkNMTR67Z7B_aqbyrtW1K7GWeoR1Yb0JtdqwYQA_h4LlKulZtMr5vwwoe6yzG9osm2G6sCGReHWQvDlpepkskFHs-d6SO2BHuehTuWwjCSNqy36dYZclV8tXmbGzLWfNg"

app = Flask(__name__)
@app.route("/", methods=["GET"])
def main():
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