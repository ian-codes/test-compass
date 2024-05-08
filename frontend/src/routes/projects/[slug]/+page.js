import { projects } from "$models/projects.js";
import { goto } from "$app/navigation";

export function load({ params }) {
    return projects.find(project => project.id === params.slug ?? goto("/"));
}