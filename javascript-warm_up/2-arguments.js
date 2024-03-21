#!/usr/bin/node
const args_count = process.argv.length - 2 

if (args_count === 0) {
    console.log('No argument');
} else if (args_count === 1) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
