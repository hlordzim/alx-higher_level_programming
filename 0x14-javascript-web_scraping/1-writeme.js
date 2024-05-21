#!/usr/bin/node
/* script that writes a string to a file.*/

const fs = require('fs');


const args = process.argv.slice(2);
const filePath = args[0];
const content = args[1];

if (!filePath || !content) {
    console.log("Usage: node script.js <file_path> <content>");
    process.exit(1);
}

fs.writeFile(filePath, content, { encoding: 'utf8' }, (err) => {
    if (err) {
        console.error(`An error occurred: ${err}`);
        process.exit(1);
    } else {
        console.log(`Content written to ${filePath} successfully.`);
    }
});
