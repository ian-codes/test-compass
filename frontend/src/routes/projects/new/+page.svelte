<section class="flex flex-col items-center gap-5 
    py-12  visible">

    <h2 class="text-center text-xl font-mono font-extralight">
        Create New Project
    </h2>

    <form on:submit|preventDefault={handleSubmit}
        class="flex max-w-sm w-full gap-2 flex-col items-center justify-center">

        <div 
            class="input-container">
            <label for="name">
                Name
            </label>

            <input 
                bind:value={project.name}
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
                bind:value={project.description}
                id="description" 
                name="description"
                type="text"
                minlength="10"
                class:invalid={errors.description}
                class="resize-y h-16 max-h-32"></textarea>
        </div>

        {#if createFailed}
            <p>Failed to create project.</p>
        {/if}

        <button type="submit" class="btn">
            Create
        </button>

        <button on:click={() => goto("/")} type="reset" class="btn-secondary">
            Discard
        </button>
    </form>
</section>


<script>
    import { goto } from "$app/navigation.js";
    const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;
    const CREATE_PROJECT_URL = `${BACKEND_URL}projects/new/`;
    let createFailed = false;

    let project = {
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
            const response = await makeCreateProjectPostRequest();
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
        errors.name = !project.name.trim();
        errors.description = !project.description.trim();
        return !Object.values(errors).includes(true);
    }

    async function makeCreateProjectPostRequest() {
        return await fetch(CREATE_PROJECT_URL, {
            method: 'POST',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(project),
            credentials: 'include'
        })
    }
</script>