{#if isLoading}
    <h1 class="text-2xl">Loading...</h1>
{:else}
    <div class="flex flex-col justify-center items-center 
        gap-4 w-full m-auto"
        class:visible={!isLoading}>

        <h1 class="text-3xl">
            Hey, {user.first_name}.
        </h1>

        <section class="flex flex-col gap-4">
            <h2>Organization • {organization?.name ?? "Loading..."}</h2>
            <InviteComponent /> <!-- only show if user is manager -->
        </section>

        <!-- <section>
            <h2>Members • {members.length}</h2>

            <div class="overflow-scroll px-2 py-10">
                <ol class="flex flex-row gap-2 w-max">
                    {#each members as member}
                        <MemberCard member={member} />
                    {/each}
                </ol>
            </div>
        </section> -->

        <section id="projects" class="flex flex-col gap-5">
            <h2 class="m-0">Projects • {projects.length}</h2>

            <ol class="flex flex-wrap items-center justify-center gap-4">
                {#each projects as project}
                    <ProjectCard project={project} />
                {/each}
            </ol>
        </section>
    </div>
{/if}

<script>
    import InviteComponent from "$lib/organization/InviteComponent.svelte";
    import ProjectCard from "$lib/projects/ProjectCard.svelte";

    export let data;
    let user = data.user;
    let projects = data.projects;
    let organization = data.organization;

    $: isLoading = !user && !projects && !organization
</script>