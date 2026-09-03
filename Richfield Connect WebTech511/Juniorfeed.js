//<!--feed java-->
let user = JSON.parse(localStorage.getItem("richfieldUser"));

    if (user) {
      // Fill in the profile fields
      document.getElementById("username").innerText = user.name || "";
    }

 // Like Functionality(*Appended)
let liked = false;
  let count = 0;

  function toggleLike() {
    const button = document.getElementById("likeButton");
    const counter = document.getElementById("likeCounter");

    if (!liked) {
      liked = true;
      count++;
      button.classList.add("liked");
      button.innerText = "👎 Unlike";
    } else {
      liked = false;
      count--;
      button.classList.remove("liked");
      button.innerText = "👍 Like";
    }

    counter.innerText = count;
  }

function updateDateTime() {
      const now = new Date();
      // Format:Wednesday, June 10, 2026, 14:17
      const options = {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
      };
      document.getElementById("dateTime").innerText = now.toLocaleString('en-US', options);
      document.getElementById("datetime").innerText = now.toLocaleString('en-US', options);
    }

    // Call once when page loads
    updateDateTime();

    // Optional: update every second
    setInterval(updateDateTime, 1000);
$(document).ready(function() {
  let user = JSON.parse(localStorage.getItem("richfieldUser"));
  let posts = JSON.parse(localStorage.getItem("richfieldPosts")) || [];
  let obj = JSON.parse(user);
  console.log(obj.studentNumber);
  console.log(obj.campus);
  console.log(obj.email);
  console.log(obj.bio);
  console.log(obj.interests);

  // Render posts from localStorage
  function renderPosts() {
    $("#feedContainer").empty();
    posts.forEach((post, index) => {
      $("#feedContainer").append(`
        <div class="post" data-index="${index}">
          <p><strong>${post.username}</strong> - ${post.timestamp}</p>
          <p>${post.content}</p>
          <button class="likeBtn ${post.liked ? 'liked' : ''}">
            ❤️ Like (<span class="likeCount">${post.likes}</span>)
          </button>
          <button class="deleteBtn">🗑 Delete</button>
        </div>
      `).children().last().hide().fadeIn(500); // fade-in effect
    });
  }

  renderPosts();

  // Create Post
  $("#postBtn").click(function() {
    if (!user) {
      alert("Please sign up first.");
      return;
    }
    let content = $("#postContent").val().trim();
    if (content) {
      let newPost = {
        username: user.name,
        timestamp: new Date().toLocaleString(),
        content: content,
        likes: 0,
        liked: false
      };
      posts.push(newPost);
      localStorage.setItem("richfieldPosts", JSON.stringify(posts));
      renderPosts();
      $("#postContent").val("");
    }
  });

 

  // Delete Post
  $("#feedContainer").on("click", ".deleteBtn", function() {
    let index = $(this).closest(".post").data("index");
    if (confirm("Delete this post?")) {
      posts.splice(index, 1);
      localStorage.setItem("richfieldPosts", JSON.stringify(posts));
      renderPosts();
    }
  });
});