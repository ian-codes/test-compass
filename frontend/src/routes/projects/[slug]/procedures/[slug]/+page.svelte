{#if isLoading}
    <h1 class="text-2xl">Loading...</h1>
{:else}
    <div class="flex flex-col relative justify-center items-center 
        gap-4 w-full m-auto mt-0"
        class:visible={!isLoading}>

        <section class="flex flex-col gap-4 relative overflow-hidden">
            <CardType type="Test Procedure" />

            <h1 class="text-3xl text-center">
                {procedure.name}
            </h1>
            <span class="absolute text-sm top-0 right-0 p-4 opacity-60">
                <span class="select-none">
                    ID:
                </span>
                <span>
                    {data.slug}
                </span>
            </span>
            <p class="text-center mt-10">
                {procedure.description}
            </p>


            <div class="tap-container mt-24 mb-6 border-b-2
                {(activeTab == "results" ? "border-purple-300" : "border-orange-300")}
                flex my-10flex-row justify-center">

                <button on:click={() => activeTab = "uats"}
                    class="tab uats"
                    class:activeTab={activeTab == "uats"}>
                    User Acceptance Tests
                </button>

                <button on:click={() => activeTab = "results"}
                    class="tab results"
                    class:activeTab={activeTab == "results"}>
                    Test Procedure Results
                </button>
            </div>

            <UatList
                uats={tests}
                bind:activeTab={activeTab} />

            <ProcedureResultList 
                slug={data.slug} 
                procedureResults={procedureResults}
                bind:activeTab={activeTab} />
        </section>
    </div>
{/if}

<script>
    import CardType from "$lib/global/CardType.svelte";
    import UatList from "$lib/uats/UatList.svelte";
    import ProcedureResultList from "$lib/procedures/ProcedureResultList.svelte";

    export let data;
    let procedure = data.procedure;
    let procedureResults = data.procedureResults;
    let tests = data.procedure?.tests;

    let activeTab = "uats";

    $: isLoading = !procedure && !procedureResults && !tests
</script>


<style lang="postcss">
    .activeTab.results {
        @apply bg-purple-300
    }
    .activeTab.uats {
        @apply bg-orange-300
    }
</style>