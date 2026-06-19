let bulb = document.querySelector(".bulb");
let btn = document.querySelector("button");

btn.addEventListener("click",function(){
    if(bulb.classList.contains("bulb2")){
        bulb.classList.toggle("bulb2");
        btn.textContent = "ON";
    }
    else{
        bulb.classList.toggle("bulb2");
        btn.textContent = "OFF";
    }
});
