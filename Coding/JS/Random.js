function ROLL(d){
  if(d==1){
  var s = prompt("Enter Your Predicted Number :");
  var c = Math.floor(Math.random()*6)+1;
  document.write(c);
  if(s==c){
    document.write("You've Won !!!Congatulations.");
  }
  else{
    document.write("Better Luck next Time :-(");
  }
}
}
