#!/usr/bin/env node
var pred = require("./pred-n2.js");

//var mycnt=0;

function main() {
   var arg = process.argv[2];
   console.log(arg);
   
   var res = pred.test(arg);
   // res = false;
   
   //mycnt++;
   //console.error("cnt=" + mycnt+"\n");
   if (res) {
      console.error("REPED");
   } else {
      console.log("not ok!");
   }
}

main();

