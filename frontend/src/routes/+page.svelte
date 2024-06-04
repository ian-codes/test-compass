<section>
    <h2>Organization</h2>
    <InviteComponent /> <!-- only show if user is manager -->
</section>

<section>
    <h2>Members • {members.length}</h2>

    <div class="overflow-scroll px-2 py-10">
        <ol class="flex flex-row gap-2 w-max">
            {#each members as member}
                <MemberCard member={member} />
            {/each}
        </ol>
    </div>
</section>


{#if projects}
    <section class="flex flex-col gap-5">
        <div class="flex flex-row gap-5 justify-start items-center">
            <h2 class="m-0">Projects • {projects.length}</h2>

            <button on:click={() => goto("/projects/new")}
                class="btn !m-0 !w-max inline-block">
                New Project
            </button>
        </div>

        <ol class="flex flex-wrap items-center justify-center gap-4">
            {#each projects as project}
                <ProjectCard project={project} />
            {/each}
        </ol>
    </section>
{/if}



<script>
    import InviteComponent from "$lib/organization/InviteComponent.svelte";
    import { members } from "$models/members.js";
    import ProjectCard from "$lib/projects/ProjectCard.svelte";
    import MemberCard from "$lib/organization/MemberCard.svelte";
    import { onMount } from "svelte";
    import { goto } from "$app/navigation.js";

    const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;
    const GET_PROJECTS_URL = `${BACKEND_URL}organizations/projects/`;

    let projects = [];

    onMount(async () => {
        projects = await getProjects();
        console.log("projcets:", projects)
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