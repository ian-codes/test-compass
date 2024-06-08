<nav class="block inset-0 overflow-x-hidden max-w-full">

    <button on:click={handleClick} class="relative dark:hover:bg-slate-600 hover:bg-slate-200 rounded-lg 
        transition-al cursor-pointer p-1.5 z-20 w-10 h-8 flex flex-col justify-between items-center">
        {#each {length: 3} as _}
            <span class="dark:bg-white h-0.5 rounded-sm w-full bg-black" />
        {/each}
    </button>

    <ul class="{(isOpen ? "right-0 w-full" : "-right-full w-0")} z-10 transition-all 
        absolute pt-24 max-w-fulldark:bg-slate-700 outline bg-slate-200 top-0 h-min 
        bottom-0 flex flex-col">

        {#if $loggedIn}
            <NavItem 
                slug={"/"}
                title={"Home"} 
                onClick={handleClick} 
            />

            <NavItem 
                slug={"/projects"}
                title={"Projects"} 
                onClick={handleClick} 
            />

            <NavItem 
                slug={"/sign-out"}
                title={"Log Out"} 
                onClick={handleClick} 
            />
        {:else}
            <NavItem 
                slug={"/login"}
                title={"Log In"} 
                onClick={handleClick} 
            />

            <NavItem 
                slug={"/register"}
                title={"Register"} 
                onClick={handleClick} 
            />
        {/if}
    </ul>
</nav>


<script>
    import NavItem from "./NavItem.svelte";
    import { loggedIn } from "$stores/userAuth";

    let isOpen = false;

    function handleClick() {
        isOpen = !isOpen;
    }
</script>