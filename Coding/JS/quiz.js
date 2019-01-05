//set count to zero
var count = 0;
//Ask a question,and if it is correct update the counter by 1.
var q1 = prompt("What is the name of the language which is named on a species of snake ?");
if(q1.toLowerCase==="python"){
  count+=1;
}
var q2 = prompt("Who was the inventor of Kali Linux ?");
if(q2.toLowerCase==="linustorvalds"){
  count+=1;
}
var q3 = prompt("Who was the inventor of the C language ?");
if(q3.toLowerCase==="dennisritchie"){
  count+=1;
}
var q4 = prompt("When was the C Language Invented ?");
if(q4=="1972"){
  count+=1;
}
var q5 = prompt("Where was it Invented ?");
if(q5.toLowerCase==="at&tlaboratories"){
  count+=1;
}
var q6 = prompt("Which is the Best Operating System ?");
if(q6.toLowerCase==="linux"){
  count+=1;
}
//Output The nouber of Correct Questions
document.write("<p> You've answered "+counter+" questions Correct.</p>");
//Compare the total count value to print the Result
if(count===6){
  document.write("<p><strong>Congrats ! You've won a Golden Crown</strong></p>");
}
else if(count>=3){
  document.write("<p><strong>You've a Silver Crown</strong></p>");
}
else if(count>=1){
  document.write("<p><strong>You've a Bronze Crown</strong></p>");
}
else{
  document.write("Sorry !! :-( try again next Time.");
}
