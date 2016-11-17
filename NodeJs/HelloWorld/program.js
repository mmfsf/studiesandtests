var arr = process.argv;
var result = 0;
for (var index = 2; index < arr.length; index++){
	result += Number(arr[index]);
}

console.log(result);