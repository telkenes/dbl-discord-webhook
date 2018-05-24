var express = require('express');
var snekfetch = require('snekfetch')
var app = express();
var config = require('./config.json')

var webhookurl = config.webhookurl
var bodyParser = require('body-parser');
app.use(bodyParser.json()); 
app.use(bodyParser.urlencoded({ extended: true }));

app.use(express.static('public'));

app.get("/", function (req, res) {
  res.send("dis is not a website kthx")
});

app.post("/hook", function (req, res) {
  if (req.headers.authorization !== config.auth) return res.send({code: "invalid auth"})
    var user_id = req.body.user;
    var bot = req.body.bot;
  if (req.body.type === "test") {
    snekfetch.post(webhookurl).send({ "content": `<@${user_id}> voted <@${bot}> (This is a test)`}).then(r => {})
  } else {
    snekfetch.post(webhookurl).send({ "content": `<@${user_id}> voted <@${bot}>`}).then(r => {})
}
    res.send({code: "success"});
});

var listener = app.listen(process.env.PORT, function () {
  console.log('Your app is listening on port ' + listener.address().port);
});
