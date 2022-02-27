import login from './login';
import Navbar from './navbar';
import signup from './signup';
import './App.css';
import { BrowserRouter as Router, Switch, Route} from "react-router-dom";
import home from './home';
import calendar from './calendar';
import appointment from './appointment';
import Assignments from './assignments';
import announcements from './annoucements';
import classes from './classes';
function App() {
  return (
    <div className="App">
      <Router>
      <Switch>
        <Route path="/login" exact component={login} />
        <Route path="/home" exact component={home} />
        <Route path="/signup" exact component={signup} />
        <Route path="/calendar" exact component={calendar} />
        <Route path="/appointment" exact component={appointment} />
        <Route path="/assignments" exact component={Assignments} />
        <Route path="/announcements" exact component={announcements} />
        <Route path="/classes" exact component={classes} />
     <Navbar/>
     </Switch>
     </Router>
    </div>
  );
}
export default App;
