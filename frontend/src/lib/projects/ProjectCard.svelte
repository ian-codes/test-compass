<li id="#{project.id}" 
    class="p-10 text-white rounded-lg shadow-xl
    max-w-sm w-full relative outline outline-1
    bg-gradient-to-br from-cyan-600 to-blue-700 overflow-hidden
    flex flex-col justify-between gap-5 flex-auto">

    <CardType type={"Project"} />

    <span class="absolute text-sm top-0 right-0 p-4 opacity-60">
        <span class="select-none">
            ID:
        </span>
        <span>
            {project.id}
        </span>
    </span>

    <div class="flex flex-col justify-between items-start">
        <span class="font-extralight text-sm opacity-70">Name</span>
        <h3 class="text-2xl font-bold">
            {project.name}
        </h3>
    </div>

    <div class="flex flex-col justify-between items-start">
        <span class="font-extralight text-sm opacity-70">Description</span>
        <p class="text-lg">
            {project.description}
        </p>
    </div>

    <a href="/projects/{project.id}"
        class="hover:scale-105
        flex flex-row items-center gap-2
        btn-tertiary">
        
        <span style="background-image: url('/open.svg');" 
            class="hover transition-all block icon w-5 h-5" />
        
        Go to Project
    </a>
</li>


<script>
    import CardType from "$lib/global/CardType.svelte";
    export let project;
</script>


<style lang="postcss">
    .details-wrapper {
        @apply flex flex-row justify-between
    }
    a:hover .hover {
        @apply invert
    }
</style>