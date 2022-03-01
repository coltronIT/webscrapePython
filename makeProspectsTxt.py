import json
from textwrap import indent
import requests
from requests.structures import CaseInsensitiveDict

with open('testRealFeb.txt', 'r') as f:
    numbur = 1
    with open('ProspectsGood.txt', 'w') as fun:
        for i in f:
            try:
                newI = i.strip().split(" ")
                lgplayername = newI[0]
                user = newI[1]
                status = newI[2]
                print(status)
                url = "https://proclubs.ea.com/api/nhl/members/search?platform=ps4&memberName=" + user
                headers = CaseInsensitiveDict()
                headers["user-agent"] = "Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
                headers["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
                resp = requests.get(url, headers=headers)
                uglyJson = resp.json()
                dumpedJson = json.dumps(uglyJson)
                y = {"lgplayername": lgplayername}
                ytwo = {"status": status}
                z = json.loads(str(dumpedJson))
                z["members"][0].update(y)
                z["members"][0].update(ytwo)
                ez = z["members"][0]
                numbur = numbur + 1
                fun.write(str(ez["skplayername"]) + "," + str(ez["gamesplayed"]) + "," + str(ez["skgoals"]) + "," + str(ez["skassists"]) + "," + str(ez["skplusmin"]) + "," + str(ez["skpim"]) + "," + str(ez["skhits"]) + "," + str(ez["glgp"]) + "," + str(ez["dgp"]) + "," + str(ez["rwgp"]) + "," + str(ez["cgp"]) + "," +
                          str(ez["lwgp"]) + "," + str(ez["glgaa"]) + "," + str(ez["glga"]) + "," + str(ez["glsaves"]) + "," + str(ez["glsavepct"]) + "," + str(ez["glso"]) + "," + str(ez["glsoperiods"]) + "," + str(ez["blazeId"]) + "," + str(ez["favoritePosition"]) + "," + str(ez["name"]) + "," + str(ez["lgplayername"]) + "," + str(ez["status"]) + "\n")
                print('got one' + ez["skplayername"] +
                      " " + ez["gamesplayed"] + " " + str(numbur) + status)
                numbur = numbur + 1
            except Exception as e:
                print('hi')

    f.close()
f.close()
