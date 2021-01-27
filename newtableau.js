
// Select the button
var button = d3.select("#button");

// Select the form
var form = d3.select("#form");

// Create event handlers 
button.on("click", migrationCalculate);
form.on("submit", migrationCalculate);

function migrationCalculate(){
    var medincome, homeprice, umemployment, totalpop , usState, statekey;

    try
    {
        medincome = parseInt(document.getElementById('medIncome').value);
        homeprice= parseInt(document.getElementById('homePrice').value);
        umemployment = parseInt(document.getElementById('unEmployment').value);
        totalpop = parseInt(document.getElementById('Pop').value);
        usState = document.getElementByName('State')
        statekey = "Current residence in_" + usState
   
    if 

   }
   catch (e)
   {
        alert ('Exception Caught '+e);
     
}

//Get state values as well [switch, state is 1 ,else 0]
// easier to push to a dataframe [ selected state option will equal 1]
// var netMigration = (-0.44387379688931183(medincome) + 0.015972921446556314(homeprice)+ (-1797.7717263571649(umemployment)) + 0.004259499225071295(totalpop) +4600.38253616)

}