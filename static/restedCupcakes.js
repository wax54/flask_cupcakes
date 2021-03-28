const BASE_URL = '/api/cupcakes'

async function getAllCakes() {
    const res = await axios.get(BASE_URL);
    cupcakes = res.data.cupcakes;
    return cupcakes;
}

async function getCakesByFlavor(term) {
    const res = await axios.get(BASE_URL + '?term=' + term);
    cupcakes = res.data.cupcakes;
    return cupcakes;
}


async function getCake(cake_id) {
    const res = await axios.get(`${BASE_URL}/${cake_id}`);
    cupcake = res.data.cupcake;
    return cupcake;
}

async function createCake(cake) {
    try {
        const res = await axios.post(BASE_URL, cake);
        cupcake = res.data.cupcake;
        return cupcake;
    }
    catch {
        return false;
    }
}


