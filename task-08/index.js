var numberOfButtons = 
    document.querySelectorAll(".button").length;
  
for (var j = 0; j < numberOfButtons; j++) {
  
  document.querySelectorAll(".drum")[j]
  .addEventListener("click", function() {
  
    var buttonStyle = this.innerHTML;
    btnpress(buttonStyle);
  });
}

document.addEventListener("keypress", function(event) {
  btnpress(event.key);
});

function btnpress(letter){
  switch(letter) {
    case "w":

      var sound1 = new Audio("sounds/crash.mp3");
      sound1.play();
      break;

    case "a":
      
      var sound1 = new Audio("sounds/kick-bass.mp3");
      sound1.play();
      break;
    
      case "s":
      var sound3 = new Audio("sounds/snare.mp3");
      sound3.play();
      break;
    
    case "d":
      var sound4 = new Audio("sounds/tom-1.mp3");
      sound4.play();
      break;
    
    case "j":
      var sound5 = new Audio("sounds/tom-2.mp3");
      sound5.play();
      break;
    
    case "k":
      var sound6 = new Audio("sounds/tom-3.mp3");
      sound6.play();
      break;
    
    case "l":
      var sound7 = new Audio("sounds/tom-4.mp3");
      sound7.play();
      break;
  }
  
}

