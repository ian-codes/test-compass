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

            <div class="flex flex-col gap-10">
                <div class="flex flex-col justify-between items-start">
                    <span class="font-extralight text-md">Description</span>
                    <p class="text-xl">
                        {procedure.description}
                    </p>
                </div>
            </div>

            <div class="mt-24">
                <UatList
                    buttonEnabled={false}
                    uats={tests}
                    bind:activeTab={activeTab} />
            </div>

            <!-- <ProcedureResultList 
                slug={data.slug} 
                procedureResults={procedureResults}
                bind:activeTab={activeTab} /> -->
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
        @apply bg-orange-400
    }
</style>