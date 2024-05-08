<script>
    import "../app.css";
    import Header from "$lib/global/Header.svelte";
</script>


<div class="min-h-dvh overflow-x-hidden relative">
    <div class="inset-0 absolute hidden
    bg-gradient-to-r from-slate-500 via-transparent to-slate-500" />

    <Header />
    <main class="dark:text-white dark:bg-slate-500
        h-full bg-slate-100 p-2 py-8
        flex flex-col gap-10">
        <slot />
    </main>
</div>

