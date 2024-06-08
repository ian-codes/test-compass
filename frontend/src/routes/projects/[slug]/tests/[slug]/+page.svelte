{#if isLoading}
    <h1 class="text-2xl">Loading...</h1>
{:else}
    <div class="flex flex-col relative justify-center items-center 
        gap-4 w-full m-auto mt-0"
        class:visible={!isLoading}>

        <CardType type="User Acceptance Test" />

        <section class="flex flex-col gap-4 relative">
            <h1 class="text-3xl">
                {test.status}
            </h1>
            <span class="absolute text-sm top-0 right-0 p-4 opacity-60">
                <span class="select-none">
                    ID:
                </span>
                <span>
                    {data.slug}
                </span>
            </span>
            <p>
                {test.notes}
            </p>

            <div class="tap-container mt-24 mb-6 border-b-2
                border-orange-300 flex my-10flex-row justify-center">

                <button type="button" on:click={() => {return;}}
                    class="tab uats activeTab">
                    Test Results
                </button>
            </div>

            <UatResultList uatResults={testResults} />
        </section>
    </div>
{/if}



<script>
    import UatResultList from "$lib/uats/UatResultList.svelte";
    import CardType from "$lib/global/CardType.svelte";

    export let data;
    let test = data.test;
    let testResults = data.testResults;

    $: isLoading = !test && !testResults
</script>
