
// Functions is JavaScript can be Declared in Three Ways.

// First Way --> Function Declaration
function show() {
    console.log("This is just a Display Function Declaration.");
} 

// Second Way --> Function Expression
// Function Expressions are created when the execution reaches them. That would happen only in the line (*). Too late.

let display = function () {     // ----------------- (*)
    console.log("This is also a Display Function, but Function Expression.");
};
 //A Function Expression is used inside the statement: let sayHi = ...;, as a value.
 // It’s not a code block. The semicolon ; is recommended at the end of statements, no matter what is the value.
 // So the semicolon here is not related to the Function Expression itself in any way, it just terminates the statement.


// Third Way --> Arrow Functions
let disp = () => console.log("This is also a Display Function, but an Arrow Function.")

// We can also Write Multiline Arrow Functions.
let disp1 = (a, b, opn) => {
    if ( opn == "Add" ) console.log(a+b);
    else if ( opn == "Sub" ) console.log(a-b);
    else return console.log("Please Provide Some Operation to be Performed");
};


show();
display();
disp();
disp1(2, 3, "Add");

// Hence we can see Both are smililar in their working but not in their usages.


// As we know that if a function is declared in scope of some other code block then it is onlly accessible in that
// code block only so, 

// What can we do to make welcome visible outside of if?
// The correct approach would be to use a Function Expression and assign welcome to the variable that is declared
// outside of if and has the proper visibility.

let age = prompt("What is your age?", 18);

let welcome;

if (age < 18) {

  welcome = () => {
    alert("Hello!");
  };

} else {

  welcome = () => {
    alert("Greetings!");
  };

}

welcome(); // ok now