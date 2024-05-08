<script>
    $: email = ["", null]
    $: password = ["", null]

    let loginFailed = false

    async function handleSubmit() {
        if (!validateInputs()) {
            return
        }

        let token = await makeLoginPostRequest()

        if (token == null) {
            loginFailed = true
        }

        resetInputValues()
    }

    function validateInputs() {
        email[1] = email[0] != "" && email[0]
        password[1] = password[0] != "" && password[0]
        return email[1] && password[1]
    }

    function resetInputValues() {
        email = ["", null]
        password = ["", null]
    }
    
    async function makeLoginPostRequest() {
        try {
            const response = await fetch("apiURL", {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ username: email[0], password: password[0] })
            })

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json()
            return data.token
        }
        catch {
            return null
        }
    }
</script>



<section class="dark:bg-slate-600  flex flex-col items-center gap-5 
    py-12 bg-slate-300">

    <h2 class="text-center text-xl font-mono font-extralight">
        Log In
    </h2>

    <form on:submit|preventDefault={handleSubmit}
        class="flex gap-2 flex-col items-center justify-center">

        <div 
            class:invalid={email[1] == false}
            class="input-container">
            <label for="email">
                Email
            </label>

            <input 
                bind:value={email[0]}
                id="email"
                name="email"
                type="email" />
        </div>

        <div 
            class:invalid={password[1] == false}
            class="input-container">
            <label for="password">
                Password
            </label>

            <input 
                bind:value={password[0]}
                id="password" 
                name="password"
                type="password"
                min="6" />
        </div>

        {#if loginFailed}
            <p>Login failed.</p>
        {/if}

        <button type="submit" class="mt-5 bg-primary px-4 py-2 rounded-lg w-full">
            Log In
        </button>
    </form>

    <a href="/register" class="text-sm underline">Don't have an account? Register here.</a>
</section>


<style>
    .input-container {
        @apply flex flex-col gap-1  p-2
    }
    .invalid {
        @apply outline outline-red-400 outline-2
    }
</style>