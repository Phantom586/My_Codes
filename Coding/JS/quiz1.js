var count = 0;
var q1 = prompt("What is the name of the language which is named on a species of snake ?");
if(q1.toLowerCase==="python"){
  count+=1;
}
var q2 = prompt("Who was the inventor of Kali Linux ?");
if(q2.toLowerCase==="linus"){
  count+=1;
}
var q3 = prompt("Who was the inventor of the C language ?");
if(q3.toLowerCase==="dennis"){
  count+=1;
}
document.write("<p> You've answered "+counter+" questions Correct.</p>");
if(count===3){
  document.write("<p><strong>Congrats ! You've won a Golden Crown</strong></p>");
}
else if(count>=1){
  document.write("<p><strong>You've a Silver Crown</strong></p>");
}
else{
  document.write("Sorry !! :-( try again next Time.");
}
