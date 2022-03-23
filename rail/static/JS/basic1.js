var downarrow = document.getElementById("down-arrow");
var logout = document.getElementById("logout");
      
downarrow.addEventListener("click",()=>{
    console.log("clicked");
    if(logout.style.display == "block"){
        logout.style.display = "none";
    }
    else
        logout.style.display = "block";
});


// active class 
var header = document.getElementById("navbar");
var btns = header.getElementsByClassName("search-option");
for (var i=0 ; i<btns.length ; i++){
    btns[i].addEventListener("click", function(){
        current = document.getElementsByClassName("active");
        if(current.length > 0){
                current[0].className += current[0].className.replace(" active","");
        }
        this.className += " active";
    });
}