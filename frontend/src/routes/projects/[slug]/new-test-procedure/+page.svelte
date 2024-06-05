<section class="dark:bg-slate-700  flex flex-col items-center gap-5 
    py-12 bg-slate-200">

    <h2 class="text-center text-xl font-mono font-extralight">
        New Test Procedure
    </h2>

    <form on:submit|preventDefault={handleSubmit}
        class="flex max-w-sm w-full gap-2 flex-col items-center justify-center">

        <div 
            class="input-container">
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

        <div 
            class="input-container">
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

        {#if createFailed}
            <p>Failed to create test procedure.</p>
        {/if}

        <button type="submit" class="btn">
            Create
        </button>

        <button type="reset" class="btn-secondary">
            Discard
        </button>
    </form>
</section>


<script>
    import { goto } from "$app/navigation.js";
    const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;

    export let data;

    console.log(data);

    let createFailed = false;

    let procedure = {
        name: "",
        description: ""
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
                goto("/");
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
        const url = `${BACKEND_URL}organizations/projects/${data.slug}/testprocedures/create/`;
        return await fetch(url, {
            method: 'POST',
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(procedure),
            credentials: 'include'
        })
    }
</script>