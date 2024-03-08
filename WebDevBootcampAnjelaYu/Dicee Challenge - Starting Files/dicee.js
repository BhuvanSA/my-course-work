const randomNo1 = Math.floor(Math.random() * 6) + 1;
const randomNo2 = Math.floor(Math.random() * 6) + 1;



var x = document.getElementById("img1");
var y = document.getElementById("img2");

x.src = "images/dice"+randomNo1 +".png";
y.src = "images/dice"+randomNo2 +".png";


