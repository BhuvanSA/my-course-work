let buttonColours = ["red", "blue", "green", "yellow",]
var gamePattern = [];
var userClickedPattern = [];
var level = 0;

// Randomly choosed the next sequence and pushes
// it into a gamePattern array also blinks 
// function nextSequence() { 
//   level  += 1;
//   $("#level-title").text("Level "+level);
//   let x = Math.floor((Math.random() * 4));
//   let randomChosenColour = buttonColours[x];
//   gamePattern.push(randomChosenColour);
//   $("#"+randomChosenColour).fadeOut(100).fadeIn(100);
// }

// Just plays sound
// function playSound(sound) {
//   var sound = new Audio('sounds/'+sound+'.mp3');
//   sound.play();
// }

// Animates the button when user clicks
// function animatePress(currentColor) {
//   $('#'+currentColor).addClass("pressed");
//   setTimeout(() => {
//    $('#'+currentColor).removeClass("pressed"); 
//   },100);
//   
// }


function game() {
  if (JSON.stringify(gamePattern) === JSON.stringify(userClickedPattern)) {
    nextSequence();
    userClickedPattern = [];
  }

  else {
    $("#level-title").text("Game Over, Press Any Key to Restart");
    playSound("wrong");
    $("body").addClass("game-over");
    setTimeout(() => {
      $("body").removeClass("game-over");
    }, 200);
    level = 0;
    gamePattern = [];
    
  }
 
}

// Starts off the game
$(document).on("keydown", function(event) {
  if (level == 0) {
    nextSequence();
  }
});

// When user clicks a button the sequence
// is pushed to userClickedPattern
$("div.btn").click(function() {
  let userChosenColour = this.id;
  userClickedPattern.push(userChosenColour);
  playSound(userChosenColour);
  animatePress(userChosenColour);
  
  if (userClickedPattern.length == gamePattern.length) {
    game();
  }
});
