import { useState } from "react";
import Form from "./screens/Form";
import Home from "./screens/Home";

function App() {
  const [screen, setScreen] = useState("signup");
  return <div>{screen == "signup" ? <Form setScreen={setScreen} /> : <Home setScreen={setScreen} />}</div>;
}

export default App;
