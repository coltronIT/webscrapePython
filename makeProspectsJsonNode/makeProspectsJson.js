const fs = require('fs')
const EAurl = "https://proclubs.ea.com/api/nhl/members/search?platform=ps4&memberName="

/*   
 * step1 Read file save data
 * step2 foreach line retrieve EAdata from EA url + user
 * step3 combine read data and EAdata and export as json to new file
 */


// Step 1 (COMPLETE*)
fs.readFile('../testRealFeb.txt', 'utf8' , (err, data) => {
  if (err) {
    console.error(err)
    return
  }
	//(Do THIS *) should probably return data rather than console.log
  console.log(data)
})

// Step 2





// Step 3
fs.writeFile('cuteTEST.json', randomContent, err => {
  if (err) {
    console.error(err)
    return
  }
  //file written successfully
})


