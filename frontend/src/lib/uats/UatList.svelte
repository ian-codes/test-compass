<div id="user-acceptance-tests"
    class="hidden min-h-lvh flex-col gap-5"
    class:visible={isVisible}>

    <div class="pb-8 flex flex-row gap-5 justify-between items-center">
        <h2>User Acceptance Tests • {uats.length}</h2>

        {#if buttonEnabled}
            <button on:click={() => goto(`${url}/tests/new`)}
                class="btn !m-0 !w-max inline-block">
                Add New
            </button>
        {/if}
    </div>

    <ol class="flex flex-wrap justify-center gap-y-12 gap-x-4">
        {#each uats as uat}
            <UatCard uat={uat} />
        {/each}
    </ol>
</div>

<script>
    import { page } from "$app/stores";
    import { goto } from "$app/navigation.js";
    import UatCard from "./UatCard.svelte";
    export let uats;
    export let activeTab;
    export let buttonEnabled;

    let url = $page.url.pathname;

    $: isVisible = activeTab == "uats";
</script>

<style lang="postcss">
    .visible {
        @apply flex;
    }
</style>