{#if isLoading}
    <h1 class="text-2xl">Loading...</h1>
{:else}
    <div class="flex flex-col relative justify-center items-center 
        gap-4 w-full m-auto mt-0"
        class:visible={!isLoading}>

        <section class="flex flex-col gap-4 relative">
            <h1 class="text-3xl">
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
            <p>
                {procedure.description}
            </p>
        </section>
    </div>
{/if}



<script>
    export let data;
    let procedure = data.procedure;
    let procedureResults = data.procedureResults;
    let tests = data.procedure?.tests;

    $: isLoading = !procedure && !procedureResults && !tests
</script>
