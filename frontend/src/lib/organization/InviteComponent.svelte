<script>
    $: email = ["", null]

    async function handleInvite() {
        try {
            const response = await fetch("apiURL", {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ email: email[0] })
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
</script>



<div class="flex flex-row items-center">
    <div 
        class:invalid={email[1] == false}
        class="input-container">

        <input 
            id="invitee_email"
            name="invitee_email"
            type="email" 
            placeholder="Invitee's Email"
            class=" shadow-md" />
    </div>

    <button on:click={handleInvite} class="btn !m-0 !w-max inline-block">
        Invite
    </button>
</div>