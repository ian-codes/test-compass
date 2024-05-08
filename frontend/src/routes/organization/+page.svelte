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


<section>
    <h1>Orgnization</h1>

    <div class="flex flex-col">
        <div 
            class:invalid={email[1] == false}
            class="input-container">

            <label for="invitee_email">
                Invite a User to your Organization
            </label>
            <input 
                id="invitee_email"
                name="invitee_email"
                type="email" 
                placeholder="Invitee's Email" />
        </div>

        <button on:click={handleInvite} class="btn">
            Invite User to Organization
        </button>
    </div>

</section>