import React, { useState, useEffect } from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";

import NavBar from "./components/SplashPage/Navbar/index.js";
import HomePage from "./components/SplashPage/HomePage"
import ProtectedRoute from "./components/SplashPage/auth/ProtectedRoute";

import { authenticate } from "./services/auth";
import ProductListing from "./components/Products/ProductListing.js";

function App() {
  const [authenticated, setAuthenticated] = useState(false);
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    (async() => {
      const user = await authenticate();
      if (!user.errors) {
        setAuthenticated(true);
      }
      setLoaded(true);
    })();
  }, []);

  if (!loaded) {
    return null;
  }
  return (
    <BrowserRouter>
      <NavBar authenticated={authenticated} setAuthenticated={setAuthenticated} />
      <Switch>
        <Route path="/" exact={true}>
          <HomePage></HomePage>
        </Route>
        {/* <ProtectedRoute exact={true} path="/listings/create" authenticated={authenticated}>
          <CreateHouseForm user={authenticated} />
        </ProtectedRoute> */}
        {/* <Route path='/listings/:id' exact={true}>
          <HouseProfilePage />
      </Route>*/}
        <Route path="/t-shirts/">
          <ProductListing />
        </Route>
      </Switch>
    </BrowserRouter>
  );
}


  // return (
  //   <BrowserRouter>
  //     <NavBar setAuthenticated={setAuthenticated} />
  //     <Route path="/login" exact={true}>
  //       <LoginForm
  //         authenticated={authenticated}
  //         setAuthenticated={setAuthenticated}
  //       />
  //     </Route>
  //     <Route path="/sign-up" exact={true}>
  //       <SignUpForm authenticated={authenticated} setAuthenticated={setAuthenticated} />
  //     </Route>
  //     <ProtectedRoute path="/users" exact={true} authenticated={authenticated}>
  //       <UsersList/>
  //     </ProtectedRoute>
  //     <ProtectedRoute path="/users/:userId" exact={true} authenticated={authenticated}>
  //       <User />
  //     </ProtectedRoute>
  //     <ProtectedRoute path="/" exact={true} authenticated={authenticated}>
  //       <h1>My Home Page</h1>
  //     </ProtectedRoute>
  //   </BrowserRouter>
  // );
// }

export default App;
