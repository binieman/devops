'use strict';

const express = require('express');
const request = require('request')
const ping = require('ping');
const bodyParser = require('body-parser')
const app = express();
// Constants
const PORT = process.env.PORT || 80;
const HOST = '0.0.0.0';
var hosts = [];

app.listen(PORT, HOST);

app.use(bodyParser.urlencoded({extended :true}));
app.use(bodyParser.json());



// home
app.get('/', (req, res) => {
  res.send('Hello world\n');
});

// get method
app.get('/pong', (req, res) => {
  setTimeout(()=>{
    res.send('PONG');
  }, 10000); // timeout of 10 seconds to send pong response
});

// post route

function promiseGetPong(host){
  return new Promise((resolve,reject)=>{
    request.get('http://'+host+'/pong',(err,resp,body)=>{  
      if(err){
        reject(host+resp+err)
      }
      else{
        resolve(host)
      }
    }) 
  })
}

var success = []    // array to hold success 
var failed  = []    // array to hold failed
var promises = []   // array to hold promises

async function pingHosts(hosts){
  promises = []
  success =[]
  failed = []
  hosts.targets.forEach(host => {
    promises.push(promiseGetPong(host).then((value)=>{ // add all the promises to array
      console.log(value)
      success.push(`<${host} pong was successful>`);
    }).catch((err)=>{
      console.log(err)
      failed.push(`<${host} failed>`);
    }))

  });
}



app.post('/ping',(req,res)=>{
  hosts = req.body;
  pingHosts(hosts);
  console.log(hosts);

  // wait for all promises to be settled
  Promise.all(promises).then((result)=>{
    res.setHeader('Content-Type', 'application/json');
    // jsonify the succes and failed array
    var jsonRespose = JSON.stringify({"Success":success,"fail":failed})
    res.end(jsonRespose);
  })
})




console.log(`Running on http://${HOST}:${PORT}`);