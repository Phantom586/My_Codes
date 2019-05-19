function pow(x, n) {

    if ( n < 0) return NaN;
    if (Math.round(n) != n) return NaN;

    let result = 1;
    for(let y = 0; y < n; y++) {
        result *= x;
    }
    return result;
}

// function checkName() {

//     let name = prompt("Enter Your Name :");
//     if (name == "Harsh" ) {
//         // console.log(`Welcome Sir! ${name}`);
//         return true;
//     } else {
//         // console.log("You are not Authorized to View this Page!!!");
//         return false;
//     }
    
// }