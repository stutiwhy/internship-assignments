// Question 1 : Multiplication Table Generator

for(let i = 1; i <= 10; i++){ // outer loop for first number of multiplication. 
    for(let ii = 1; ii <= 10; ii++){ // inner loop for the second number.
        console.log(i + " * " + ii + " = " + i * ii);
    }
}
// this way the multiplication tables of numbers 1 - 10 till the number 10 are printed.


// Question 2 : Sum of Numbers in an Array

let arr = [3, 6, 9, 12, 15, 18] // creating array.
sum = 0 // initializaing sum as zero.
for(i of arr){ // looping through all array elements.
    sum += i // adding current array element to sum.
}  
console.log("sum of array = " + sum) // printing results.


// Question 3 : Palindrome Checker

palindrome_check = (word) => {
    let len = word.length - 1 // initializing len to last char's index of word.
    for (let i = 0; i < word.length / 2; i++) { // looping through first half of word.
        if (word[i] != word[len]) { // comparing it with the second half of the word.
            return false
        }
        len-- // if char matches, then check the next char.
    }
    return true // all characters of first half match the second.
}
console.log(palindrome_check('stuti')) // false
console.log(palindrome_check('level')) // true


// Question 4 : Fibonacci Sequence Generator

fibo = (n) => {
    let sum, i, c // declaring variables.
    let a = 0 // first number of fibonacci series.
    let b = 1 // second number.
    let fibonacci = [a, b] // initializing it as first and second number.
    if(n <= 0) 
        return [0] // returning array with only zero if n is zero or negative.
    if(n == 1)
        return [0, 1] // returning array with only zero and one if n is 1.
    for(i = 2; i < n; i++){
        c = a + b // sum of last two numbers.
        a = b 
        b = c
        fibonacci.push(c) // pushing the added value to the array.
    }
    return fibonacci // returning the array.
}
let fibonacci = fibo(20) // storing the array in fibonacci variable.
console.log(fibonacci)


// Question 5 : Block Scope with Let and Const

// code block
if(true){
    // these are local variables, except var b.
    let a = "This is not a, inside the block." // block scoped.
    var b = "This is definitely not b, inside the block." // function scoped.
    const c = "This is absolutely not c, inside the block." // block scoped.
}

// console.log(a) // this causes error.

console.log(b) // this does not because it is default public i.e.
// if a variable is declared using var inside a code block, it is accessible even outside of it. 

// console.log(c) // this also causes error.

// all the variables below are of global scope because they are outside any block.
let d = "This is not d, outside the block."
var e = "This is definitely not e, outside the block."
const f =  "This is a f."

// another code block.
if(true){
    console.log(d)
    console.log(e)
    console.log(f)
}
// all the statements in the if block above execute flawlessly because global scope is accessible everywhere.

// lexical scope
function outer(){
    let a = 1
    function inner(){ // lexical scope means that inner functions can access local variables of outer functions. 
        let b = 10
        console.log(a + b)
    }
    // but outer functions cannot access the local variables of inner function.
    // console.log(b) // this will not work.
    inner()
}
// inner() // will cause error because it is a local function.
outer()