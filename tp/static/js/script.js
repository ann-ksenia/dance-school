var button = document.test.button;

  function change()
  {
    if (document.getElementById("Text").style.color=="blue"){
        document.getElementById("Text").style.color="black";
        document.getElementById("Text").style.fontFamily = "Arial";
    }
    else{
        document.getElementById("Text").style.color="blue";
        document.getElementById("Text").style.fontFamily="Verdana";
    }
  }

  button.addEventListener("click", change);