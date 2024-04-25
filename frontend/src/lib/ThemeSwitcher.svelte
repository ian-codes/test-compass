<script>
    let darkMode = false;
    const darkModeImg = "/darkmode.svg";
    const lightModeImg = "/lightmode.svg";

    function handleClick() {
        darkMode = !darkMode;

        darkMode
            ? document.documentElement.classList.add('dark')
            : document.documentElement.classList.remove('dark');
    }
</script>


<button title="toggle {(darkMode ? "light mode" : "dark mode")}" on:click={handleClick}
    class="hover:outline dark:hover:outline-black outline-slate-400 hover:scale-105 transition-all 
    z-20 relative rounded-full dark:invert bg-center bg-contain bg-no-repeat w-8 h-8"
    style="background-image: url('{(darkMode ? lightModeImg : darkModeImg)}')" />
