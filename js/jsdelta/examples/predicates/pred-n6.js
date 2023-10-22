#!/usr/bin/env node
var pre_cnt = 0;
//const logging = require("./logging");

var execSucc = function (filename) {
    var process = require("child_process");
    var output = null;
    const options = {
        stdio: "pipe"
    };
    
    // return true;
    // console.log('"'+filename+'"');

    try {
	// output = process.execSync('node ' + filename, options);
        pre_cnt++;
        output = process.execSync('java -jar testjs-n.jar "$(cat ' + filename + ')"', options);	
	//console.log('finish');
	output = output.toString();
	
         // console.log(output);
	//console.log(out);
    } catch (err) {
        return false;
    }

    if (output === null) {
        return false;
    }
    
const regex1 = new RegExp("UNREACH", "g");
const count1 = (output.match(regex1) || []).length;
const regex2 = new RegExp("NEGATING", "g");
const count2 = (output.match(regex2) || []).length;

return (count1 >= 1) & (count2 >= 1);
};
exports.test = execSucc;
