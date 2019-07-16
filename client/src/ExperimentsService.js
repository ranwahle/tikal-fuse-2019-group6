import axios from "axios";

function getExperiments() {
    return axios.get('/api/experiments/status')
}

export default getExperiments;
