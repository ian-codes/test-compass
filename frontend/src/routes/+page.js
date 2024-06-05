const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;
const GET_PROJECTS_URL = `${BACKEND_URL}organizations/projects/`;

export async function load({ fetch }) {
    let projects = await getProjects(fetch);
    return { projects }
}

async function getProjects(fetch) {
    try {
        const response = await fetch(GET_PROJECTS_URL, {
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