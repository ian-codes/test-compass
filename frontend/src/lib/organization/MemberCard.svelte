<script>
    export let member;
</script>

<li class="block cursor-pointer relative overflow-hidden
    rounded-full px-6 py-4 w-max text-white transition-all
    hover:scale-105 hover:text-purple-700 hover:outline outline-purple-500">

    <span class="z-10 block relative">
        {member.name}
    </span>

    <div class="absolute inset-0 hover transition-all
    bg-gradient-to-br from-purple-400 to-purple-600" />
</li>


<style>
    li:hover .hover {
        @apply opacity-0
    }
</style>