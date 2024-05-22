<svelte:head>
	<title>{data?.name ?? "Loading..."} • Test Compass</title>
</svelte:head>

<script>
    import ProjectDetails from "../../../lib/projects/ProjectDetails.svelte";

    export let data;
</script>


<ProjectDetails project={data} />