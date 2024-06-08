<div id="procedure-results"
    class="hidden min-h-lvh flex-col gap-5"
    class:visible={isVisible}>

    <div class="pb-8 flex flex-row gap-5 justify-between items-center">
        <h2>Procedure Results • {procedureResults.length}</h2>

        <button on:click={() => goto(`${slug}/new-test-procedure`)}
            class="btn !m-0 !w-max inline-block">
            Add New
        </button>
    </div>

    <ol class="flex flex-wrap items-center justify-center gap-4">
        {#each procedureResults as procedureResult}
            <ProcedureResultCard procedureResult={procedureResult} />
        {/each}
    </ol>
</div>

<script>
    import { goto } from "$app/navigation.js";
    import ProcedureResultCard from "./ProcedureResultCard.svelte";
    export let activeTab;
    export let procedureResults;
    export let slug;

    $: isVisible = activeTab == "results";
</script>

<style lang="postcss">
    .visible {
        @apply flex;
    }
</style>