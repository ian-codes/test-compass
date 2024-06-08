<script>
    const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;
    const GET_USER_URL = `${BACKEND_URL}organizations/user/`;

    import "../app.css";
    import Header from "$lib/global/Header.svelte";
    import { goto } from "$app/navigation";
    import { onMount } from "svelte";
    import { page } from '$app/stores';
    import { loggedIn } from '../stores/userAuth';

    let initialized = false;

    $: if (initialized && $page.url.pathname) {
        checkAuth();
    }

    onMount(async () => {
        initialized = true;
        await checkAuth();
    })

    async function checkAuth() {
        console.log($page.url.pathname)
        console.log($loggedIn)
        const response = await fetch(GET_USER_URL, {
            method: 'GET',
            credentials: 'include'
        });
        if (response.status == 401) {
            loggedIn.set(false);
            if ($page.url.pathname != '/register') {
                goto("/login");
            }
        } else {
            loggedIn.set(true)
        }
    }
</script>


<div class="min-h-dvh overflow-x-hidden relative">
    <div class="inset-0 absolute hidden
    bg-gradient-to-r from-slate-500 via-transparent to-slate-500" />

    <Header />
    <main class="dark:text-white dark:bg-slate-800
        h-full bg-slate-100 p-2 py-8 min-h-lvh
        flex flex-col items-center gap-10">
        <slot />
    </main>
</div>

