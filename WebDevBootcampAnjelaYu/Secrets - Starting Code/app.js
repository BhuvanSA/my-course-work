//jshint esversion:6

require("dotenv").config();
const express = require("express");
const mongoose = require("mongoose");
const saltRounds = 10;
const session = require("express-session");
const passport = require("passport");
const passportLocalMongoose = require("passport-local-mongoose");

const app = express();

app.set("view engine", "ejs");
app.use(express.static("public"));
app.use(express.urlencoded({ extended: true }));
app.use(
  session({
    secret: "Our little secret",
    resave: false,
    saveUninitialized: false,
  })
);
app.use(passport.initialize());
app.use(passport.session());

mongoose.connect("mongodb://localhost:27017/userDB");
// mongoose.set("useCreateIndex", true);

const userSchema = new mongoose.Schema({
  email: String,
  password: String,
});

userSchema.plugin(passportLocalMongoose);

const secret = process.env.SECRET;

const User = mongoose.model("User", userSchema);

passport.serializeUser(User.serializeUser());
passport.deserializeUser(User.deserializeUser());

app.get("/", function(req, res) {
  res.render("home");
});

app.get("/login", function(req, res) {
  res.render("login");
});

app.post("/login", function(req, res) {
  const username = req.body.username;
  const password = req.body.password;

  User.findOne({ email: username })
    .then((foundUser) => {
      if (!foundUser) {
        res.send("No user found Please register");
      } else {
        // do stuff
        bcrypt.compare(password, foundUser.password, function(err, result) {
          if (result === true) {
            res.render("secrets");
          }
        });
      }
    })
    .catch((err) => {
      res.send(err);
    });
});

app.get("/register", function(req, res) {
  res.render("register");
});

app.post("/register", function(req, res) {
  User.register({ username: req.body.username }, req, body.password).then().catch();


  const newUser = new User({
    email: req.body.username,
    password: hash,
  });

  newUser
    .save()
    .then(() => {
      // res.send("Succesfully saved  user");
      res.render("secrets");
    })
    .catch((err) => {
      res.send(err);
    });
});
});

app.listen(3000, function() {
  console.log("Server started on PORT 3000");
});
