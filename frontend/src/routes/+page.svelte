{#if isLoading}
    <h1 class="text-2xl">Loading...</h1>
{:else}
    <div class="flex flex-col justify-start items-center 
        gap-4 w-full m-auto mt-0"
        class:visible={!isLoading}>

        <h1 class="text-3xl">
            Hey, {user.first_name}.
        </h1>

        <section class="flex flex-col gap-4 mt-4">
            <h2 class="mb-5">Organization • {organization?.name ?? "Loading..."}</h2>
            <InviteComponent /> <!-- only show if user is manager -->
        </section>

        <section id="projects" class="flex flex-col gap-5">
            <div class="flex flex-row items-center justify-between gap-4 mb-10">
                <h2 class="m-0">Projects • {projects.length}</h2>

                <button on:click={() => goto("/projects/new")}
                    class="btn !m-0 !w-max inline-block">
                    Add New
                </button>
            </div>

            <ol class="flex flex-wrap items-center justify-center gap-y-12 gap-x-4">
                {#each projects as project}
                    <ProjectCard project={project} />
                {/each}
            </ol>
        </section>
    </div>
{/if}

<script>
    import { goto } from "$app/navigation";
    import InviteComponent from "$lib/organization/InviteComponent.svelte";
    import ProjectCard from "$lib/projects/ProjectCard.svelte";

    export let data;
    let user = data.user;
    let projects = data.projects;
    let organization = data.organization;

    $: isLoading = !user && !projects && !organization
</script>