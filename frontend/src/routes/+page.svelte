<section>
    <h2>Organization</h2>
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


{#if data.projects}
    <section id="projects" class="flex flex-col gap-5">
        <h2 class="m-0">Projects • {data.projects.length}</h2>

        <ol class="flex flex-wrap items-center justify-center gap-4">
            {#each data.projects as project}
                <ProjectCard project={project} />
            {/each}
        </ol>
    </section>
{/if}



<script>
    import InviteComponent from "$lib/organization/InviteComponent.svelte";
    import ProjectCard from "$lib/projects/ProjectCard.svelte";

    export let data;
</script>