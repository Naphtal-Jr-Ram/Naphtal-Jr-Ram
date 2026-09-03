$(document).ready(function(){
  $("#signupForm").on("submit", function(e){
    e.preventDefault();
    let valid = true;

    // Validation
    if($("#name").val().trim() === ""){
      $("#nameError").text("Name required");
      valid = false;
    } else { $("#nameError").text(""); }

    if(isNaN($("#studentNumber").val())){
      $("#studentError").text("Student number must be numeric");
      valid = false;
    } else { $("#studentError").text(""); }

    let emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
    if(!emailPattern.test($("#email").val())){
      $("#emailError").text("Invalid email");
      valid = false;
    } else { $("#emailError").text(""); }