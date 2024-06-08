<script>
    import CardType from "$lib/global/CardType.svelte";
    export let uatResult;
</script>

<li id="#{uatResult.id}" 
    class="p-10 text-white rounded-lg shadow-xl
    max-w-sm w-full relative
    bg-gradient-to-tr from-yellow-500 to-amber-600
    flex flex-col justify-between gap-5">

    <CardType type={"Test Result"} />

    <span class="absolute text-sm top-0 right-0 p-4 opacity-60">
        <span class="select-none">
            ID:
        </span>
        <span>
            {uatResult.id}
        </span>
    </span>

    <div class="flex flex-col justify-between items-start">
        <span class="font-extralight text-md">Status</span>
        <h3 class="text-2xl font-bold">
            {uatResult.status}
        </h3>
    </div>

    <div class="flex flex-col justify-between items-start">
        <span class="font-extralight text-md">Notes</span>
        <p class="text-xl">
            {uatResult.notes}
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