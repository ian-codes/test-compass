<p>{statusMessage}</p>


<script>
    const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;
    const SIGN_OUT_URL = `${BACKEND_URL}account/logout/`;
    import { goto } from "$app/navigation.js";
    import { onMount } from "svelte";

    let statusMessage = "Signing you out...";

    onMount(async () => {
        try {
            let response = await signOut();
            if (response.ok) {
                statusMessage = "Signed out successfully!";
                goto("/");
            } else {
                statusMessage = "Failed to sign out. Please try again later.";
            }
        }
        catch {
            statusMessage = "Failed to sign out. Please try again later.";
        }
    });

    async function signOut() {
        return await fetch(SIGN_OUT_URL, {
            method: 'POST',
            headers: {
                "Content-Type": "application/json"
            },
            credentials: 'include'
        })
    }
</script>