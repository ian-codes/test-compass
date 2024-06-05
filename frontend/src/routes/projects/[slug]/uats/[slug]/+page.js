const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;
const GET_PROJECTS_URL = `${BACKEND_URL}organizations/projects/`;

export async function load({ params }) {
    return await getProject(params.slug);
}

async function getProject(projectId) {
    const url = `${GET_PROJECTS_URL}${projectId}`;
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