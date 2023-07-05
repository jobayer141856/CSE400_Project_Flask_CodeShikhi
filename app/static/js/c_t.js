// function mySyntex(){
//     var sidebar = document.querySelector("#sidebar")
//         sidebar.classList.toggle("active-nav")
//     var content = document.querySelector('.my-container1')
//         content.style.display ='none'
//         console.log(content)
//   }
var sidebar = document.querySelector("#sidebar")
var syntex = document.querySelector("#mySyntex")
syntex.addEventListener("click", () => {
    sidebar.classList.toggle("active-nav")
    var content = document.querySelector(".my-container1")
    content.style.display ='none'
    console.log(content)
})