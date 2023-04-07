$(document).ready(function () {
  
    $(".nav-link").click(function (){
      $(this).addClass("active").siblings().removeClass("active");
    });
  });
  

  setTimeout(function() {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2000);