// App.js
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Layout from './Layout';
import HomePage from './HomePage';
import UserProfile from './UserProfile';
import LoginForm from './LoginForm';
import SignUpForm from './SignUpForm';
import MatchPage from './MatchPage';
import '../index.css'

const App = () => {
    return (
        <Router>
            <div className = "app-container">
            <Layout>
                <Switch>
                    <Route exact path="/" component={HomePage} />
                    <Route path="/profile" component={UserProfile} />
                    <Route path="/login" component={LoginForm} />
                    <Route path="/signup" component={SignUpForm} />
                    <Route path="/matches" component={MatchPage} />
                </Switch>
            </Layout>
            </div>
        </Router>
    );
};

export default App;


