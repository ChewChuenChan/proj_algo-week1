// push font
function pushFront(arr,elem){
    arr.push(elem); // push method adds one element to the end of the array and returns in the new length of the array; ie 8 push in the array [5,7,2,3], returns in [5,7,2,3,8]
    for (var i =0; i < arr.length-1; i++){ // start the for loop as i =0
        var temp = arr[i]; // save the first element of array into temp, in this case temp = arr[0], which is temp=5
        arr[i]=arr[arr.length-1]; // change the last element of arrange into first element; so arr[0]=arr[4], arr[0]=8
        arr[arr.length-1]=temp; // the first element swaps to last element; so arr[4]=5
        //so now the array is [8,7,2,3,5]
        //when i =1
        //temp =arr[1]=7
        //arr[1]=arr[4]=5
        //arr[4]=7
        // so now the array is [8,5,2,3,7]
        // when i =2
        // temp = arr[2]=2
        // arr[2]=arr[4]=7
        // arr[4]=2
        // so now the array is [8,5,7,3,2]
        // when i =3
        // temp=arr[3]=3
        //arr[3]=arr[4]=2
        //arr[4]=3
        // so now the array is [8,5,7,2,3]
    }
    console.log(arr);
}

pushFront([5,7,2,3],8);
pushFront([99],7);

//Pop Front
function popFront(arr){
    var temp =arr[0]; // save the first element of the array in temp
    for(var i=1; i<arr.length; i++){ // set for loop and shirt the element of array into left side
        arr[i-1]=arr[i]; //arr[0]=arr[1], arr[1]=arr[2].. stop at i < arr.length
    }
    arr[arr.length-1]=temp; // set  temp in the last element of the array 
    console.log(arr.pop()); // pop method removes the last element from the array and returns that element, console.log print the pop out element out.
    console.log(arr);
}

popFront([0,5,10,15]);
popFront([4,5,7,9]);


//Insert At
function insertAt(arr,index,elem){
    arr.push(elem); 
    for (var i =index; i < arr.length-1; i++){ 
        var temp = arr[i]; 
        arr[i]=arr[arr.length-1]; 
        arr[arr.length-1]=temp; 
    }
    console.log(arr);
}

insertAt([100,200,5],2,3);
insertAt([9,33,7],1,42);

//Remove At
function removeAt(arr,index){
    var temp = arr[index];
    for(var i = index +1; i < arr.length; i++){
        arr[i-1]=arr[i];
    }
    arr[arr.length-1]=temp;
    console.log(arr.pop());
    console.log(arr);
}

removeAt([1000,3,204,77],1);
removeAt([8,20,55,44,98],3);

//Swap Pairs
function swapPairs(arr){
    for (var i =0; i < arr.length-1; i=i+2){ 
        var temp=arr[i];
        arr[i]=arr[i+1];
        arr[i+1]=temp;
    }
    
    console.log(arr);
}

swapPairs([1,2,3,4]);
swapPairs(["Brendan",true,42]);


//removeDupes
function removeDupes(arr){
    const unique=[];
    for(var i=0; i< arr.length;i ++){
        if(arr[i]!=arr[i+1]){
        unique.push(arr[i]);}
        }
        console.log(unique);
    
    }
    
    removeDupes([-2,-2,3.14,5,5,10]);
    removeDupes([9,19,19,19,19,19,29]);