let user = JSON.parse(localStorage.getItem("richfieldUser"));

    if (user) {
      // Fill in the profile fields
      document.getElementById("profileName").innerText = user.name || "";
      document.getElementById("profileNumber").innerText = user.studentNumber || "";
      document.getElementById("profileCampus").innerText = user.campus || "";
      document.getElementById("profileEmail").innerText = user.email || "";
      document.getElementById("profileBio").innerText = user.bio || "";
      document.getElementById("profileInterests").innerText = user.interests || "";
    } else {
      // If no user data found
      document.querySelector(".profile-card").innerHTML = "<p>No profile data found. Please sign up first.</p>";
    }