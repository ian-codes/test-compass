<section id="user-acceptance-tests"
    class="hidden min-h-lvh flex-col gap-5"
    class:visible={isVisible}>

    <div class="pb-8 flex flex-row gap-5 justify-between items-center">
        <h2>User Acceptance Tests • {uats.length}</h2>

        <button on:click={() => goto(`${slug}/new-user-acceptance-test`)}
            class="btn !m-0 !w-max inline-block">
            Add New
        </button>
    </div>

    <ol class="flex flex-wrap items-center justify-center gap-4">
        {#each uats as uat}
            <UatCard uat={uat} />
        {/each}
    </ol>
</section>

<script>
    import { goto } from "$app/navigation.js";
    import UatCard from "./UatCard.svelte";
    export let uats;
    export let activeTab;
    export let slug;

    $: isVisible = activeTab == "uats";
</script>

<style lang="postcss">
    .visible {
        @apply flex;
    }
</style>