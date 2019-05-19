
// This Script Demostrates Objects in JavaScript.

let person = {};

// adding Properties of a Person
person.sex = "male";
person.age = 24;
person.hair = "curly";

// assign multiword property-name
person["likes Football"] = true;

// console.log(person.sex);
// console.log(person.age);
// console.log(person.hair);
// console.log(person["likes Football"]);

// checking if the specified property exists or not.
// let gender = "sex";
// console.log("sex" in person);
// console.log(gender in person);
// console.log("height" in person);


// if the keys are non-integer, then they are listed in the creation order.
// in Case for Integers the keys are Sorted.

// For In Loop
for (let keys in person) {
    console.log(person[keys]);
}