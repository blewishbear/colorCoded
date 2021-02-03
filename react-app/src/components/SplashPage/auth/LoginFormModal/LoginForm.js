import React, { useState } from "react";
import { login } from "../../../../services/auth";
import {useUser} from "../../../../context/UserContext"
import "./LoginForm.css"


const LoginForm = ({ onClose }) => {
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState("");
  const{ setUser, setAuthenticated } = useUser();
  const [password, setPassword] = useState("");

  const onLogin = async (e) => {
    e.preventDefault();
    const userResponse = await login(email, password);
    if (!userResponse.errors) {
      setAuthenticated(true);
      setUser(userResponse)
      onClose()
    } else {
      setErrors(userResponse.errors);
    }
  };
  const onLoginDemo = async (e) => {
    e.preventDefault();
    const userResponse = await login("demo@aa.io","password");
    if (!userResponse.errors) {
      setAuthenticated(true);
      setUser(userResponse)
      onClose()
    } else {
      setErrors(userResponse.errors);
    }
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };



  return (
    <form className="login-form" onSubmit={onLogin}>
      <div>
        {errors.map((error) => (
          <div>{error}</div>
        ))}
      </div>
      <div className="login__form-input">
        <div>
          <label htmlFor="email">Email</label>
          <input
            name="email"
            type="text"
            placeholder="Email"
            value={email}
            onChange={updateEmail}
          />
        </div>
        <div>
          <label htmlFor="password">Password</label>
          <input
            name="password"
            type="password"
            placeholder="Password"
            value={password}
            onChange={updatePassword}
          />
          <button type="submit">Login</button>
          <button onClick={onLoginDemo} type="submit">Demo User</button>
        </div>
      </div>
    </form>
  );
};


export default LoginForm;
