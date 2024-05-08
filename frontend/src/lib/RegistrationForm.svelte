<script>
    $: first_name = ["", null]
    $: last_name = ["", null]
    $: email = ["", null]
    $: password = ["", null]
    $: isOrganizationManager = false
    $: organization_name = ["", null]

    let registrationFailed = false

    async function handleSubmit() {
        if (!validateInputs())
            return

        await makeRegisterPostRequest()

        resetInputValues()
    }

    function generatePayload() {
        return {
            email: email[0],
            password: password[0],
            first_name: first_name[0],
            last_name: last_name[0],
            organization_name: organization_name[0]
        }
    }

    function resetInputValues() {
        first_name = ["", null]
        last_name = ["", null]
        email = ["", null]
        password = ["", null]
        isOrganizationManager = false
        organization_name = ["", null]
    }

    async function makeRegisterPostRequest() {
        let payload = generatePayload()

        try {
            const response = await fetch("apiURL", {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(payload)
            })

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json()
            return data.token
        }
        catch {

        }
    }


    function handleStatusChange() {
        isOrganizationManager = !isOrganizationManager
    }


    function validateInputs() {
        first_name[1] = first_name[0] != "" && first_name[0]
        last_name[1] = last_name[0] != "" && last_name[0]
        email[1] = email[0] != "" && email[0]
        password[1] = password[0] != "" && password[0]

        if (isOrganizationManager) {
            organization_name[1] = organization_name[0] != "" && organization_name[0]
            return first_name[1] && last_name[1] && email[1] && password[1] && organization_name[1]
        }

        return first_name[1] && last_name[1] && email[1] && password[1]
    }
</script>



<section class="dark:bg-slate-600 flex flex-col items-center gap-5 
    py-12 bg-slate-300">

    <h2 class="text-center text-xl font-mono font-extralight">
        Register
    </h2>

    <form on:submit={handleSubmit}
        class="flex gap-2 flex-col items-center justify-center">

        <div 
            class:invalid={first_name[1] == false}
            class="input-container">
            <label for="firstName">
                First Name
            </label>
            <input
                bind:value={first_name[0]}
                id="firstName"
                name="firstName"
                type="text" />
        </div>

        <div 
            class:invalid={last_name[1] == false}
            class="input-container">
            <label for="lastName">
                Last Name
            </label>
            <input
                bind:value={last_name[0]}
                id="lastName"
                name="lastName"
                type="text" />
        </div>

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

        <div>
            <input 
                on:change={handleStatusChange}
                id="isOrganizationManager"
                name="isOrganizationManager"
                type="checkbox" />
            <label for="isOrganizationManager">
                Organization Manager
            </label>
        </div>

        {#if isOrganizationManager}
            <div
                class:invalid={organization_name[1] == false}
                class="input-container">
                <label for="organization">
                    Organization Name
                </label>
                <input 
                    bind:value={organization_name[0]}
                    id="organization"      
                    name="organization"              
                    type="text" />
            </div>
        {/if}

        {#if registrationFailed}
            <p>Failed to register.</p>
        {/if}

        <button on:submit={handleSubmit} 
            class="bg-primary mt-5 px-4 py-2 rounded-lg w-full">
            Register
        </button>
    </form>

    <a href="/login" class="text-sm underline">Already registered? Log in here.</a>
</section>


<style>
    .input-container {
        @apply flex flex-col gap-1  p-2
    }
    .invalid {
        @apply outline outline-red-400 outline-2
    }
</style>