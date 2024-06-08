const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;


export async function load({ fetch, url, params }) {
    let get_procedure_url = `${BACKEND_URL}${url.pathname.slice(1)}/`;
    let get_procedure_results_url = `${BACKEND_URL}${url.pathname.slice(1)}/results/`;

    let procedure = await getProcedure(fetch, get_procedure_url);
    let procedureResults = await getProcedureResults(fetch, get_procedure_results_url);

    return {
        slug: params.slug,
        procedure: procedure,
        procedureResults: procedureResults,
    }
}


async function getProcedure(fetch, url) {
    try {
        const response = await fetch(url, {
            method: 'GET',
            credentials: 'include'
        });
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return await response.json();
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
        return null;
    }
}

async function getProcedureResults(fetch, url) {
    try {
        const response = await fetch(url, {
            method: 'GET',
            credentials: 'include'
        });
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return await response.json();
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
    }
}