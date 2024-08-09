import React, { useState, useEffect } from "react";
import "./Home.css";
import { MdAdd } from "react-icons/md";
import axios from "axios";

const Home = ({setScreen}) => {
  const [searchText, setSearchText] = useState("");
  const [users, setUsers] = useState([]);
  const [isFetching, setIsFetching] = useState(false);

  useEffect(() => {
    fetchUsers();
  }, []);

  const fetchUsers = (e) => {
    if(e) e.preventDefault();
    if (isFetching) return;
    setIsFetching(true);
    try {
      axios
        .get("http://127.0.0.1:8000/users?search_query=" + searchText)
        .then((res) => {
          setUsers(res.data);
          console.log(res.data);
          setIsFetching(false);
        });
    } catch (e) {
      setIsFetching(false);
      console.log(e);
    }
  };

  return (
    <>
    <button onClick={() => setScreen("signup")} className="floating-button">
      <MdAdd className="add-icon" />
    </button>
    <div className="home-screen-container">
      <form onSubmit={fetchUsers} className="search-container">
        <input
          className="form-input-field search-field"
          value={searchText}
          onChange={(e) => setSearchText(e.target.value)}
          placeholder="Search username or email"
        />

        <button type="submit" className="search-button">
          Search
        </button>
      </form>
      {users.length > 0 ? (
        <div className="cards-container">
          {users.map((user) => {
            return (
              <div key={user.email} className="form-container card">
                <img
                  className="card-image"
                  src={`http://127.0.0.1:8000/image/${user.display_pic}`}
                />

                <p className="card-user-name">
                  {user.first_name + " " + user.last_name}
                </p>
                <div className="line"></div>
                <p className="card-user-username">{user.username}</p>
              </div>
            );
          })}
        </div>
      ) : (
        <div className="no-user-to-show">
          <p>No users to show</p>
        </div>
      )}
    </div>
    </>
  );
};

export default Home;
