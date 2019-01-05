var q = 3;
var qleft ='['+ q + ' questions left]';
var q1 = prompt("Enter First number " + qleft);
q -=1;
qleft ='['+ q + ' questions left]';
var q2 = prompt("Enter second number " + qleft);
q -= 1;
document.write("<p>"+"Press 1 for Addition"+"</p>");
document.write("<p>"+"Press 2 for Subtraction"+"</p>");
document.write("<p>"+"Press 3 for Multiplication"+"</p>");
document.write("<p>"+"Press 4 for Division"+"</p>");
qleft ='['+ q + ' questions left]';
var q3 = prompt("Enter Your Operation" + qleft);
if(q3==1){
var a = parseInt(q1)+parseInt(q2);
document.write("Addition of the numbers is :"+a);
}
else if(q3==2){
  var s = parseInt(q1)-parseInt(q2);
  document.write("Subtraction of the numbers is :"+s);
}
else if(q3==3){
  var m = parseInt(q1)*parseInt(q2);
  document.write("Multiplication of the numbers is :"+m);
}
else{
  var d = parseInt(q1)/parseInt(q2);
  document.write("Division of the numbers is :"+d);
}
