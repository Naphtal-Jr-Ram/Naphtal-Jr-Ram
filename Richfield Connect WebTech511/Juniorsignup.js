$(document).ready(function() {
  // Live preview updates
  $("#name").on("input", function() {
    $("#previewName").text($(this).val());
  });

  $("#bio").on("input", function() {
    $("#previewBio").text($(this).val());
  });

  $("#interests").on("input", function() {
    let interests = $(this).val().split(",");
    $("#previewInterests").empty();
    interests.forEach(i => {
      $("#previewInterests").append(`<span class="tag">${i.trim()}</span> `);
    });
  });

  // Form validation and storage
  $("#signupForm").on("submit", function(e) {
    e.preventDefault();
    let valid = true;

    $(".error").text(""); // reset errors

    if ($("#name").val().trim() === "") {
      $("#name").next(".error").text("Name required");
      valid = false;
    }
    if (!/^\d+$/.test($("#studentNumber").val())) {
      $("#studentNumber").next(".error").text("Must be numeric");
      valid = false;
    }
    if ($("#password").val().length < 8) {
      $("#password").next(".error").text("Min 8 characters");
      valid = false;
    }
    if ($("#password").val() !== $("#confirmPassword").val()) {
      $("#confirmPassword").next(".error").text("Passwords must match");
      valid = false;
    }

    if (valid) {
      let user = {
        name: $("#name").val(),
        studentNumber: $("#studentNumber").val(),
        campus: $("#campus").val(),
        email: $("#email").val(),
        interests: $("#interests").val(),
        bio: $("#bio").val()
      };
      localStorage.setItem("richfieldUser", JSON.stringify(user));
      window.location.href = "profile.html";
    }
  });
});