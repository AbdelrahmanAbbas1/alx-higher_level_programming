#!/usr/bin/node

if (!isNaN(parseInt(process.argv[3], 10))) {
  console.log(parseInt(process.argv[3], 10));
} else {
  console.log('Not a number');
}
