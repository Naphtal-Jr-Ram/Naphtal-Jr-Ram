import { useContext } from "react"; //Import react element from react
import AppContext from "../context/AppContext"; //Import AppComtext from AppContext.jsx

function PostCard({ post }) { //PostCard function declaration
  const { dispatch } = useContext(AppContext); //Accessing data in AppContext file

  const handleLike = () => {
    dispatch({
      type: "TOGGLE_LIKE",
      payload: post.id,
    });
  };

  const handleDelete = () => {
    const confirmation =
      window.confirm(
        "Delete this post?"
      );

    if (confirmation) {
      dispatch({
        type: "DELETE_POST",
        payload: post.id,
      });
    }
  };

  return (
    <div className="post-card">

      <div className="post-header">
        <h3>{post.username}</h3> {/*Display username*/}

        <p>
          {post.timestamp} {/*Display date-time stamp*/}
        </p>
      </div>

      <p className="post-content">
        {post.content} {/*Display content from post*/}
      </p>

      <div className="post-actions">

        <button
          className={
            post.liked
              ? "liked-btn"
              : "like-btn"
          }
          onClick={handleLike}
        >
          👍 {post.likes}
        </button>

        <button
          className="delete-btn"
          onClick={handleDelete} //{/*Post deletion button*/}
        >
          Delete
        </button>

      </div>

    </div>
  );
}

export default PostCard;