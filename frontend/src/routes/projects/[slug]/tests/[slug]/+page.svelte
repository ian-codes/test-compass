{#if isLoading}
    <h1 class="text-2xl">Loading...</h1>
{:else}
    <div class="flex flex-col relative justify-center items-center 
        gap-4 w-full m-auto mt-0"
        class:visible={!isLoading}>

        <section class="flex flex-col gap-4 relative text-center overflow-hidden">
            <CardType type="User Acceptance Test" />

            <h1 class="text-3xl mb-10">
                {test.name}
            </h1>

            <span class="absolute text-sm top-0 right-0 p-4 opacity-60">
                <span class="select-none">
                    ID:
                </span>
                <span>
                    1
                </span>
            </span>

            <div class="flex flex-col gap-10 py-8">
                <div class="flex flex-col justify-between items-start">
                    <span class="font-extralight text-md">Description</span>
                    <p class="text-xl">
                        {test.description}
                    </p>
                </div>
    
                <div class="flex flex-col justify-between items-start">
                    <span class="font-extralight text-md">Preconditions</span>
                    <p class="text-xl">
                        {test.pre_conditions}
                    </p>
                </div>
    
                <div class="flex flex-col justify-between items-start">
                    <span class="font-extralight text-md">Steps</span>
                    <p class="text-xl">
                        {test.steps}
                    </p>
                </div>
    
                <div class="flex flex-col justify-between items-start">
                    <span class="font-extralight text-md">Expected Result</span>
                    <p class="text-xl">
                        {test.expected_result}
                    </p>
                </div>
    
                <div class="flex flex-col justify-between items-start">
                    <span class="font-extralight text-md">Created by</span>
                    <p class="text-xl">
                        {test.creator}
                    </p>
                </div>
            </div>

            <div class="mt-12">
                <UatResultList slug={data.slug} uatResults={testResults} />
            </div>
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
