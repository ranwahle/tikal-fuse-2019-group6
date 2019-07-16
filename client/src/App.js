import React from 'react';
import logo from './MyChaoticHeart.jpg';
import './App.css';
import getExperiments from "./ExperimentsService";

class App extends React.Component {

     componentDidMount() {
        this.setState({experiments: []}, async () => {
            const currentExperiments = await getExperiments();
            console.log('curent exp', currentExperiments);
            this.setState({experiments: currentExperiments});
        });
    }

    render() {
        const experiments = this.state ? this.state.experiments : {};
        const active = experiments.active || {};
        console.log('active', active);
        return (
            <div className="App">
                <header className="App-header">
                    <img src={logo} className="App-logo" alt="logo"/>


                </header>
                <div>
                    <h2>  Active: </h2>
                    {Object.keys(active).map(key => (<li key={key}>{key}</li>))}
                </div>

            </div>

        );
    }
}

export default App;
