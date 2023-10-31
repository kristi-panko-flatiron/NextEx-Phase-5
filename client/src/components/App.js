import React from "react";
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import HomePage from '../components/HomePage';
import MatchPage from '../components/MatchPage';


function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route exact path="/" component={HomePage} />
          <Route exact path="/matches" component={MatchPage} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;

