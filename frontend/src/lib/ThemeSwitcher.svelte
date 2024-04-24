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


<button on:click={handleClick}
    class="dark:invert bg-center bg-contain bg-no-repeat w-8 h-8"
    style="background-image: url('{(darkMode ? lightModeImg : darkModeImg)}')" />
