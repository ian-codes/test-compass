const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;

export async function load({ fetch, url, params }) {
    let get_test_url = `${BACKEND_URL}${url.pathname.slice(1)}/`;
    let get_test_results_url = `${BACKEND_URL}${url.pathname.slice(1)}/results/`;

    let test = await getTest(fetch, get_test_url);
    let testResults = await getTestResults(fetch, get_test_results_url);

    return {
        slug: params.slug,
        test: test,
        testResults: testResults,
    }
}

async function getTest(fetch, url) {
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

async function getTestResults(fetch, url) {
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