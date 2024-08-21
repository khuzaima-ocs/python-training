import React, { useState, useEffect } from "react";
import "./Home.css";
import { MdAdd } from "react-icons/md";
import axios from "axios";
import ReactPaginate from "react-paginate";

const Home = ({ setScreen }) => {
  const [searchText, setSearchText] = useState("");
  const [users, setUsers] = useState([]);
  const [isFetching, setIsFetching] = useState(false);
  const [page, setPage] = useState(0);
  const [totalPages, setTotalPages] = useState(1);
  const [totalItems, setTotalItems] = useState(4);

  useEffect(() => {
    fetchUsers();
  }, [page]);

  const fetchUsers = () => {
    if (isFetching) return;
    setIsFetching(true);
    try {
      axios
        .get(
          `http://127.0.0.1:8000/users?search_query=${searchText}&size=${totalItems}&page=${page + 1}`
        )
        .then((res) => {
          console.log(res);
          setUsers(res.data.items);
          setTotalPages(res.data.pages);
          setPage(res.data.page - 1); 
          setIsFetching(false);
        });
    } catch (e) {
      setIsFetching(false);
      console.log(e);
    }
  };

  const updateData = (e) => {
    e.preventDefault();
    if(page == 0) {
      fetchUsers()
    }
    setPage(0);
  };

  const handlePageClick = (event) => {
    setPage(event.selected);
  };

  return (
    <>
      <button onClick={() => setScreen("signup")} className="floating-button">
        <MdAdd className="add-icon" />
      </button>
      <div className="home-screen-container">
        <form onSubmit={updateData} className="search-container">
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
          <>
            <div className="cards-container">
              {users.map((user) => (
                <div key={user.email} className="form-container card">
                  <img
                    className="card-image"
                    src={`http://127.0.0.1:8000/image/${user.display_pic}`}
                    alt={user.username}
                  />
                  <p className="card-user-name">
                    {user.first_name + " " + user.last_name}
                  </p>
                  <div className="line"></div>
                  <p className="card-user-username">{user.username}</p>
                </div>
              ))}
            </div>
            <ReactPaginate
              breakLabel="..."
              nextLabel=">"
              onPageChange={handlePageClick}
              pageRangeDisplayed={5}
              pageCount={totalPages}
              previousLabel="<"
              renderOnZeroPageCount={null}
              forcePage={page}
            />
          </>
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