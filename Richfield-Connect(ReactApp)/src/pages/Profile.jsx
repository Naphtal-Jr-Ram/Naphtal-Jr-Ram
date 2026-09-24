import { useContext } from "react"; //Import usecontext from react libraray
import AppContext from "../context/AppContext";// Import AppContext from context file

import "../styles/Profile.css"; // Import css styling for profile page

function Profile() {
  const { user, posts } =
    useContext(AppContext); //Accessing data in AppContext using user and post variables

  if (!user) { //If there is no user details
    return (
      <div className="no-profile">

        <h2>
          No Profile Found {/*Display ni profile/user details found*/}
        </h2>

        <p>
          Please register first.{/*Tell user to register first*/}
        </p>

      </div>
    );
  }

  const initials =
    user.fullName
      .split(" ")
      .map(
        (name) => name[0]
      )
      .join("")
      .toUpperCase(); //Display user full name as initials

  return (
    <div className="profile-page">

      <div className="profile-card">

        <div className="profile-avatar">
          {initials}
        </div>

        <h2>
          {user.fullName} {/*Display user full name*/}
        </h2>

        <p>
          <strong>
            Student Number:
          </strong>{" "}
          {user.studentNumber}{/*Display user student number under student number section*/}
        </p>

        <p>
          <strong>
            Campus:
          </strong>{" "}
          {user.campus}{/*Display campus chosen under campus label*/}
        </p>

        <p>
          <strong>
            Email:
          </strong>{" "}
          {user.email} {/*Display email*/}
        </p>

        <h3>Interests</h3>

        <div className="interest-tags">
          {user.interests.map(
            (interest) => (
              <span
                key={interest}
                className="tag"
              >
                {interest}
              </span>
            )
          )}
        </div>

        <h3>Bio</h3>

        <p>{user.bio}</p>

        <div className="stats">

  <div>
    <h3>{posts.length}</h3> {/*Display number of posts*/}
    <p>Posts</p>
  </div>

  <div>
    <h3>{user.interests.length}</h3>{/*Display number interests chosen as number of connections*/}
    <p>Connections</p>
  </div>

  <div>
    <h3>{user.interests.length}</h3>{/*Display number of interests as user number of bgroups.*/}
    <p>Groups</p>
  </div>

</div>
</div>
</div>
  );
}

export default Profile;
