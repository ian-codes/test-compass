<section id="procedure-results"
    class="min-h-lvh flex-col gap-5">

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
</section>

<script>
    import { goto } from "$app/navigation.js";
    import ProcedureResultCard from "./ProcedureResultCard.svelte";
    export let procedureResults;
    export let slug;
</script>