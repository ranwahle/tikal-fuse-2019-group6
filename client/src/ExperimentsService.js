import axios from "axios";

async function getExperiments() {
    const response = await axios.get('/api/experiments/status')

    return response.data;
}

export default getExperiments;
