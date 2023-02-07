document.addEventListener("DOMContentLoaded", function(e){
    const dropDownGid = document.getElementsByClassName('clicked')
    const buttons = document.getElementsByClassName("pointer");

    function dropDown(){
      for (const element of Array.from(dropDownGid)){
        if (element.style.display === "block"){
          element.style.display = "none";
        }else{
          element.style.display = "block";
        }
      }
    }

    for (const button of Array.from(buttons)) {
      button.addEventListener("click", dropDown);
    }
  })

  //All classes open when you click on one