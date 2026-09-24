import {
  createContext,
  useReducer,
  useEffect
} from "react";

export const AppContext = createContext();

const initialState = {
  user: null,
  posts: []
};

function appReducer(state, action) {

  switch (action.type) {

    case "LOAD_DATA":
      return {
        ...state,
        user: action.payload.user,
        posts: action.payload.posts
      };

    case "REGISTER_USER":
      return {
        ...state,
        user: action.payload
      };

    case "ADD_POST":
      return {
        ...state,
        posts: [action.payload, ...state.posts]
      };

    case "TOGGLE_LIKE":
      return {
        ...state,
        posts: state.posts.map(post =>
          post.id === action.payload
            ? {
                ...post,
                liked: !post.liked,
                likes: post.liked
                  ? post.likes - 1
                  : post.likes + 1
              }
            : post
        )
      };

    case "DELETE_POST":
      return {
        ...state,
        posts: state.posts.filter(
          post => post.id !== action.payload
        )
      };

    default:
      return state;
  }
}

export function AppProvider({ children }) {

  const [state, dispatch] =
    useReducer(appReducer, initialState);

  useEffect(() => {

    const savedUser =
      JSON.parse(
        localStorage.getItem("richfieldUser")
      ) || null;

    const savedPosts =
      JSON.parse(
        localStorage.getItem("richfieldPosts")
      ) || [];

    dispatch({
      type: "LOAD_DATA",
      payload: {
        user: savedUser,
        posts: savedPosts
      }
    });

  }, []);

  useEffect(() => {

    localStorage.setItem(
      "richfieldUser",
      JSON.stringify(state.user)
    );

  }, [state.user]);

  useEffect(() => {

    localStorage.setItem(
      "richfieldPosts",
      JSON.stringify(state.posts)
    );

  }, [state.posts]);

  return (
    <AppContext.Provider
      value={{
        user: state.user,
        posts: state.posts,
        dispatch
      }}
    >
      {children}
    </AppContext.Provider>
  );
}