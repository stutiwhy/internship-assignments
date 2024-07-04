//  Question 1
// *Task:* Write a JavaScript function that takes an array of strings and returns a new array with each string capitalized.

function capitalizeStrings(words) {
    new_array = [] // initializing empty array to store capitalized words
    for(let i of words){ // looping through values of words
        new_word = i[0].toUpperCase() + i.slice(1) // changing first character of every word to upper case then concating them with the rest of the word
        new_array.push(new_word) // pushing the new word in the new array
    }
    return new_array // returning new array with capitalized words
}

const words = ["apple", "banana", "cherry", "stuti"]
console.log(capitalizeStrings(words)) // output will be : [ 'Apple', 'Banana', 'Cherry', 'Stuti' ]


// Question 2
// *Task:* Create a function that returns the second largest element in an array.

function secondLargest(arr) {
    if (arr.length < 2) {
        let str = "Please input a bigger array." // cannot find second largest element if array doesn't have more than 1 elements
        return str
    }
    arr.sort((a, b) => b - a) // sorting the array in descending order
    return arr[1] // returning the second element which will be the second largest element because of the sorting
}

const arr = [3, 1, 4, 2, 5]
console.log(secondLargest(arr)) // 4
const arr1 = [3]
console.log(secondLargest(arr1)) // Please input a bigger array.


// Question 3
// *Task:* Write a JavaScript function that takes an array of objects and a key, and returns an array of values corresponding to that key.

function getValuesByKey(objects, key) {
    // .map is looping through the objects in the array and the nameless function will return the value of the key to the array
    return objects.map(obj => obj[key]) // returning array of values
}

const objects = [{ name: "John", age: 25 }, { name: "Jane", age: 30 }, { name: "Jim", age: 20 }]
const key = "name"
console.log(getValuesByKey(objects, key)) // [ 'John', 'Jane', 'Jim' ]


// Question 4
// *Task:* Calculate the factorial of every element in an array and store it in a new array.

function factorial(n) { // function to calculate the factorial of every element
    let fact = 1 // needs to be 1 or answer will be zero
    for (let i = 1; i <= n; i++) { // iterating from 1 to n
        fact *= i // calculating the factorial of n by multiplying current result to i
    }
    return fact
}

function factorialArray(numbers) { // function that stores the factorials calculated in a new array
    let facts = [] // initializing empty array to store the factorials of all numbers
    for (let i in numbers) { // iterating through the number of numbers in array starting from zero and ending at n - 1
        facts.push(factorial(numbers[i])) // pushing the factorial in the new array
    }
    return facts
}

const numbers = [1, 2, 3, 4]
console.log(factorialArray(numbers)) // [ 1, 2, 6, 24 ]

// Question 5
// *Task:* Create a function to find the intersection of two arrays.

function intersection(arr1, arr2) {
    let new_arr = [] // initializing empty array to store the common array elements
    for (let i in arr1) { // iterating through the array indexes
        if (arr2.includes(arr1[i])) { // checking if the second array constains the arr1[i]th element or not
            new_arr.push(arr1[i]) // if yes, pushing that common element in the new array
        }
    }
    return new_arr // returning the new array with the common elements
}

const array1 = [1, 2, 3, 4]
const array2 = [3, 4, 5, 6]
console.log(intersection(array1, array2)) // [3, 4]
