import "./App.css";
import Home from "./Component/Home";
import { BrowserRouter, Switch, Route } from "react-router-dom";
import Login from "./Component/Login";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Switch>
          <Route path="/login" exact>
            <Login />
          </Route>
          <Route path="/home" exact>
            <Home />
          </Route>
          <Route path="/cart" exact>
            {/* <Cart /> */}
          </Route>
        </Switch>
      </BrowserRouter>
    </div>
  );
}

export default App;