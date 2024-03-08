//jshint esversion:7

const mongoose = require("mongoose");

mongoose.connect("mongodb://localhost:27017/fruitsDB", {
  useNewUrlParser: true,
});

const fruitSchema = new mongoose.Schema({
  name: {
    type: String,
    required: [true, "No name specified"],
  },
  rating: {
    type: Number,
    min: 1,
    max: 10,
  },
  review: String,
});

const Fruit = mongoose.model("Fruit", fruitSchema);

const fruit = new Fruit({
  rating: 4,
  review: "Pretty solid as a fruit",
});

// fruit.save();
//

// Fruit.updateOne({ name: undefined }, { name: "jaimeLannister" }).then(
//   (data) => {
//     console.log(data);
//     finder();
//   }
// );

Fruit.deleteMany({ name: "Orange" }).then((data) => {
  console.log(data);
  finder();
});

function finder() {
  people.find().then((data) => {
    data.forEach((object) => {
      console.log(object.name);
    });
    mongoose.connection.close();
  });
}
