const testPlayers = require("./lovely.json");
const fs = require("fs");

let numbr = 1;
testPlayers.forEach((player) => {
  const { members } = player;
  const {
    skplayername,
    gamesplayed,
    skgoals,
    skassists,
    skplusmin,
    skpim,
    skhits,
    glgp,
    dgp,
    rwgp,
    cgp,
    lwgp,
    glgaa,
    glga,
    glsaves,
    glsavepct,
    glso,
    glsoperiods,
    blazeId,
    favoritePosition,
    name,
  } = Object(members[0]);
  console.log(skplayername);

  const doggyPile = [
    skplayername,
    gamesplayed,
    skgoals,
    skassists,
    skplusmin,
    skpim,
    skhits,
    glgp,
    dgp,
    rwgp,
    cgp,
    lwgp,
    glgaa,
    glga,
    glsaves,
    glsavepct,
    glso,
    glsoperiods,
    blazeId,
    favoritePosition,
    name,
  ];
  fs.appendFile("./justForMaggie.txt", doggyPile.toString() + "\n", (err) => {
    if (err) {
      console.log(numbr, "this was an error");
      numbr = numbr + 1;
    } else {
      console.log(numbr, "success");
      numbr = numbr + 1;
    }
  });
});
// console.log(customer[0].members.length);
