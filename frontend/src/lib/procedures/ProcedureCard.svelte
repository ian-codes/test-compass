<script>
    export let procedure;
</script>

<li id="#{procedure.id}" 
    class="p-10 text-white rounded-lg shadow-xl
    max-w-sm w-full relative
    bg-gradient-to-tr from-cyan-400 to-blue-600
    flex flex-col justify-between gap-5">

    <span class="absolute text-sm top-0 right-0 p-4 opacity-60">
        <span class="select-none">
            ID:
        </span>
        <span>
            {procedure.id}
        </span>
    </span>

    <div class="flex flex-col justify-between items-start">
        <span class="font-extralight text-md">Name</span>
        <h3 class="text-2xl font-bold">
            {procedure.name}
        </h3>
    </div>

    <div class="flex flex-col justify-between items-start">
        <span class="font-extralight text-md">Description</span>
        <p class="text-xl">
            {procedure.description}
        </p>
    </div>
</li>

<style lang="postcss">
    .details-wrapper {
        @apply flex flex-row justify-between
    }
    a:hover .hover {
        @apply invert
    }
</style>