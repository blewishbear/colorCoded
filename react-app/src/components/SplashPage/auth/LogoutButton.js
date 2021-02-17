import React, { useEffect  } from "react";
import { useHistory } from "react-router-dom";
import { logout } from "../../../services/auth";
import {useUser} from "../../../context/UserContext"

const LogoutButton = ({setAuthenticated}) => {
  const {setUser} = useUser()
  const history = useHistory()
  const { user } = useUser()
  const onLogout = async (e) => {
    await logout();
    setAuthenticated(false);
    setUser(false)
    history.push("/t-shirts")

  };


  return <button onClick={onLogout} className="usermenu__option">Logout</button>;
};

export default LogoutButton;
