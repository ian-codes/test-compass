{#if isLoading}
    <h1>Loading...</h1>
{:else}
    <section class="dark:bg-slate-700  flex flex-col items-center gap-5 
        py-12 bg-slate-200">

        <h2 class="text-center text-xl font-mono font-extralight">
            New Test Procedure
        </h2>

        <form on:submit|preventDefault={handleSubmit}
            class="flex max-w-sm w-full gap-4 flex-col items-center justify-center">

            <div class="input-container">
                <label for="name">
                    Name
                </label>

                <input 
                    bind:value={procedure.name}
                    id="name"
                    name="name"
                    type="text"
                    minlength="3"
                    class:invalid={errors.name} />
            </div>

            <div class="input-container">
                <label for="description">
                    Description
                </label>

                <textarea 
                    bind:value={procedure.description}
                    id="description" 
                    name="description"
                    type="text"
                    minlength="10"
                    class:invalid={errors.description}
                    class="resize-y h-16 max-h-32"></textarea>
            </div>

            {#if tests.length}
                <div class="input-container mt-4 p-2 outline-1 outline rounded-lg outline-slate-400">
                    <label for="tests" 
                        class="relative flex flex-row justify-between items-center">

                        <button type="button"
                            class="absolute inset-0 opacity-0" 
                            on:click={() => showTests = !showTests} />

                        User Acceptance Tests ({chosenTests.length})

                        <span style="background-image: url('/expand.svg');"
                            class="inline-block invert dark:invert-0 bg-no-repeat 
                            bg-center bg-contain w-4 h-4 {(showTests ? "rotate-180" : "")}" />
                    </label>

                    <ol name="tests" class="hidden mt-4 flex-col gap-2"
                        class:show={showTests}>
                        {#each tests as test}
                            <li class="relative gap-4 flex flex-row items-baseline justify-between p-2 outline-slate-400 outline outline-1 rounded-lg"
                                class:chosen={chosenTests.includes(test)}>
                                <button 
                                    type="button" 
                                    class="absolute inset-0 opacity-0" 
                                    on:click={() => handleTestClick(test)}/>
        
                                <span>
                                    {test.name}
                                </span>

                                <span class="text-sm opacity-60">
                                    <span class="select-none">
                                        ID:
                                    </span>
                                    <span>
                                        {test.id}
                                    </span>
                                </span>
                            </li>
                        {/each}
                    </ol>
                </div>
            {/if}

            {#if createFailed}
                <p>Failed to create test procedure.</p>
            {/if}

            <div class="w-full">
                <button type="submit" class="btn">
                    Create
                </button>
    
                <button 
                    on:click={() => goto(back_url)}
                    type="reset" 
                    class="btn-secondary">
                    Discard
                </button>
            </div>
        </form>
    </section>
{/if}

<script>
    import { goto } from "$app/navigation.js";
    const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;

    export let data;

    $: showTests = false;

    function handleTestClick(test) {
        const index = chosenTests.indexOf(test);
        if (index !== -1) {
            chosenTests.splice(index, 1);
        } else {
            chosenTests.push(test);
        }
        chosenTests = chosenTests.slice(); // Reassign to trigger reactivity
    }

    let chosenTests = [];

    let tests = data.uats;

    const back_url = `/projects/${data.slug}`;

    $: isLoading = !tests;

    let createFailed = false;

    let procedure = {
        name: "",
        description: "",
    }

    let errors = {
        name: false,
        description: false
    }

    async function handleSubmit() {
        if (!areInputsValid()) {
            alert("Please fill in the input fields.");
            return;
        }
        try {
            const response = await makeCreateProcedurePostRequest();
            if (response.ok) {
                createFailed = false;
                goto(back_url);
            } else {
                createFailed = true;
            }
        } catch {
            createFailed = true;
        }
    }

    function areInputsValid() {
        errors.name = !procedure.name.trim();
        errors.description = !procedure.description.trim();
        return !Object.values(errors).includes(true);
    }

    async function makeCreateProcedurePostRequest() {
        procedure.acceptance_tests = chosenTests.map(test => test.id);

        const url = `${BACKEND_URL}projects/${data.slug}/procedures/new/`;

        console.log(procedure)
        return await fetch(url, {
            method: 'POST',
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(procedure),
            credentials: 'include'
        })
    }
</script>


<style lang="postcss">
    .chosen {
        @apply bg-gradient-to-bl from-orange-300 to-orange-400 text-black;
    }
    .show {
        display: flex !important;
    }
</style>