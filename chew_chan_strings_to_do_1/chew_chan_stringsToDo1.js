// Remove Blanks

// Create a function that, 
// given a string, 
// returns all of that string’s contents, but without blanks.

function removeBlanks(str){
    //make new string
    let newString ="";
    //loop through the string
    for(let char in str){

        // if string doesn't have space
        if(str[char]!=" "){
        // add in new string
        newString += str[char];
        }
    }        
        // return newstring
    return newString;
}

let result=removeBlanks(" Pl ayTha tF u nkyM usi c ");
console.log (result);
let result1=removeBlanks("I can not BELIEVE it's not BUTTER");
console.log (result1);


// // Get Digits

// // Create a JavaScript function that given a string, 
// // returns the integer made from the string’s digits.

function getDigits(str){
    //make new string
    let newString ="";
    //loop through the string
    for(let char in str){
        // if string not a not number character
        if(!isNaN(str[char])){
        // add in new string
        newString += str[char];
        }
    }
    //convert string into number
    let Integer = Number(newString);    
        // return number
    return Integer;
}

let result2=getDigits("abc8c0d1ngd0j0!8");
console.log (result2);
let result3=getDigits("0s1a3y5w7h9a2t4?6!8?0");
console.log (result3);

// Acronyms

// Create a function that, 
// given a string, returns the string’s acronym (first letter of the word capitalized)

function Acronyms(str){
    //make new string
    let newString ="";
    // split the string into word array
    const wordsArray = str.split(' ');
    //loop through the array
    for(let word in wordsArray){
        //when array is not a space
        if(wordsArray[word]!=''){
            // add the first letter of each word in wordsArray into new string
            newString += wordsArray[word][0];
        }
    }
    //convert character into uppercase
    let upperCase = newString.toUpperCase();    
        // return 
    return upperCase;
}

let result4=Acronyms(" there's no free lunch - gotta pay yer way. ");
console.log (result4);
let result5=Acronyms("Live from New York, it's Saturday Night!");
console.log (result5);



// Count Non-Spaces

// Create a function that, given a string, 
// returns the number of non-space characters found in the string.

function countNonSpaces(str){
    //make a counter
    let counter =0;

    //loop through the string
    for(let char in str){
        // if string doesn't have space
        if(str[char]!=" "){
        // counter increment
        counter ++;
        }
    }        
        // return counter
    return counter;
}

let result6=countNonSpaces("Honey pie, you are driving me crazy");
console.log (result6);
let result7=countNonSpaces("Hello world !");
console.log (result7);


// Remove Shorter Strings

// Create a function that, given an array of strings and a numerical value, 
// returns an array that only contains strings longer than or equal to the given value. 

function removeShorterStrings(arr,val){
    //make new array
    let newArray =[];
    // make new index number
    let nextIndex=0;

    //loop through the array
    for(let word in arr){
        //if the length of the array is longer than or equal to given value
        if(arr[word].length >= val){
            // add the array into the new array
            newArray[nextIndex ++]=arr[word];
        }
    }

        // return 
    return newArray;
}

let result8=removeShorterStrings(['Good morning', 'sunshine', 'the', 'Earth', 'says', 'hello'], 4);
console.log (result8);
let result9=removeShorterStrings(['There', 'is', 'a', 'bug', 'in', 'the', 'system'], 3);
console.log (result9);