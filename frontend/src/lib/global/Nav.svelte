<nav class="block inset-0 overflow-x-hidden max-w-full">
    <button on:click={handleClick} class="relative dark:hover:bg-slate-600 hover:bg-slate-200 rounded-lg 
        transition-al cursor-pointer p-1.5 z-20 w-10 h-8 flex flex-col justify-between items-center">
        {#each {length: 3} as _}
            <span class="dark:bg-white h-0.5 rounded-sm w-full bg-black" />
        {/each}
    </button>
    <ul class="{(isOpen ? "right-0 w-full" : "-right-full w-0")} z-10 transition-all absolute pt-24 max-w-full
 dark:bg-slate-700 outline bg-slate-200 top-0 h-min bottom-0 flex flex-col">
        {#each menuItems as item}
            <li class="{($page.path == item.title ? "current" : "")}">
                <a on:click={handleClick}
                title="{item.title}" href="{item.slug}"
                class=" dark:text-white hover:text-white hover:bg-slate-500
                transition-all text-end block text-nowrap p-6">
                    {item.title}
                </a>
            </li>
        {/each}
    </ul>
</nav>


<script>
    import { page } from "$app/stores";

    let menuItems = [
        {
            title: "Home",
            slug: "/"
        },
        {
            title: "Projects",
            slug: "/projects"
        },
        {
            title: "Procedures",
            slug: "/procedures"
        },
        {
            title: "UATs",
            slug: "/uats"
        },
        {
            title: "Sign Out",
            slug: "sign-out"
        }
    ];

    let isOpen = false;

    function handleClick() {
        isOpen = !isOpen;
    }
</script>


<style>
    .current {
        background: red;
    }
</style>