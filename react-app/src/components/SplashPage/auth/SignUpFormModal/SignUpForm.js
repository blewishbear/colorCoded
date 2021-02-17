import React, { useState } from "react";
import { Redirect } from 'react-router-dom';
import { signUp } from '../../../../services/auth';
import { useUser } from '../../../../context/UserContext'
import "./SignUpForm.css";


const SignUpForm = ({authenticated, setAuthenticated, onClose}) => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [repeatPassword, setRepeatPassword] = useState("");
  const { user, setUser } = useUser()

  const onSignUp = async (e) => {
    e.preventDefault();
    if (password === repeatPassword) {
      const userResponse = await signUp(username, email, password);
      if (!userResponse.errors) {
        setAuthenticated(true);
        setUser(user)
      }
    }
  };

  const updateUsername = (e) => {
    setUsername(e.target.value);
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const updateRepeatPassword = (e) => {
    setRepeatPassword(e.target.value);
  };

  if (authenticated) {
    return <Redirect to="/" />;
  }

  return (
    <form className="modal-content" onSubmit={onSignUp}>
      <div className="signup-form__top">

        <input placeholder="User Name"
          type="text"
          name="username"
          onChange={updateUsername}
          value={username}
        ></input>
      </div>
      <div>

        <input placeholder="Email"
          type="text"
          name="email"
          onChange={updateEmail}
          value={email}
        ></input>
      </div>
      <div>

        <input placeholder="Password"
          type="password"
          name="password"
          onChange={updatePassword}
          value={password}
        ></input>
      </div>
      <div>

        <input placeholder="Repeat Password"
          type="password"
          name="repeat_password"
          onChange={updateRepeatPassword}
          value={repeatPassword}
          required={true}
        ></input>
      </div>
      <div className='signup-btn'>
        <button type="submit"onClick={onClose}>Sign Up</button>
      </div>
    </form>
  );
};

export default SignUpForm;
