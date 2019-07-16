import React from 'react';
import logo from './MyChaoticHeart.jpg';
import './App.css';
import getCurrentExperiments, {getExperiments, runExperiment} from "./ExperimentsService";

class App extends React.Component {

     componentDidMount() {
        this.setState({currentExperiments: []}, async () => {
            const currentExperiments = await getCurrentExperiments();
            console.log('curent exp', currentExperiments);
            this.setState({currentExperiments: currentExperiments}
            ,async () => {
                const experiments = await getExperiments();
                this.setState({experiments: experiments})
                }) ;
        });
    }

    runExperiment = (event) => {
         const {value} = event.currentTarget;
         runExperiment(value);
    }

    render() {
        const currentExperiments = this.state ? this.state.currentExperiments : {};
        const experiments = this.state && this.state.experiments ? this.state.experiments : [];
        const active = currentExperiments.active || {};
        console.log('active', active);
        return (
            <div className="App">
                <select onChange={this.runExperiment}>
                    {experiments.map(experiment =>
                        (<option key={experiment.name} value={experiment.name}>{experiment.description}
                        </option>))
                    }
                </select>
                <header className="App-header">
                    <img src={logo} className="App-logo" alt="logo"/>


                </header>
                <div>
                    <h2>  Active: </h2>
                    {Object.keys(active).map(key => {
                        const activeExperiments = active[key] || [];

                        return (<li key={key}>{key}
                            {
                                activeExperiments.map(exp => {
                                    return  (<span>Time: {new Date(exp.time_start)}</span>)
                                })
                            }
                        </li>)
                    })}
                </div>

            </div>

        );
    }
}

export default App;
