<script>
    import ProjectCard from "$lib/projects/ProjectCard.svelte";
    import { onMount } from "svelte";
    import { goto } from "$app/navigation.js";

    const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;
    const GET_PROJECTS_URL = `${BACKEND_URL}projects/`;

    let projects;

    onMount(async () => {
        projects = await getProjects();
    });

    async function getProjects() {
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
</script>

<section class="flex min-h-lvh flex-col gap-5">
    {#if projects}
        <div class="flex flex-row items-center justify-between gap-4 mb-10">
            <h2 class="m-0">Projects • {projects.length}</h2>

            <button on:click={() => goto("/projects/new")}
                class="btn !m-0 !w-max inline-block">
                Add New
            </button>
        </div>

        <ol class="flex flex-wrap items-center justify-center gap-4">
            {#each projects as project}
                <ProjectCard project={project} />
            {/each}
        </ol>
    {:else}
        <p class="text-center">Loading projects...</p>
    {/if}
</section>