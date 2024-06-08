const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;
const GET_PROJECTS_URL = `${BACKEND_URL}projects/`;
const GET_USER_URL = `${BACKEND_URL}user/`;
const GET_ORG_URL = `${BACKEND_URL}org/`;


export async function load({ fetch }) {
    let user = await getUser(fetch);
    let organization = await getOrganization(fetch);
    let projects = await getProjects(fetch);
    return { 
        organization: organization,
        user: user, 
        projects: projects 
    }
}

async function getUser(fetch) {
    try {
        const response = await fetch(GET_USER_URL, {
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

async function getOrganization(fetch) {
    try {
        const response = await fetch(GET_ORG_URL, {
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