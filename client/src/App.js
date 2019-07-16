import React from 'react';
import logo from './MyChaoticHeart.jpg';
import './App.css';
import getExperiments from "./ExperimentsService";

class App extends React.Component {

     componentDidMount() {
        this.setState({experiments: []}, async () => {
            const currentExperiments = await getExperiments();
            this.setState({experiments: currentExperiments});
        });
    }

    render() {
        const experiments = this.state ? this.state.experiments : {};
        const active = experiments.active || {};
        return (
            <div className="App">
                <header className="App-header">
                    <img src={logo} className="App-logo" alt="logo"/>


                </header>
                <div>
                    Active:
                    {Object.keys(active).map(key => (<li>key</li>))}
                </div>

            </div>

        );
    }
}

export default App;
