const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;

export async function load({ fetch, params }) {
    let get_uats_url = `${BACKEND_URL}projects/${params.slug}/tests/`;
    let uats = await getUats(fetch, get_uats_url);

    return { 
        slug: params.slug,
        uats: uats
    }
}

async function getUats(fetch, url) {
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