import "../styles/ProfilePreview.css"; //import css for profile preview

function ProfilePreview({ formData }) { //Profilepreview function declaration with formData as input
  return (
    <div className="preview-card">

      <h2>Live Profile Preview</h2>

      <div className="preview-avatar"> {/*Display username as initials*/}
        {formData.fullName
          ? formData.fullName
              .split(" ")
              .map(name => name[0])
              .join("")
              .toUpperCase()
          : "RG"}
      </div>

      <h3>
        {formData.fullName || "Your Name"} {/*Display full name from form data or "Your name" string if no data is filled yet*/}
      </h3>

      <p>{formData.campus || "Campus"}</p>{/*Display campus name selected by user.*/}

      <p className="preview-bio">
        {formData.bio || "Your bio will appear here..."}{/*Display BIO data*/}
      </p>

      <div className="interest-tags">{/*Display interests typed in in signup form*/}

        {formData.interests.map(interest => (
          <span
            key={interest}
            className="tag"
          >
            {interest}
          </span>
        ))}

      </div>

    </div>
  );
}

export default ProfilePreview;
