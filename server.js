'use strict';

const express = require('express');

const ping = require('ping');
// Constants
const PORT = process.env.PORT || 80;
const HOST = '0.0.0.0';

//
// App
const app = express();

//app.set('port', process.env.PORT);

app.get('/', (req, res) => {
  res.send('Hello world\n');
});

app.listen(PORT, HOST);

var hosts = ['192.168.33.11','192.168.33.12','192.168.33.13'];

var cron = require('node-cron')
cron.schedule('*/60 * * * * *', () => {  // 10 second cronjob to ping
    //console.log('Every 60 seconds');
    hosts.forEach(function (host) {
        ping.promise.probe(host,).then(function (res) {
                console.log(res);
        });
    });
});

console.log(`Running on http://${HOST}:${PORT}`);