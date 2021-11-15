import React from "react";
import {
    BrowserRouter as Router,
    Switch,
    Route
} from "react-router-dom";
import Landing from './Components/LandingPage/Landing'
import Search from './Components/SearchPage/Search'

function App() {
    return (
        <Router>
            <Switch>
                <Route exact path="/" component={Landing} />
                <Route path="/results" component={Search} />
               
            </Switch>
        </Router>
    );
}
export default App;