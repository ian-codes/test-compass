<section class="flex flex-col gap-4 relative">
    <h1 class="text-3xl text-center">
        {project.name}
    </h1>
    <span class="absolute text-sm top-0 right-0 p-4 opacity-60">
        <span class="select-none">
            ID:
        </span>
        <span>
            {project.id}
        </span>
    </span>
    <p>
        {project.description}
    </p>
    <div>
</section>




<div class="flex flex-row justify-center">
    <button on:click={() => activeTab = "procedures"}
        class="tab"
        class:activeTab={activeTab == "procedures"}>
        Test Procedures
    </button>
    <button on:click={() => activeTab = "uats"}
        class="tab"
        class:activeTab={activeTab == "uats"}>
        User Acceptance Tests
    </button>
</div>


<section id="procedures"
    class="hidden min-h-lvh flex-col gap-5"
    class:visible={activeTab == "procedures"}>
    {#if procedures}
        <div class="flex flex-row gap-5 justify-between items-center">
            <h2>Test Procedures • {procedures.length}</h2>

            <button on:click={() => goto(`${data.slug}/new-test-procedure`)}
                class="btn !m-0 !w-max inline-block">
                Add New
            </button>
        </div>

        <ol class="flex flex-wrap items-center justify-center gap-4">
            {#each procedures as procedure}
                <ProcedureCard procedure={procedure} />
            {/each}
        </ol>
    {:else}
        <p class="text-center">Loading procedures...</p>
    {/if}
</section>


<section id="user-acceptance-tests"
    class="hidden min-h-lvh flex-col gap-5"
    class:visible={activeTab == "uats"}>
    {#if uats}
        <div class="flex flex-row gap-5 justify-between items-center">
            <h2>User Acceptance Tests • {uats.length}</h2>

            <button on:click={() => goto(`${data.slug}/new-user-acceptance-test`)}
                class="btn !m-0 !w-max inline-block">
                Add New
            </button>
        </div>

        <ol class="flex flex-wrap items-center justify-center gap-4">
            {#each uats as uat}
                <UatCard procedure={uat} />
            {/each}
        </ol>
    {:else}
        <p class="text-center">Loading user acceptance tests...</p>
    {/if}
</section>


<script>
    import { goto } from "$app/navigation.js";
    import ProcedureCard from "$lib/procedures/ProcedureCard.svelte";
    import UatCard from "$lib/uats/UatCard.svelte";

    export let data;
    let project = data.project;
    let procedures = data.procedures;
    let uats = data.uats;

    let activeTab = "procedures";
</script>


<style lang="postcss">
    .activeTab {
        @apply bg-slate-200 dark:bg-slate-700 outline-1 outline;
    }
    .tab {
        @apply px-4 py-2 rounded-md;
    }
    .visible {
        @apply flex;
    }
</style>