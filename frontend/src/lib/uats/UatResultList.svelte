<section id="user-acceptance-tests"
    class="min-h-lvh flex-col gap-5">

    <div class="pb-8 flex flex-row gap-5 justify-between items-center">
        <h2>User Acceptance Tests Results • {uatResults.length}</h2>

        <button on:click={() => goto(`${slug}/new-user-acceptance-test`)}
            class="btn !m-0 !w-max inline-block">
            Add New
        </button>
    </div>

    <ol class="flex flex-wrap items-center justify-center gap-4">
        {#each uatResults as uatResult}
            <UatResultCard uatResult={uatResult} />
        {/each}
    </ol>
</section>

<script>
    import { goto } from "$app/navigation.js";
    import UatResultCard from "./UatResultCard.svelte";
    export let uatResults;
    export let slug;
</script>