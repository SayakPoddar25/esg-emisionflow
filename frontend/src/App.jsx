import { Routes, Route } from "react-router-dom";

import Login from "./pages/login/Login";
import Dashboard from "./pages/dashboard/Dashboard";
import Upload from "./pages/upload/Upload";
import Review from "./pages/review/Review";

import "./App.css";

function App() {
  return (
    <Routes>
      <Route
        path="/"
        element={<Login />}
      />

      <Route
        path="/dashboard"
        element={<Dashboard />}
      />

      <Route
        path="/upload"
        element={<Upload />}
      />

      <Route
        path="/review"
        element={<Review />}
      />
    </Routes>
  );
}

export default App;