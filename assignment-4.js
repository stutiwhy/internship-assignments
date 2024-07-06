// Question 1
// Task: Write a function that takes an object and returns an array of the object's keys and values.

function getKeysAndValues(person) {
    let person_arr = [] // initializing empty array to store the keys and values 
    for (let k of Object.keys(person)) { // iterating through every key of the object
        person_arr.push([k, person[k]]) // pushing the values as [key, value] format in new array
    }
    return person_arr // returning the new array
}

let person = {name : 'Stuti', age : 17, hobby : 'sleep'}
console.log(getKeysAndValues(person)) // [ [ 'name', 'Stuti' ], [ 'age', 17 ], [ 'hobby', 'sleep' ] ]


// Question 2
// Task: Create a function to convert a string to title case.

function toTitleCase(inp_str) {
    let str = inp_str.toLowerCase().split(' ') // converting all chars of the string to lowercase and splitting each word
    let str_arr = [] // initializing empty array to store all the words which will later be joined to make a string

    for (let i of str) { // iterating through all words of the splitted lowercase array (string)
        // converting the first letter of char to uppercase and concatenating the rest of the word to it then pushing it into a new array
        str_arr.push(i.charAt(0).toUpperCase() + i.slice(1))
    }

    return str_arr.join(' ') // joining the new array with spaces in between each word to turn it back to string
}

console.log(toTitleCase("this is TO TITLE CaSe.")) // This Is To Title Case.


// Question 3
// Task: Implement a function that checks if an object is empty.

function isObjEmpty(obj) {
    let empty = false // creating new bool to store the result of empty or not
    if(Object.keys(obj).length == 0) // checking if the length of the object is zero
        empty = true // if it is, then result is set to true, else it stays false
    return empty
}

let person1 = {name : 'Stuti', age : 17, hobby : 'sleep'}
let not_person = {}

console.log(isObjEmpty(person1)) // false
console.log(isObjEmpty(not_person)) // true


// Question 4
// Task: Write a function to count the number of occurrences of each character in a string.

function countChars(word) {
    let char_count = {} // initializing empty obj to store the count of each char
    for(let i = 0; i < word.length; i++) { // looping through each occurence of the word
        let char = word[i]
        // if the current occurence doesn't already exist in obj its value is undefined, so it is added and its value incremented
        if(char_count[char] != undefined) { 
            char_count[char] += 1
        } else { // occurence already exists in obj and its value is incremented
            char_count[char] = 1
        }
    }
    return char_count
}

console.log(countChars("hheeelllllo ssstuuti")) // { h: 2, e: 3, l: 5, o: 1, ' ': 1, s: 3, t: 2, u: 2, i: 1 }