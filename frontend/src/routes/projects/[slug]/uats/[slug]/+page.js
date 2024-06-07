const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;
const GET_PROJECTS_URL = `${BACKEND_URL}organizations/projects/`;

export async function load({ params }) {
    return params;
}