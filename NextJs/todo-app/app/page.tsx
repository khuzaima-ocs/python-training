"use client"

import { useState } from "react";
import { Todo, TodoStatus } from "@/types";
import { capitalizeFirstLetter } from "@/utils";

const todos: Todo[] = [
  {
    id: 1,
    title: "Go to GYM",
    description: "At 11pm, I have to go to gym.",
    status: "pending",
  },
  {
    id: 2,
    title: "Have dinner",
    description: "At 12pm, I should have dinner.",
    status: "in-progress",
  },
  {
    id: 3,
    title: "Have dinner",
    description: "At 12pm, I should have dinner.",
    status: "completed",
  },
  {
    id: 4,
    title: "Have dinner",
    description: "At 12pm, I should have dinner.",
    status: "removed",
  },
];

const get_todo_bg = (status: TodoStatus): String => {
  let style = "";
  if (status === "pending") {
    style = "bg-yellow-800 hover:bg-yellow-700";
  } else if (status === "completed") {
    style = "bg-green-800 hover:bg-green-700";
  } else if (status === "in-progress") {
    style = "bg-blue-800 hover:bg-blue-700";
  } else if (status === "removed") {
    style = "bg-red-800 hover:bg-red-700";
  }

  return style;
};

const Home = () => {
  const [newTodo, setNewTodo] = useState({
    title: "",
    description: "",
    status: "pending" as TodoStatus,
  });

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>
  ) => {
    const { name, value } = e.target;
    setNewTodo({
      ...newTodo,
      [name]: value,
    });
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    todos.push({ ...newTodo, id: todos.length + 1 });
    setNewTodo({
      title: "",
      description: "",
      status: "pending",
    });
  };

  return (
    <div className="flex justify-center items-center w-full min-h-screen">
      <div className="flex justify-center items-center w-4/5 gap-5">
        <div className="flex flex-1 flex-col gap-2 p-4 bg-gray-900 rounded-xl text-sm">
          <div className="flex justify-between w-full bg-gray-800 px-5 py-3 rounded-t-lg hover: cursor-pointer">
            <p>Title</p>
            <p>Description</p>
            <p>Status</p>
          </div>
          {todos.map((todo, index) => {
            return (
              <div
              key={index}
                className={` ${get_todo_bg(todo.status)} ${
                  index === todos.length - 1 ? "rounded-b-lg" : ""
                }  flex justify-between w-full px-5 py-3 hover: cursor-pointer`}
              >
                <p>{todo.title}</p>
                <p>{todo.description}</p>
                <p>{capitalizeFirstLetter(todo.status)}</p>
              </div>
            );
          })}
        </div>
        <div className="flex flex-1 flex-col gap-5 p-4 bg-gray-900 rounded-xl text-sm">
          <h2 className="text-lg text-center">Add Todo</h2>
          <form onSubmit={handleSubmit} className="flex flex-col gap-2">
            <input
              type="text"
              name="title"
              value={newTodo.title}
              onChange={handleChange}
              placeholder="Title"
              className="p-3 rounded bg-gray-800 text-white"
              required
            />
            <input
              type="text"
              name="description"
              value={newTodo.description}
              onChange={handleChange}
              placeholder="Description"
              className="p-3 rounded bg-gray-800 text-white"
              required
            />
            <select
              name="status"
              value={newTodo.status}
              onChange={handleChange}
              className="p-3 rounded bg-gray-800 text-white"
              required
            >
              <option value="pending">Pending</option>
              <option value="in-progress">In Progress</option>
              <option value="completed">Completed</option>
              <option value="removed">Removed</option>
            </select>
            <button
              type="submit"
              className="p-3 rounded bg-green-800 text-white hover:bg-green-700"
            >
              Add Todo
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default Home;
