let buttonColours = ["red", "blue", "green", "yellow"];
var gamePattern = [];
var userClickedPattern = [];

var level = 0;
var gameOver = false;
var curr = 0;

// Just plays sound
function playSound(sound) {
  var sound = new Audio('sounds/'+sound+'.mp3');
  sound.play();
}

// Animates the button when user clicks
function animatePress(currentColor) {
  $('#'+currentColor).addClass("pressed");
  setTimeout(() => {
   $('#'+currentColor).removeClass("pressed"); 
  },100);
  
}

// Generates nextSequence of game
function nextSequence() { 
  level  += 1;
  $("#level-title").text("Level "+level);
  let x = Math.floor((Math.random() * 4));
  let randomChosenColour = buttonColours[x];
  gamePattern.push(randomChosenColour);
  $("#"+randomChosenColour).fadeOut(100).fadeIn(100);
}

// Checks weather the pattern entered by user is
// same as gamePattern
function check(color) {
  if (color == gamePattern[curr]) {
    curr  += 1;
    return true;
  }
  curr += 1;
  return false;
}

function game(userChosenColour) {
  
  if (check(userChosenColour) && gameOver == false) {
    if (gamePattern.length == userClickedPattern.length) {
      setTimeout(() => {
        nextSequence();
      }, 1000)
      userClickedPattern = [];
      curr = 0;
    }
    // pass
  }

  else {
    // Freak out
    $("#level-title").text("Game Over, Press Any Key to Restart");
    gameOver = true;
    $("body").addClass("game-over");
    setTimeout(() => {
      $("body").removeClass("game-over")
    }, 300);
    
  }
    
}

// When user clicks a button the sequence
// is pushed to userClickedPattern
$("div.btn").click(function() {
  if (gameOver == false) {
    let userChosenColour = this.id;
    userClickedPattern.push(userChosenColour);
    playSound(userChosenColour);
    animatePress(userChosenColour);
    game(userChosenColour);
    }
  }
);

$(document).on("keydown", function() {
  if ((level == 0) || (gameOver)) {
    userClickedPattern = [];
    gamePattern = [];
    level = 0;
    curr = 0;
    gameOver = false;
    nextSequence();
  }
  
})


