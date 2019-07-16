import axios from "axios";

async function getCurrentExperiments() {
    const response = await axios.get('/api/experiments/status')

    return response.data;
}

export async function getExperiments() {
    const response = await axios.get('/api/experiments')

    return response.data.experiments;
}

export  function runExperiment(name) {
    axios.get(`/api/experiments/${name}/run`);
}


export default getCurrentExperiments;
