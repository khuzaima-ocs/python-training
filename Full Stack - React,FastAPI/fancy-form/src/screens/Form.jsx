import toast, { Toaster } from "react-hot-toast";
import React, { useState, useRef } from "react";
import { IoPerson } from "react-icons/io5";
import { TbArrowBackUp } from "react-icons/tb";
import axios from "axios";
import "./Form.css";

const notify = (message, state) => {
  if (state == "success") {
    toast.success(message, {
      icon: "✅",
    });
  } else if (state == "error") {
    toast.error(message, {
      icon: "❌",
    });
  }
};

const Form = ({ setScreen }) => {
  const fileInputRef = useRef(null);
  const [user, setUser] = useState({
    firstName: "",
    lastName: "",
    email: "",
    username: "",
    password: "",
    confirmPassword: "",
  });
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [file, setFile] = useState(null);
  const [imagePreview, setImagePreview] = useState(null);

  const changeFormValue = (name, value) => {
    setUser((prevUser) => ({ ...prevUser, [name]: value }));
  };

  const handleChange = (e) => {
    changeFormValue(e.target.name, e.target.value);
  };

  const handleClick = () => {
    fileInputRef.current.click();
  };

  const handleFileChange = (event) => {
    const image = event.target.files[0];
    if (image) {
      setFile(image);
      const imageUrl = URL.createObjectURL(image);
      setImagePreview(imageUrl);
    }
  };

  const submit = (e) => {
    e.preventDefault();
    if (isSubmitting) return;
    if (!file) {
      notify("Please select an iamge", "error");
      setIsSubmitting(false);
      return;
    }
    setIsSubmitting(true);

    if (user.password !== user.confirmPassword) {
      notify("Passwords must match", "error");
      setIsSubmitting(false);
      return;
    }

    try {
      const reqBody = new FormData();
      for (const key in user) {
        reqBody.append(key, user[key]);
      }
      if (file) {
        reqBody.append("file", file);
      }

      axios
        .post("http://127.0.0.1:8000/signup", reqBody, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then((res) => {
          notify(res.data, "success");
          console.log(res);
        });

      setUser({
        firstName: "",
        lastName: "",
        email: "",
        username: "",
        password: "",
        confirmPassword: "",
      });

      setFile(null);
      setImagePreview(null);
      if (fileInputRef.current) {
        fileInputRef.current.value = "";
      }

      setIsSubmitting(false);
    } catch (e) {
      console.log(e);
      notify("Something went wrong", "error");
      setIsSubmitting(false);
    }
  };

  return (
    <>
      <button onClick={() => setScreen("users")} className="floating-button">
        <TbArrowBackUp className="add-icon" />
      </button>
      <div className="topmost-container">
        <Toaster />
        <form onSubmit={submit} className="form-container">
          <div onClick={handleClick} style={{ cursor: "pointer" }}>
            {file ? (
              <img
                src={imagePreview}
                alt=""
                style={{
                  width: "100px",
                  height: "100px",
                  objectFit: "cover",
                  borderRadius: "25%",
                }}
              />
            ) : (
              <IoPerson className="avatar" />
            )}

            <input
              type="file"
              ref={fileInputRef}
              onChange={handleFileChange}
              style={{ display: "none" }}
            />
          </div>

          <input
            className="form-input-field"
            name="firstName"
            value={user.firstName}
            onChange={handleChange}
            placeholder="First Name"
            required
          />

          <input
            className="form-input-field"
            name="lastName"
            value={user.lastName}
            onChange={handleChange}
            placeholder="Last Name"
            required
          />

          <input
            className="form-input-field"
            name="email"
            type="email"
            value={user.email}
            onChange={handleChange}
            placeholder="Email"
            required
          />
          <input
            className="form-input-field"
            name="username"
            value={user.username}
            onChange={handleChange}
            placeholder="Username"
            required
          />
          <input
            className="form-input-field"
            name="password"
            type="password"
            value={user.password}
            onChange={handleChange}
            placeholder="Password"
            minLength={6}
            required
          />
          <input
            className="form-input-field"
            name="confirmPassword"
            type="password"
            value={user.confirmPassword}
            onChange={handleChange}
            placeholder="Re-enter password"
            required
          />

          <button type="submit" className="signup-button">
            SIGN UP
          </button>
        </form>
      </div>
    </>
  );
};

export default Form;
