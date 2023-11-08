import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Layout from './Layout';
import HomePage from './HomePage';
import UserProfile from './UserProfile';
import LoginForm from './LoginForm';
import SignUpForm from './SignUpForm';
import MatchPage from './MatchPage';
import UserDetailPage from './UserDetailPage';
import MatchesPage from './MatchesPage';
import { AuthProvider } from './AuthContext';
import '../index.css'

const App = () => {
    return (
    <AuthProvider>
        <div className ="app-background">
        <Router>
            <div className = "app-container">
            <Layout>
                <Switch>
                    <Route exact path="/" component={HomePage} />
                    <Route path="/profile" component={UserProfile} />
                    <Route path="/login" component={LoginForm} />
                    <Route path="/signup" component={SignUpForm} />
                    <Route path="/matches" component={MatchPage} />
                    <Route path="/users/:userId" component={UserDetailPage} />
                    <Route path="/my-matches" render={() => <MatchesPage userId={localStorage.getItem('userId')} />} />
                </Switch>
            </Layout>
            </div>
        </Router>
        </div>
    </AuthProvider>
    );
};

export default App;
