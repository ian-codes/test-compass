<script>
    import Nav from "./Nav.svelte";
    import ThemeSwitcher from "./ThemeSwitcher.svelte";
</script>


<header class="shadow-md shadow-slate-200 py-4 p-1 bg-slate-100 dark:bg-slate-800 flex flex-row items-center justify-between gap-2">
    <a href="/" title="home" class="z-50 relative cursor-pointer p-2 rounded-lg hover:bg-white hover:bg-opacity-10 transition-all
    flex flex-row gap-2 justify-start items-center">
        <div class="absolute inset-0" />
        <span class="drop-shadow-lg rounded-full shadow-slate-200 block bg-contain bg-center bg-no-repeat w-10 h-10" style="background-image: url('/logo.png')" />
        <span class="dark:text-white tracking-widest uppercase">Test Compass</span>
    </a>
    
    <div class="flex flex-row items-cente gap-5">
        <ThemeSwitcher />
        <Nav />
    </div>
</header>

<style>
    @keyframes spinning {
        0% {transform: rotate(0)}
        100% {transform: rotate(360)}
    }
</style>