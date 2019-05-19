
// This Program Shows the Working of the Labels in JavaScript.
Outer:for ( let i = 0; i < 4; i++ ) {
        for ( let j = 0; j < 4; j++ ) {
            console.log(` Iterating Through (${i}, ${j})`);
            if ( i == 3 && j == 3) break Outer; 
        }
    }
console.log("Outside the Loop");

// But these are not similar to Goto in C i.e., they can't jump anywhere in the program, they can only jump to a Label
// that is above them.