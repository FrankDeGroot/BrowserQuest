#!/usr/bin/env node
if (process.argv.length !== 4) {
    console.log('Specify in and out file')
    process.exit()
}
const expat = require('node-expat')
const fs = require('fs')
const parser = new expat.Parser('UTF-8')
const outStream = fs.createWriteStream(process.argv[3])
const elementStack = []
let separator = '';
console.time('parse')
outStream.write('{')
fs.createReadStream(process.argv[2]).pipe(parser).on('startElement', (name, attrs) => {
    convertInts(attrs)
    elementStack.push(name)
    const json = JSON.stringify(attrs)
    outStream.write(separator + '"' + name + '":' + json.substr(json, json.length - 1))
    // if (elementStack.length !== 0 && elementStack[elementStack.length - 1] === name) {
    // } else {
    // }
    separator = ','
}).on('endElement', function () {
    outStream.write('}')
    // if (elementStack.length !== 0) {
    //     elementStack.pop()
    // }
}).on('end', () => {
    outStream.write('}')
    console.timeEnd('parse')
    outStream.end()
}).on('error', (error) => {
    console.log(error)
    outStream.end()
})

function convertInts(attrs) {
    for (let attr in attrs) {
        let val = attrs[attr]
        if (!isNaN(val)) {
            attrs[attr] = +val
        }
    }
}
