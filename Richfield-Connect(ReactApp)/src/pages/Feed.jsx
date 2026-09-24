import { useContext } from "react";

import AppContext from "../context/AppContext";

import CreatePost from "../components/CreatePost";
import PostCard from "../components/PostCard";

import "../styles/Feed.css";

function Feed() {
  const {
    posts,
    user,
  } = useContext(AppContext);

  if (!user) {
    return (
      <h2>
        Please register before accessing the feed.
      </h2>
    );
  }

  return (
    <div className="feed-page">

      <h1>Student Feed</h1>

      <CreatePost />

      <div className="posts-container">

        {posts.length === 0 ? (
          <p>
            No posts yet.
            Create First post!
          </p>
        ) : (
          posts.map((post) => (
            <PostCard
              key={post.id}
              post={post}
            />
          ))
        )}

      </div>

    </div>
  );
}

export default Feed;
``