<script>
    export let project;
</script>

<li id="#{project.id}" 
    class="p-10 text-white rounded-lg shadow-xl
    max-w-sm w-full relative
    bg-gradient-to-tr from-cyan-400 to-blue-600
    flex flex-col justify-between gap-5">

    <span class="absolute text-sm top-0 right-0 p-4 opacity-60">
        <span class="select-none">
            ID:
        </span>
        <span>
            {project.id}
        </span>
    </span>

    <div class="flex flex-col justify-between items-start">
        <span class="font-extralight text-md">Name</span>
        <h3 class="text-2xl font-bold">
            {project.name}
        </h3>
    </div>

    <div class="flex flex-col justify-between items-start">
        <span class="font-extralight text-md">Description</span>
        <p class="text-xl">
            {project.description}
        </p>
    </div>

    <a href="/projects/{project.id}"
        class="hover:scale-105
        flex flex-row items-center gap-2
        btn-secondary hover:bg-white dark:text-white dark:hover:text-black
        hover:text-black text-white 
        transition-all">
        
        <span style="background-image: url('/open.svg');" 
            class="hover transition-all block icon w-5 h-5" />
        
        Go to Project
    </a>
</li>

<style lang="postcss">
    .details-wrapper {
        @apply flex flex-row justify-between
    }
    a:hover .hover {
        @apply invert
    }
</style>