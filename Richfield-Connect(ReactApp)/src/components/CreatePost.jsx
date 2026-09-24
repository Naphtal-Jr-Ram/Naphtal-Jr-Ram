import { useState, useContext } from "react"; //Importing two react hooks from react library
import AppContext from "../context/AppContext"; //Importing custom react context called appcontext

function CreatePost() { //declaration of function called createpost
  const { user, dispatch } = useContext(AppContext); //Accessing context data in AppContext

  const [content, setContent] = useState(""); //Create content and setcontent state variable 
  const [error, setError] = useState("");//Create error  and setError variables

  const handleSubmit = (e) => { //function handlesubmit declaration
    e.preventDefault(); //Prevention of default browser behaviour

    if (!content.trim()) { //if no data in variable content is detected
      setError("Post content cannot be empty."); //set an error
      return;
    }

    setError(""); //Otherwise, if there is data, setError to an empty string.

    const newPost = { //declaration of variable newPost
      id: crypto.randomUUID(), //Date and time Unique identifier
      username: user.fullName, //Populate user's name from user
      timestamp: new Date().toLocaleString(),//timestamp using local date
      content, //display content typed by user
      likes: 0, //set initial likes of post to zero
      liked: false,
    };

    dispatch({
      type: "ADD_POST",
      payload: newPost,
    });

    setContent("");
  };

  return (
    <form
      className="create-post"
      onSubmit={handleSubmit} //form declaration
    >
      <textarea //textarea for user content
        placeholder="Share an academic thought..."
        value={content}
        onChange={(e) =>
          setContent(e.target.value)
        }
      />

      {error && (
        <p className="error">
          {error}
        </p>
      )}

      <button type="submit"> 
        Post
      </button>
    </form>
  );
}

export default CreatePost;