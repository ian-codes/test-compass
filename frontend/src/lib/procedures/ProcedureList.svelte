<section id="procedures"
    class="hidden min-h-lvh flex-col gap-5"
    class:visible={isVisible}>

    <div class="pb-8 flex flex-row gap-5 justify-between items-center">
        <h2>Test Procedures • {procedures.length}</h2>

        <button on:click={() => goto(`${slug}/new-test-procedure`)}
            class="btn !m-0 !w-max inline-block">
            Add New
        </button>
    </div>

    <ol class="flex flex-wrap items-center justify-center gap-4">
        {#each procedures as procedure}
            <ProcedureCard procedure={procedure} />
        {/each}
    </ol>
</section>

<script>
    import { goto } from "$app/navigation.js";
    import ProcedureCard from "./ProcedureCard.svelte";
    export let procedures;
    export let activeTab;
    export let slug;

    $: isVisible = activeTab == "procedures";
</script>

<style lang="postcss">
    .visible {
        @apply flex;
    }
</style>