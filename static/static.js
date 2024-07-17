document.addEventListener("DOMContentLoaded", function(){
    const searchForm = document.querySelector("form");
    const searchInput = document.querySelector("#pswd");

    searchForm.addEventListener("submit", function(event){
        if(searchInput.ariaValueMax.trim()=== ""){
            event.preventDefault();
            alert("Please enter a keyword to search...");
        }



    } );
});