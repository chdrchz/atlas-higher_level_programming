#!/usr/bin/node
const args_count = process.argv.length - 2 

if (args_count.length === 0) {
    console.log('No argument');
} else if (args_count.length === 1) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
