import React, {createContext, useState, useEffect, useContext } from 'react';
import { authenticate } from "../services/auth";


const UserContext = createContext(null);
export const useUser = () => useContext(UserContext)

const UserProvider = ({children}) => {
  const[user, setUser ] = useState(null)
  const [loaded, setLoaded] = useState(false);
  const [authenticated, setAuthenticated] = useState(false);



  useEffect(() => {
    (async() => {
      const user = await authenticate();
      if (!user.errors) {
        setAuthenticated(true);
      }
      setUser(user)
      setLoaded(true);
    })();
  }, []);

  if (!loaded) {
    return null;
  }
  return(
  <UserContext.Provider value={{user, setUser, authenticated, setAuthenticated}}>
    {children}
    </UserContext.Provider>
    )
}
export default UserProvider
