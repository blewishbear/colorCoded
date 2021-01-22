import React from "react";
import { logout } from "../../../services/auth";
import {useUser} from "../../../context/UserContext"

const LogoutButton = ({setAuthenticated}) => {
  const {setUser} = useUser()
  const onLogout = async (e) => {
    await logout();
    setAuthenticated(false);
    setUser(false)
  };

  return <button onClick={onLogout} className="usermenu__option">Logout</button>;
};

export default LogoutButton;
