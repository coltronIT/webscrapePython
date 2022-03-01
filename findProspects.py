from bs4 import BeautifulSoup
import requests

url = "https://www.leaguegaming.com/forums/index.php?leaguegaming/league&action=league&page=draftlist&leagueid=67&seasonid=19"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
players = doc.find_all(["a"], class_="userlevelid")
tr = doc.find_all(["tr"])
# deeperTr = tr[1]
# evenDeeperTr = deeperTr.find_all(["td"])[2]
# for td in evenDeeperTr:
#     print(td)

everythingArray = []
num = 0


for i in range(len(players)):
    # for i in range(85):

    player = players[i].string

    newUrl = "https://www.leaguegaming.com/forums/" + players[i]['href']
    newResult = requests.get(newUrl)
    newDoc = BeautifulSoup(newResult.text, "html.parser")
    banner = (newDoc.find(["div"], class_="team_banner_home"))
    gamesPlayedBigDiv = banner.find(["div"], class_="stat_hl_box")
    gamesPlayedLittleDiv = gamesPlayedBigDiv.find("span")
    try:
        gamesPlayed = int(gamesPlayedLittleDiv.string)
    except:
        gamesPlayed = "unknown"

    deeperTr = tr[i+1]
    evenDeeperTr = deeperTr.find_all(["td"])[1]
    evenDeeperTr = deeperTr.find_all(["td"])[2]
    for td in evenDeeperTr:
        gamertag = td.text
    evenDeeperTr = deeperTr.find_all(["td"])[5]
    for td in evenDeeperTr:
        consoleVersion = td.text
    evenDeeperTr = deeperTr.find_all(["td"])[6]
    for td in evenDeeperTr:
        status = td.text.strip()
    # evenDeeperTr = deeperTr.find_all(["td"])[3]
    # for td in evenDeeperTr:
    #     positionUgly = td.text
    #     size = len(positionUgly)
    #     # gets rid of the \n\t\t\t\t\t that's at the end of the position while scraping
    #     position = positionUgly[:size - 6]

    if ("PS5" in str(players[i].parent.parent)):
        consoleVersion = "PS5"
    elif ("PS4" in str(players[i].parent.parent)):
        consoleVersion = "PS4"
    # playerArray = [i, player, gamertag,
    #                position, gamesPlayed, consoleVersion]
    playerArray = [num, gamertag]
    playerGamerTag = (playerArray[1])

    with open('testRealFeb.txt', 'a') as f:
        try:
            if len(status) > 1:
                f.write(str(player) + " " + gamertag +
                        " " + str(status) + "\n")
            else:
                f.write(str(player) + " " + gamertag + " " + "none" + "\n")
            print("yesProspect" + gamertag +
                  str(gamesPlayed) + "length of status:          " + str(len(status)) + "status:       " + str(status) + consoleVersion)
            num = num + 1
        except:
            print("")

print("All Done grabbing as many names as I can that are ps4")
