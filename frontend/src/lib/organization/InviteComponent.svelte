<script>
    const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;
    const INVITE_URL = `${BACKEND_URL}organization/invite/`;

    let email = "";
    let invalid = false;
    let hasFailed;
    $: submitText = hasFailed ? "Failed to send invite." : "Invite sent!";

    async function handleInvite() {
        if (!email.trim()) {
            invalid = true;
            alert("Please enter a valid email.");
            return;
        }
        try {
            const response = await fetch(INVITE_URL, {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ email: email }),
                credentials: 'include'
            })
            if (response.ok) {
                hasFailed = false;
            } else {
                hasFailed = false;
                invalid = false;
            }
        }
        catch {
            hasFailed = false;
        }
    }
</script>



<form on:submit|preventDefault={handleInvite} class="flex flex-row items-center">
    <div 
        class:invalid={email[1] == false}
        class="input-container !w-min">

        <input 
            bind:value={email}
            id="invitee_email"
            name="invitee_email"
            type="email" 
            placeholder="Invitee's Email"
            class=" shadow-md"
            class:invalid={invalid} />
    </div>

    <button
        type="submit"
        class="btn !m-0 !w-max inline-block">
        Invite
    </button>

    {#if hasFailed}
        <p>
            {submitText}
        </p>
    {/if}
</form>