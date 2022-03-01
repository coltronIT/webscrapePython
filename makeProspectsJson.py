import json
from textwrap import indent
import requests
from requests.structures import CaseInsensitiveDict

with open('testRealFeb.txt', 'r') as f:
    hugeJson = []
    numbur = 1

    with open('feb.json', 'w') as fun:
        for i in f:
            def goofy():
                try:
                    newI = i.strip().split(" ")
                    lgplayername = newI[0]
                    user = newI[1]
                    status = str(newI[2])
                    print(newI)
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
                    hugeJson.append(z)
                except Exception as e:
                    print('skippin dis one tho' + str(e))
            goofy()
    f.close()
    fun.write(json.dumps(hugeJson))
f.close()
