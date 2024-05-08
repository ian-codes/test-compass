<script>
    import { projects } from "$models/projects.js";
    import ProjectCard from "$lib/projects/ProjectCard.svelte";
</script>

<section class="flex flex-col gap-5">
    <h2>Projects • {projects.length}</h2>

    <ol class="flex flex-wrap items-center justify-center gap-4">
        {#each projects as project}
            <ProjectCard project={project} />
        {/each}
    </ol>
</section>