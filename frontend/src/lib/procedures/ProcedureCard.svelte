<li id="#{procedure.id}" 
    class="p-10 text-white rounded-lg shadow-xl outline-1
    max-w-sm w-full relative overflow-hidden outline
    bg-gradient-to-tr from-purple-400 to-violet-600
    flex flex-col justify-between gap-5 flex-auto">

    <CardType type={"Procedure"} />

    <span class="absolute text-sm top-0 right-0 p-4 opacity-60">
        <span class="select-none">
            ID:
        </span>
        <span>
            {procedure.id}
        </span>
    </span>

    <div class="flex flex-col justify-between items-start">
        <span class="font-extralight text-sm opacity-70">Name</span>
        <h3 class="text-2xl font-bold">
            {procedure.name}
        </h3>
    </div>

    <div class="flex flex-col justify-between items-start">
        <span class="font-extralight text-sm opacity-70">Description</span>
        <p class="text-lg">
            {procedure.description}
        </p>
    </div>

    <a href="{url}/procedures/{procedure.id}"
        class="hover:scale-105
        flex flex-row items-center gap-2
        btn-tertiary hover:bg-white dark:text-white dark:hover:text-black
        hover:text-black text-white 
        transition-all">
        
        <span style="background-image: url('/open.svg');" 
            class="hover transition-all block icon w-5 h-5" />
        
        Show Details
    </a>
</li>


<script>
    import { page } from '$app/stores';
    import CardType from "$lib/global/CardType.svelte";
    export let procedure;

    let url = $page.url.pathname;
</script>


<style lang="postcss">
    .details-wrapper {
        @apply flex flex-row justify-between
    }
    a:hover .hover {
        @apply invert
    }
</style>