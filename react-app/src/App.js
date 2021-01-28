import React, { useState } from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";

import NavBar from "./components/SplashPage/Navbar/index.js";
// import HomePage from "./components/SplashPage/HomePage";
// import ProtectedRoute from "./components/SplashPage/auth/ProtectedRoute";

// import { authenticate } from "./services/auth";
import ProductListing from "./components/Products/ProductListing.js";
// import UsersList from "./components/UsersList.js";
import IdeasFeed from "./components/Ideas/IdeasFeed.js";
import { useUser } from "./context/UserContext.js";
import CreateIdeaForm from "./components/Ideas/CreateIdeaForm.js";

function App() {
  const [cartCount, setCartCount] = useState(() => {
    if (!localStorage.getItem("cart")) {
      return 0;
    }
    const quantities = Object.values(JSON.parse(localStorage.getItem("cart")));
    return quantities.reduce((a, b) => a + b, 0);
  });
  // const [authenticated, setAuthenticated] = useState(false);
  // const [loaded, setLoaded] = useState(false);

  // useEffect(() => {
  //   (async() => {
  //     const user = await authenticate();
  //     if (!user.errors) {
  //       setAuthenticated(true);
  //     }
  //     setLoaded(true);
  //   })();
  // }, []);

  // if (!loaded) {
  //   return null;
  // }
  const { authenticated, setAuthenticated } = useUser();

  return (
    <BrowserRouter>
      <NavBar
        authenticated={authenticated}
        setAuthenticated={setAuthenticated}
        cartCount={cartCount}
      />
      <Switch>
        {/* <Route path="/" exact={true}>
          <HomePage></HomePage>
        </Route> */}
        {/* <ProductListing /> */}

        <Route path="/t-shirts">
          <ProductListing setCartCount={setCartCount} />
        </Route>
        <Route path="/ideas">
          <IdeasFeed />
        </Route>
        <Route path="/ideas/create">
          <CreateIdeaForm />
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
