<section class="flex min-h-lvh flex-col gap-5">
    {#if procedures}
        <div class="flex flex-row gap-5 justify-start items-center">
            <h2>Test Procedures • {procedures.length}</h2>

            <button on:click={handleCreateNew}
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


<section class="flex min-h-lvh flex-col gap-5">
    {#if uats}
        <div class="flex flex-row gap-5 justify-start items-center">
            <h2>User Acceptance Tests • {uats.length}</h2>

            <button on:click={handleCreateNew}
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
    import { onMount } from "svelte";
    import { goto } from "$app/navigation.js";
    import ProcedureCard from "$lib/procedures/ProcedureCard.svelte";

    export let data;

    const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;
    let get_test_procedures_url;

    let procedures;

    onMount(async () => {
        get_test_procedures_url = `${BACKEND_URL}organizations/projects/${data.id}/testprocedures/`;
        procedures = await getTestProcedures();
    });

    async function getTestProcedures() {
        try {
            const response = await fetch(get_test_procedures_url, {
                method: 'GET',
                credentials: 'include'
            });
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return await response.json();
        } catch (error) {
            console.error('There was a problem with the fetch operation:', error);
        }
    }

    function handleCreateNew() {
        goto(`${data.id}/new-test-procedure`)
    }
</script>