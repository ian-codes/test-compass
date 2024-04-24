<script>
    import ThemeSwitcher from "./ThemeSwitcher.svelte";
</script>


<header class="sticky shadow-md shadow-slate-200 p-2 bg-slate-100 dark:bg-slate-500 flex flex-row items-center justify-between gap-2">
    <div class="flex flex-row gap-2 justify-start items-center">
        <span class="block bg-contain bg-center bg-no-repeat w-10 h-10" style="background-image: url('/logo.png')" />
        <span class="dark:text-white font-bold uppercase">Test Compass</span>
    </div>
    
    <ThemeSwitcher />
</header>