import React, { useState, useEffect } from "react";
import { useRecoilState } from "recoil";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import NavBar from "./components/SplashPage/Navbar/index.js";
import ProductListing from "./components/Products/ProductListing.js";
import IdeasFeed from "./components/Ideas/IdeasFeed.js";
import { useUser } from "./context/UserContext.js";
import { cartState, productsState, ideaState, dapState } from "./Atoms"
import CreateIdeaForm from "./components/Ideas/CreateIdeaForm.js";
import CartView from "./components/Cart/CartView.js";
import HomePage from "./components/SplashPage/SplashPageModal/HomePage";


function App() {
  const [products, setProducts] = useRecoilState(productsState);
  const [cart, setCart] = useRecoilState(cartState);
  const [allIdeas, setIdeas] = useRecoilState(ideaState);
  const [daps, setDaps] = useRecoilState(dapState);
  const [loaded, setLoaded] = useState(false);

  const { user } = useUser()
  useEffect(() => {
    console.log(user)
  }, [user])

  const [cartCount, setCartCount] = useState(() => {
    if (!localStorage.getItem("cart")) {
      return 0;
    }
    const quantities = Object.values(JSON.parse(localStorage.getItem("cart")));
    return quantities.reduce((a, b) => a + b, 0);
  });

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


    })();
  }, []);

  useEffect(() => {
    (async () => {
      const res = await fetch(`/api/daps`);
      const parsedDaps = await res.json();
      await setDaps(parsedDaps);
      return setLoaded(true)


    })();
  }, []);



  const { authenticated, setAuthenticated } = useUser();

  return loaded && (
    <BrowserRouter>
      <NavBar
        authenticated={authenticated}
        setAuthenticated={setAuthenticated}
        cartCount={cartCount}
      />
      <Switch>
        <Route path="/" exact={true}>

          <HomePage />
        </Route>

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

export default App;
