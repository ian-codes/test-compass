<div id="procedures"
    class="hidden min-h-lvh flex-col gap-5"
    class:visible={isVisible}>

    <div class="pb-8 flex flex-row gap-5 justify-between items-center">
        <h2>Test Procedures • {procedures.length}</h2>

        <button on:click={() => goto(`${url}/procedures/new`)}
            class="btn !m-0 !w-max inline-block">
            Add New
        </button>
    </div>

    <ol class="flex flex-wrap justify-center gap-y-12 gap-x-4">
        {#each procedures as procedure}
            <ProcedureCard procedure={procedure} />
        {/each}
    </ol>
</div>

<script>
    import { page } from "$app/stores";
    import { goto } from "$app/navigation.js";
    import ProcedureCard from "./ProcedureCard.svelte";
    export let procedures;
    export let activeTab;

    let url = $page.url.pathname;

    $: isVisible = activeTab == "procedures";
</script>

<style lang="postcss">
    .visible {
        @apply flex;
    }
</style>