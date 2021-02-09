import React, { useState, useEffect } from "react";
import { useRecoilState } from "recoil";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import { cartState, productsState, ideaState } from "./Atoms"
import NavBar from "./components/SplashPage/Navbar/index.js";
// import HomePage from "./components/SplashPage/HomePage";
// import ProtectedRoute from "./components/SplashPage/auth/ProtectedRoute";

// import { authenticate } from "./services/auth";
import ProductListing from "./components/Products/ProductListing.js";
// import UsersList from "./components/UsersList.js";
import IdeasFeed from "./components/Ideas/IdeasFeed.js";
import { useUser } from "./context/UserContext.js";
import CreateIdeaForm from "./components/Ideas/CreateIdeaForm.js";
import CartView from "./components/Cart/CartView.js";


function App() {
  const [products, setProducts] = useRecoilState(productsState);
  const [cart, setCart] = useRecoilState(cartState);
  const [allIdeas, setIdeas] = useRecoilState(ideaState);

  const [cartCount, setCartCount] = useState(() => {
    if (!localStorage.getItem("cart")) {
      return 0;
    }
    const quantities = Object.values(JSON.parse(localStorage.getItem("cart")));
    return quantities.reduce((a, b) => a + b, 0);
  });
console.log(cart)
  useEffect(() => {
  if (!cart.length) {
      let localCart = localStorage.getItem("cart")
      localCart = JSON.parse(localCart)
      if(localCart){
        setCart(localCart)
      }
    }
  }, []);

  useEffect(() => {
    (async () => {
      const res = await fetch("/api/t-shirts");
      const parsedProducts = await res.json();
      setProducts(parsedProducts);
    })();
  }, []);

  useEffect(() => {
    (async () => {
      const res = await fetch("/api/ideas");
      const parsedIdeas = await res.json();
      setIdeas(parsedIdeas);

      console.log(parsedIdeas);
    })();
  }, []);


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
        <Route path="/" exact={true}>
          <ProductListing setCartCount={setCartCount} />

          {/* <HomePage></HomePage> */}
        </Route>
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
        <Route path="/cart">
          <CartView />
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
