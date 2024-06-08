{#if isLoading}
    <h1 class="text-2xl">Loading...</h1>
{:else}
    <div class="flex flex-col justify-start items-center 
        gap-4 w-full m-auto"
        class:visible={!isLoading}>

        <section class="flex flex-col gap-4 relative">
            <h1 class="text-3xl">
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

            <div class="tap-container mt-24 mb-6 border-b-2
                {(activeTab == "procedures" ? "border-purple-300" : "border-orange-300")}
                flex my-10flex-row justify-center">

                <button on:click={() => activeTab = "procedures"}
                    class="tab procedures"
                    class:activeTab={activeTab == "procedures"}>
                    Test Procedures
                </button>
                <button on:click={() => activeTab = "uats"}
                    class="tab uats"
                    class:activeTab={activeTab == "uats"}>
                    User Acceptance Tests
                </button>
            </div>

            <ProcedureList 
                procedures={procedures} 
                bind:activeTab={activeTab} />

            <UatList 
                uats={uats} 
                bind:activeTab={activeTab} />
        </section>
    </div>
{/if}



<script>
    import UatList from "$lib/uats/UatList.svelte";
    import ProcedureList from "$lib/procedures/ProcedureList.svelte";

    export let data;
    let project = data.project;
    let procedures = data.procedures;
    let uats = data.uats;

    let activeTab = "procedures";

    $: isLoading = !project && !procedures && !uats
</script>


<style lang="postcss">
    .activeTab {
        @apply bg-slate-300 dark:bg-slate-500 dark:text-black;
    }
    .tab {
        @apply px-4 py-2 rounded-t-lg;
    }
    .activeTab.procedures {
        @apply bg-purple-300
    }
    .activeTab.uats {
        @apply bg-orange-300
    }
</style>