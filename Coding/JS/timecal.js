var secondspermin = 60;
var minsperhour = 60;
var hoursperday = 24;
var dayinyear = 365;
var year  = prompt("Enter your Age ?");
var yearsAlive = secondspermin*minsperhour*hoursperday*dayinyear*year;
var cal = "You've Lived "+yearsAlive+" seconds.";
document.write(cal);
