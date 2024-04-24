<script>
    import "../app.css";
    import Header from "../lib/Header.svelte";
</script>


<Header />
<main class="dark:text-white dark:bg-slate-500 h-full bg-slate-100">
    <slot />
</main>
