process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function (data) {
    input_stdin += data;
});

process.stdin.on('end', function () {
    input_stdin_array = input_stdin.split("\n");
    main();    
});

function readLine() {
    return input_stdin_array[input_currentline++];
}

/////////////// ignore above this line ////////////////////

function computeHCF(x,y){
    return !y ? x : computeHCF(y, x % y);
}

function computeLCM(x,y){
    return (x*y) / computeHCF(x,y);
}

function main() {
    var t = parseInt(readLine());
    for(var a0 = 0; a0 < t; a0++){
        var n = parseInt(readLine());
        var arr = Array.apply(null, {length : n + 1}).map(Number.call, Number).splice(1);
        var multiple = 1;
        arr.forEach(function(a){
            multiple = computeLCM(multiple, a);
        });
        console.log(multiple);
    }

}