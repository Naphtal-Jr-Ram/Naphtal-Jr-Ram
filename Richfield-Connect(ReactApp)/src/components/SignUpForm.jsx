import { useState, useContext } from "react";
import { useNavigate } from "react-router-dom";

import AppContext from "../context/AppContext";
import ProfilePreview from "./profilepreview";

import "../styles/Signup.css";

function SignUpForm() {
  const navigate = useNavigate();

  const { dispatch } = useContext(AppContext);

  const [formData, setFormData] = useState({
    fullName: "",
    studentNumber: "",
    campus: "",
    email: "",
    password: "",
    confirmPassword: "",
    interests: [],
    bio: "",
    terms: false,
  });

  const [errors, setErrors] = useState({});

  const validateField = (name, value) => {
    let error = "";

    switch (name) {
      case "fullName":
        if (!value.trim()) {
          error = "Full Name is required";
        }
        break;

      case "studentNumber":
        if (!/^\d+$/.test(value)) {
          error = "Student Number must contain numbers only";
        } else if (value.length < 6) {
          error = "Student Number must be at least 6 digits";
        }
        break;

      case "campus":
        if (!value) {
          error = "Please select a campus";
        }
        break;

      case "email":
        if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)) {
          error = "Enter a valid email address";
        }
        break;

      case "password":
        if (value.length < 8) {
          error = "Password must be at least 8 characters";
        }
        break;

      case "confirmPassword":
        if (value !== formData.password) {
          error = "Passwords do not match";
        }
        break;

      case "bio":
        if (value.trim().length < 20) {
          error = "Bio must contain at least 20 characters";
        }
        break;

      default:
        break;
    }

    setErrors((prev) => ({
      ...prev,
      [name]: error,

    }));

    return error;
  };

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;

    if (type === "checkbox") {
      if (name === "terms") {
        setFormData((prev) => ({
          ...prev,
          terms: checked,
        }));
      } else {
        let updatedInterests = checked
          ? [...formData.interests, value]
          : formData.interests.filter(
              (interest) => interest !== value
            );

        setFormData((prev) => ({
          ...prev,
          interests: updatedInterests,
        }));
      }
    } else {
      setFormData((prev) => ({
        ...prev,
        [name]: value,

      }));
    }
  };

  const handleBlur = (e) => {
    validateField(e.target.name, e.target.value);
  };

  const validateForm = () => {
    const newErrors = {};

    newErrors.fullName =
      formData.fullName.trim() === ""
        ? "Full Name is required"
        : "";

    newErrors.studentNumber =
      /^\d+$/.test(formData.studentNumber) &&
      formData.studentNumber.length >= 6
        ? ""
        : "Invalid Student Number";

    newErrors.campus =
      formData.campus === ""
        ? "Please select a campus"
        : "";

    newErrors.email =
      /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)
        ? ""
        : "Invalid Email Address";

    newErrors.password =
      formData.password.length >= 8
        ? ""
        : "Password must be at least 8 characters";

    newErrors.confirmPassword =
      formData.password === formData.confirmPassword
        ? ""
        : "Passwords do not match";

    newErrors.interests =
      formData.interests.length > 0
        ? ""
        : "Select at least one interest";

    newErrors.bio =
      formData.bio.trim().length >= 20
        ? ""
        : "Bio must be at least 20 characters";

    newErrors.terms =
      formData.terms
        ? ""
        : "You must accept the Terms and Conditions";

    setErrors(newErrors);

    return !Object.values(newErrors).some(
      (error) => error !== ""
    );
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!validateForm()) {
      return;
    }

    const userProfile = {
      fullName: formData.fullName,
      studentNumber: formData.studentNumber,
      campus: formData.campus,
      email: formData.email,
      interests: formData.interests,
      bio: formData.bio,
    };

    dispatch({
      type: "REGISTER_USER",
      payload: userProfile,
    });

    localStorage.setItem(
      "richfieldUser",
      JSON.stringify(userProfile)
    );

    navigate("/profile");
  };

  return (
    <div className="signup-layout">

      <form
        className="signup-form"
        onSubmit={handleSubmit}
      >
        <h2>Student Registration</h2>

        <input
          type="text"
          name="fullName"
          placeholder="Full Name"
          value={formData.fullName}
          onChange={handleChange}
          onBlur={handleBlur}
        />
        <span className="error">
          {errors.fullName}
        </span>

        <input
          type="text"
          name="studentNumber"
          placeholder="Student Number"
          value={formData.studentNumber}
          onChange={handleChange}
          onBlur={handleBlur}
        />
        <span className="error">
          {errors.studentNumber}
        </span>

        <select
          name="campus"
          value={formData.campus}
          onChange={handleChange}
          onBlur={handleBlur}
        >
          <option value="">
            Select Campus
          </option>

          <option value="Pretoria">
            Pretoria
          </option>

          <option value="Johannesburg">
            Johannesburg
          </option>

          <option value="Polokwane">
            Polokwane
          </option>

          <option value="Durban">
            Durban
          </option>
        </select>

        <span className="error">
          {errors.campus}
        </span>

        <input
          type="email"
          name="email"
          placeholder="Email Address"
          value={formData.email}
          onChange={handleChange}
          onBlur={handleBlur}
        />
        <span className="error">
          {errors.email}
        </span>

        <input
          type="password"
          name="password"
          placeholder="Password"
          value={formData.password}
          onChange={handleChange}
          onBlur={handleBlur}
        />
        <span className="error">
          {errors.password}
        </span>

        <input
          type="password"
          name="confirmPassword"
          placeholder="Confirm Password"
          value={formData.confirmPassword}
          onChange={handleChange}
          onBlur={handleBlur}
        />
        <span className="error">
          {errors.confirmPassword}
        </span>

        <h4>Interests</h4>

        <label>
          <input
            type="checkbox"
            value="Programming"
            onChange={handleChange}
          />
          Programming
        </label>

        <label>
          <input
            type="checkbox"
            value="Design"
            onChange={handleChange}
          />
          Design
        </label>

        <label>
          <input
            type="checkbox"
            value="Data Science"
            onChange={handleChange}
          />
          Data Science
        </label>

        <label>
          <input
            type="checkbox"
            value="Networking"
            onChange={handleChange}
          />
          Networking
        </label>

        <label>
          <input
            type="checkbox"
            value="Cybersecurity"
            onChange={handleChange}
          />
          Cybersecurity
        </label>

        <span className="error">
          {errors.interests}
        </span>

        <textarea
          name="bio"
          rows="5"
          placeholder="Short Bio"
          value={formData.bio}
          onChange={handleChange}
          onBlur={handleBlur}
        />

        <span className="error">
          {errors.bio}
        </span>

        <label className="terms-label">
          <input
            type="checkbox"
            name="terms"
            checked={formData.terms}
            onChange={handleChange}
          />
          I accept the Terms and Conditions
        </label>

        <span className="error">
          {errors.terms}
        </span>

        <button type="submit">
          Register
        </button>

      </form>

      <ProfilePreview formData={formData} />

    </div>
  );
}

export default SignUpForm;
``