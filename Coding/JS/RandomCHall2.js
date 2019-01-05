var n = parseInt(prompt("Enter m number"));
var m = parseInt(prompt("Enter n number"));
var p = Math.floor(Math.random()*(n-m+1))+m;
var msg = "<p>" + p + " is a Random Number Between "+ n + " and "+ m + " ,</p>";
document.write(msg);
