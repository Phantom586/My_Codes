//Declaring Two Objects
var p1 = {name:"Harsh",marks:100,rank:1};
var p2 = {name:"Aayush",marks:99.99,rank:2};
//Create a Function That is going to work as your Methos for your Objects
function pDetails(){
  //It'll Show the Details of the Student
  document.write("<p>"+this.name+" has ranked: "+ this.rank +" and scored :"+this.marks+".</p>");
}
//Create and Method to Acess your created function.
p1.showDetails=pDetails;//showDetails is Just a Random Name you can choose your own Name for This.
p2.showDetails=pDetails;
//It's time to Call them
p1.showDetails();
p2.showDetails();
