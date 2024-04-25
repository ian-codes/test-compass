<script>
    import "../app.css";
    import Header from "../lib/Header.svelte";
</script>


<div class="min-h-dvh overflow-x-hidden relative">
    <div class="inset-0 absolute hidden
    bg-gradient-to-r from-slate-500 via-transparent to-slate-500" />

    <Header />
    <main class="dark:text-white dark:bg-slate-500
        h-full bg-slate-100">
        <slot />
    </main>
</div>

