// Invoke Functions Call on Document Loaded
document.addEventListener('DOMContentLoaded', function () {
  hljs.highlightAll();
});


let alertWrapper = document.querySelectorAll('.alert'); 
let alertClose = document.querySelectorAll('.alert__close');

if(alertWrapper){ 
    // alertWrapper[0].style.display = 'none'
    for (let i = 0; i < alertClose.length; i++) {
      alertClose[i].addEventListener('click', function(){
      alertWrapper[i].style.display = 'none'});
    }
    
  } 