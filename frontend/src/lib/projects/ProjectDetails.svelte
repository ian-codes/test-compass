<section class="flex flex-col gap-5">
    {#if project.name}
        <div class="flex flex-row justify-between">
            <a href="/#projects" 
                class="btn-secondary !outline-black !w-max">
                Back to Projects
            </a>

            <button on:click={handleDelete}
                class="btn-secondary !outline-red-500 !w-max">
                Delete this Project
            </button>
        </div>

        <h1>
            {project.name}
        </h1>

        <p>
            {project.description}
        </p>
    {:else}
        <p>Loading...</p>
    {/if}
</section>


<script>
    import { onMount } from "svelte";

    export let project;

    const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;
    let project_delete_url;

    onMount(() => {
        project_delete_url = `${BACKEND_URL}organizations/projects/${project.id}/delete/`;
    });

    let hasFailed = false;

    async function handleDelete() {
        try {
            const response = await fetch(project_delete_url, {
                method: 'DELETE',
                credentials: 'include'
            })
            if (response.ok) {
                hasFailed = false;
            } else {
                hasFailed = true;
            }
        }
        catch {
            hasFailed = true;
        }
    }
</script>
