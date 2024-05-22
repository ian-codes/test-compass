<script>
    import InviteComponent from "$lib/organization/InviteComponent.svelte";
    import { members } from "$models/members.js";
    import { projects } from "$models/projects.js";
    import ProjectCard from "$lib/projects/ProjectCard.svelte";
    import MemberCard from "$lib/organization/MemberCard.svelte";
</script>


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


<section class="flex flex-col gap-5">
    <h2>Projects • {projects.length}</h2>

    <ol class="flex flex-wrap items-center justify-center gap-4">
        {#each projects as project}
            <ProjectCard project={project} />
        {/each}
    </ol>
</section>