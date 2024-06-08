<li>
    <a on:click={onClick}
    title="{title}" href="{slug}"
    class=" dark:text-white hover:text-white hover:bg-slate-500
    transition-all text-end block text-nowrap p-6">
        {title}
    </a>
</li>

<script>
    export let title;
    export let slug;
    export let onClick;
</script>