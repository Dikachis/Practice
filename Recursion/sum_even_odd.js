#!/usr/bin/node

/*A function (evaluateEven) that accepts an integer as a parameter,
if the integer is even the value return 'even' is returned,
otherwise the value of 'odd' is returned*/

const sum = (a, b) => a + b;

function evaluateEven(e) {
    if(e % 2 == 0)
    return "even";
    else "odd";
}

function sayHello(name, status) {
    const message = "Hi I am" + " " + name + " " + "and the number is" + " " + status;
    console.log(message);
}
sayHello("YourStackUpName", evaluateEven(sum(5, 3)));
