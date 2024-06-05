const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;


export async function load({ fetch, params }) {
    let get_project_url = `${BACKEND_URL}organizations/projects/${params.slug}/`;
    let get_test_procedures_url = `${BACKEND_URL}organizations/projects/${params.slug}/testprocedures/`;
    let get_uats_url = `${BACKEND_URL}organizations/projects/${params.slug}/tests/`;
 
    let project = await getProject(fetch, get_project_url);
    let procedures = await getTestProcedures(fetch, get_test_procedures_url);
    let uats = await getUats(fetch, get_uats_url);

    return { 
        slug: params.slug, 
        project: project, 
        procedures: procedures, 
        uats: uats 
    }
}


async function getProject(fetch, url) {
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


async function getTestProcedures(fetch, url) {
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