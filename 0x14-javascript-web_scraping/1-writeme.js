#!/usr/bin/node

const fs = require('fs');
filePath = process.argv[2];
data = process.argv[3];

fs.writeFile(filePath, data, (err) => {
  if (err) {
    console.log(err);
  }
});
