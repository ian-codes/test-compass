<script>
    let requestPayload = {
        email: "",
        password: "",
        first_name: "",
        last_name: "",
        organization_name: ""
    }

    $: first_name = ["", null]
    $: last_name = ["", null]
    $: email = ["", null]
    $: password = ["", null]
    $: isOrganizationManager = false
    $: organization_name = ["", null]


    async function handleSubmit() {
        if (!validateInputs())
            return

        generatePayload()
        console.log(requestPayload)
        await makeRegisterPostRequest()
    }


    function generatePayload() {
        requestPayload.email = email[0]
        requestPayload.password = password[0]
        requestPayload.first_name = first_name[0]
        requestPayload.last_name = last_name[0]
        requestPayload.organization_name = organization_name[0]
    }


    async function makeRegisterPostRequest() {
        const token = await fetch("apiURL", {
            method: 'POST',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(requestPayload)
        })
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



<section class="flex flex-col items-center gap-5 
    py-12 bg-slate-300">

    <h2 class="text-center text-xl font-mono font-extralight">
        Register
    </h2>

    <form on:submit={handleSubmit}
        class="flex flex-col gap-5 items-center justify-center">

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

        <button on:submit={handleSubmit} class="bg-primary px-4 py-2 rounded-lg w-full">Register</button>
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