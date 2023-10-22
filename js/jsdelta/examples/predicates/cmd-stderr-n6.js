#!/usr/bin/env node
var pred = require("./pred-n6.js");

//var mycnt=0;

function main() {
   var arg = process.argv[2];
   console.log(arg);
   
   var res = pred.test(arg);
   // res = false;

   if (res) {
      console.error("REPED");
   } else {
      console.log("not ok!");
   }
}

main();

