import "./Login.css";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { loginUser } from "../../api/authApi";

function Login() {
  const navigate = useNavigate();

  const [username, setUsername] =
    useState("");

  const [password, setPassword] =
    useState("");

    const handleLogin =
    async () => {
  
      if (
        username === "admin"
        &&
        password === "admin123"
      ) {
  
        navigate(
          "/dashboard"
        );
  
      } else {
  
        alert(
          "Login failed"
        );
      }
    };

  return (
    <div className="login-container">

      <div className="login-card">

        <h1>
          EmissionFlow
        </h1>

        <p>
          ESG Emission Prototype
        </p>

        <input
          type="text"
          placeholder="Username"
          onChange={(e) =>
            setUsername(
              e.target.value
            )
          }
        />

        <input
          type="password"
          placeholder="Password"
          onChange={(e) =>
            setPassword(
              e.target.value
            )
          }
        />

        <button
          onClick={
            handleLogin
          }
        >
          Login
        </button>

      </div>

    </div>
  );
}

export default Login;