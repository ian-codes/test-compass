<script>
    export let project;
</script>

<li class="p-10 text-white rounded-lg shadow-xl
    max-w-sm w-full
    bg-gradient-to-tr from-cyan-400 to-blue-600
    flex flex-col justify-between gap-2">
    
    <h3 class="text-xl font-bold">
        {project.name}
    </h3>

    <div class="details-wrapper">
        {project.description}
    </div>


    <a href="/projects/{project.id}"
        class="hover:scale-105
        flex flex-row items-center gap-2
        btn-secondary hover:bg-white 
        hover:text-black text-white 
        transition-all">
        
        <span style="background-image: url('/open.svg');" 
            class="hover transition-all block icon w-5 h-5" />
        
        Details
    </a>
</li>

<style>
    .details-wrapper {
        @apply flex flex-row justify-between
    }
    a:hover .hover {
        @apply invert
    }
</style>