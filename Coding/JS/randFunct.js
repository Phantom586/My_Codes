var m,n;
m = prompt("Enter a start range");
n = prompt("Enter a end range");

function Random(m,n){
  var m;var n;
  if(isNAN(m) || isNAN(n)){
    throw new Error("Please Input an Integer Value !!");
  }
  var r = Math.floor(Math.random()*(m-n+1))+n;
  return r;
}
console.log(Random(m,n));
