//jshint esversion:6

const express = require("express");
const app = express();

app.listen(3000, function () {
  console.log("server started on port 3000");
});

app.get("/", function (req, res) {
  res.send("Hello World");
});

app.get("/contact", function (req, res) {
  res.send("Contact me at: bhuvansa.tk");
});

app.get("/about", function (req, res) {
  res.send("Life is this _ and I need this -");
});
