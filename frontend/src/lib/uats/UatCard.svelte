<li id="#{uat.id}" 
    class="p-10 text-white shadow-xl outline
    max-w-sm w-full relative overflow-hidden rounded-lg
    bg-gradient-to-tr from-yellow-500 to-amber-600
    flex flex-col justify-between gap-5">

    <CardType type={"Test"} />

    <span class="absolute text-sm top-0 right-0 p-4 opacity-60">
        <span class="select-none">
            ID:
        </span>
        <span>
            {uat.id}
        </span>
    </span>

    <div class="flex flex-col justify-between items-start">
        <span class="font-extralight text-md">Name</span>
        <h3 class="text-2xl font-bold">
            {uat.name}
        </h3>
    </div>

    <div class="flex flex-col justify-between items-start">
        <span class="font-extralight text-md">Description</span>
        <p class="text-xl">
            {uat.description}
        </p>
    </div>

    <div class="flex flex-col justify-between items-start">
        <span class="font-extralight text-md">Preconditions</span>
        <p class="text-xl">
            {uat.pre_conditions}
        </p>
    </div>

    <div class="flex flex-col justify-between items-start">
        <span class="font-extralight text-md">Steps</span>
        <p class="text-xl">
            {uat.steps}
        </p>
    </div>

    <div class="flex flex-col justify-between items-start">
        <span class="font-extralight text-md">Expected Result</span>
        <p class="text-xl">
            {uat.expected_result}
        </p>
    </div>

    <div class="flex flex-row gap-4">
        <a href="{url}/tests/{uat.id}/results/new"
        class="hover:scale-105
        flex flex-row items-center gap-2
        btn-secondary hover:bg-white dark:text-white dark:hover:text-black
        hover:text-black text-white 
        transition-all">

            <span style="background-image: url('/open.svg');" 
                class="hover transition-all block icon w-5 h-5" />

            New Result
        </a>

        <a href="{url}/tests/{uat.id}"
            class="hover:scale-105
            flex flex-row items-center gap-2
            btn-secondary hover:bg-white dark:text-white dark:hover:text-black
            hover:text-black text-white 
            transition-all">
            
            <span style="background-image: url('/open.svg');" 
                class="hover transition-all block icon w-5 h-5" />
            Details
        </a>
    </div>
</li>

<script>
    import { page } from '$app/stores';
    import CardType from "$lib/global/CardType.svelte";
    export let uat;

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