import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import UserProvider from './context/UserContext';
import { RecoilRoot} from "recoil";


ReactDOM.render(
  // <React.StrictMode>
    <RecoilRoot>
    <UserProvider>
    <App />
    </UserProvider>
    </RecoilRoot>
  //  </React.StrictMode>,
  ,document.getElementById('root')
);
