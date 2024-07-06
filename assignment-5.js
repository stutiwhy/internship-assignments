// Question 1
// Task: Write a function that returns a closure which adds a specific number to its argument.

function addNumber(outer) {
    function addedNumber(inner) { // inner function that adds its argument to the argument of the outer function
        return inner + outer
    }
    return addedNumber // returning the inner function
}

const addNum = addNumber(181) // closure that stores the inner function
console.log(addNum(3287)) // using the closure


// Question 2
// Task: Create a function using closure to keep track of how many times it has been called.

function countingCalls() {
    let call_count = 0 // initializing initial call count
    function count() {
        call_count++ // incrementing count because function called
        console.log("function call count : " + call_count) // printing the call count
    }
    return count // returning the inner function (closure)
}

const counter = countingCalls() // creating closure
counter()
counter()
counter() // function call count : 3


// Question 3
// Task: Implement a prototype method to calculate the area of a rectangle object.

function areaOfRect(width, height) { // area of rectangle constructor
    this.width = width
    this.height = height
    // setting width and height of the instance
}

areaOfRect.prototype.area = function() { // new prototype method to calculate area of rectangle
    return this.width * this.height // using the arguments of areaOfRect in calculation
}

const rect = new areaOfRect(238, 52) // creating instance of the areaOfRect method
console.log("area of rectangle = " + rect.area()) // printing result by calling area prototype


// Question 4
// Task: Write a function to create an object and add methods using prototype to calculate perimeter and area of a circle.

function circle(r) {
    this.radius = r // setting value of the radius of instance
}

circle.prototype.area = function() { // prototype method to calculate area of circle
    return 3.14 * this.radius * this.radius // calculating area of the circle
}

circle.prototype.perimeter = function() { // prototype method to calculate perimeter of circle
    return 2 * 3.14 * this.radius // calculated area of the circle
}

const c = new circle(7.77) // creating new instance with radius passed as argument to circle constructor
console.log("area = " + c.area()) // area = 189.57090599999998
console.log("perimeter = " + c.perimeter()) // perimeter = 48.7956


// Question 5
// Task: Create a function that returns a set of functions that can increment, decrement, reset, and get the value of a private counter. Each function should be able to modify or access the private counter, demonstrating a more complex use of closures.

function privateCounter() {
    let count = 0 // initializing initial counter as zero

    // returning an object with functions to increment, decrement, reset, and get the value of the count
    return {
        increment : function() {
            count++ // increment
        },
        decrement : function() {
            count-- // decrement
        },
        reset : function() {
            count = 0 // resetting count to zero
        },
        getValue : function() {
            return count // returning the value of count
        }
    }
}

const count = privateCounter() // creating closure
count.increment() // incrementing count
console.log(count.getValue()) // getting the value of count

count.decrement() // decrementing count
console.log(count.getValue()) // 0

count.increment() 
console.log(count.getValue()) // 1

count.decrement() 
console.log(count.getValue()) // 0

count.increment() 
console.log(count.getValue()) // 1

count.increment() 
console.log(count.getValue()) // 2

count.decrement() 
console.log(count.getValue()) // 1

count.reset() // resetting count to zero
console.log(count.getValue()) // 0