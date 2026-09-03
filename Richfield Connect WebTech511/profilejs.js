//profile javascript coding
$(document).ready(function() {
  let user = JSON.parse(localStorage.getItem("richfieldUser"));
  if (user) {
    $("#profileContainer").html(`
      <h2>${user.name}</h2>
      <p><strong>Student Number:</strong> ${user.studentNumber}</p>
      <p><strong>Campus:</strong> ${user.campus}</p>
      <p><strong>Email:</strong> ${user.email}</p>
      <p><strong>Bio:</strong> ${user.bio}</p>
      <p><strong>Interests:</strong> ${user.interests}</p>
    `).hide().fadeIn(1000); // jQuery fade-in effect
  } else {
    $("#profileContainer").html("<p>No profile found. Please sign up first.</p>");
  }
});