<section class="dark:bg-slate-700  flex flex-col items-center gap-5 
    py-12 bg-slate-200">

    <h2 class="text-center text-xl font-mono font-extralight">
        New User Acceptance Test Result
    </h2>

    <form on:submit|preventDefault={handleSubmit}
        class="flex max-w-sm w-full gap-2 flex-col items-center justify-center">

        <div 
            class="input-container">
            <label for="status">
                Status
            </label>

            <input 
                bind:value={testResult.status}
                id="status"
                name="status"
                type="text"
                minlength="1"
                class:invalid={errors.status} />
        </div>

        <div 
            class="input-container">
            <label for="notes">
                Notes
            </label>

            <textarea 
                bind:value={testResult.notes}
                id="notes" 
                name="notes"
                type="text"
                class:invalid={errors.notes}
                class="resize-y h-16 max-h-32"></textarea>
        </div>

        {#if createFailed}
            <p>Failed to add the result.</p>
        {/if}

        <button type="submit" class="btn">
            Create
        </button>

        <button 
            on:click={() => goto($backUrl)}
            type="reset" 
            class="btn-secondary">
            Discard
        </button>
    </form>
</section>


<script>
    import { backUrl } from '$lib/backUrlStore.js';

    import { page} from "$app/stores";
    import { goto } from "$app/navigation.js";

    export let data;

    const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;

    const currentUrl = $page.url.pathname.slice(1);
    let requestUrl = `${BACKEND_URL}${currentUrl}/`;

    const back_url = `/`;

    let createFailed = false;

    let testResult = {
        status: "",
        notes: ""
    }

    let errors = {
        status: false,
        notes: false
    }

    async function handleSubmit() {
        if (!areInputsValid()) {
            alert("Please fill in the input fields.");
            return;
        }
        try {
            const response = await makeRequest(requestUrl);
            if (response.ok) {
                createFailed = false;
                goto($backUrl);
            } else {
                createFailed = true;
            }
        } catch {
            createFailed = true;
        }
    }

    function areInputsValid() {
        errors.status = !testResult.status.trim();
        errors.notes = !testResult.notes.trim();
        return !Object.values(errors).includes(true);
    }

    async function makeRequest(url) {
        return await fetch(url, {
            method: 'POST',
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(testResult),
            credentials: 'include'
        })
    }
</script>