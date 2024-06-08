import { c as create_ssr_component, d as add_attribute, e as escape, v as validate_component, f as each } from "../../chunks/ssr.js";
import { C as CardType } from "../../chunks/CardType.js";
/* empty css                                                     */
const InviteComponent = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let email = "";
  return `<form class="flex flex-row items-center gap-2"><div class="${["input-container !w-min", email[1] == false ? "invalid" : ""].join(" ").trim()}"><input id="invitee_email" name="invitee_email" type="email" placeholder="Invitee's Email" class="${["shadow-md", ""].join(" ").trim()}"${add_attribute("value", email, 0)}></div> <button type="submit" class="btn !m-0 !w-max inline-block" data-svelte-h="svelte-230ayk">Invite</button> ${``} </form>`;
});
const css = {
  code: "a.svelte-l5b837:hover .hover.svelte-l5b837{--tw-invert:invert(100%);filter:var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow)\n}",
  map: `{"version":3,"file":"ProjectCard.svelte","sources":["ProjectCard.svelte"],"sourcesContent":["<li id=\\"#{project.id}\\" \\n    class=\\"p-10 text-white rounded-lg shadow-xl\\n    max-w-sm w-full relative outline\\n    bg-gradient-to-br from-cyan-500 to-blue-600 overflow-hidden\\n    flex flex-col justify-between gap-5\\">\\n\\n    <CardType type={\\"Project\\"} />\\n\\n    <span class=\\"absolute text-sm top-0 right-0 p-4 opacity-60\\">\\n        <span class=\\"select-none\\">\\n            ID:\\n        </span>\\n        <span>\\n            {project.id}\\n        </span>\\n    </span>\\n\\n    <div class=\\"flex flex-col justify-between items-start\\">\\n        <span class=\\"font-extralight text-md\\">Name</span>\\n        <h3 class=\\"text-2xl font-bold\\">\\n            {project.name}\\n        </h3>\\n    </div>\\n\\n    <div class=\\"flex flex-col justify-between items-start\\">\\n        <span class=\\"font-extralight text-md\\">Description</span>\\n        <p class=\\"text-xl\\">\\n            {project.description}\\n        </p>\\n    </div>\\n\\n    <a href=\\"/projects/{project.id}\\"\\n        class=\\"hover:scale-105\\n        flex flex-row items-center gap-2\\n        btn-secondary hover:bg-white dark:text-white dark:hover:text-black\\n        hover:text-black text-white \\n        transition-all\\">\\n        \\n        <span style=\\"background-image: url('/open.svg');\\" \\n            class=\\"hover transition-all block icon w-5 h-5\\" />\\n        \\n        Go to Project\\n    </a>\\n</li>\\n\\n\\n<script>\\n    import CardType from \\"$lib/global/CardType.svelte\\";\\n    export let project;\\n<\/script>\\n\\n\\n<style lang=\\"postcss\\">\\n    .details-wrapper {\\n    display: flex;\\n    flex-direction: row;\\n    justify-content: space-between\\n}\\n    a:hover .hover {\\n    --tw-invert: invert(100%);\\n    filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow)\\n}\\n</style>"],"names":[],"mappings":"AA0DI,eAAC,MAAM,CAAC,oBAAO,CACf,WAAW,CAAE,YAAY,CACzB,MAAM,CAAE,IAAI,SAAS,CAAC,CAAC,IAAI,eAAe,CAAC,CAAC,IAAI,aAAa,CAAC,CAAC,IAAI,cAAc,CAAC,CAAC,IAAI,eAAe,CAAC,CAAC,IAAI,WAAW,CAAC,CAAC,IAAI,aAAa,CAAC,CAAC,IAAI,UAAU,CAAC,CAAC,IAAI,gBAAgB,CAAC;AACrL"}`
};
const ProjectCard = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let { project } = $$props;
  if ($$props.project === void 0 && $$bindings.project && project !== void 0)
    $$bindings.project(project);
  $$result.css.add(css);
  return `<li id="${"#" + escape(project.id, true)}" class="p-10 text-white rounded-lg shadow-xl max-w-sm w-full relative outline bg-gradient-to-br from-cyan-500 to-blue-600 overflow-hidden flex flex-col justify-between gap-5">${validate_component(CardType, "CardType").$$render($$result, { type: "Project" }, {}, {})} <span class="absolute text-sm top-0 right-0 p-4 opacity-60"><span class="select-none" data-svelte-h="svelte-fr4vsp">ID:</span> <span>${escape(project.id)}</span></span> <div class="flex flex-col justify-between items-start"><span class="font-extralight text-md" data-svelte-h="svelte-g2pwqb">Name</span> <h3 class="text-2xl font-bold">${escape(project.name)}</h3></div> <div class="flex flex-col justify-between items-start"><span class="font-extralight text-md" data-svelte-h="svelte-1ybgxg6">Description</span> <p class="text-xl">${escape(project.description)}</p></div> <a href="${"/projects/" + escape(project.id, true)}" class="hover:scale-105 flex flex-row items-center gap-2 btn-secondary hover:bg-white dark:text-white dark:hover:text-black hover:text-black text-white transition-all svelte-l5b837"><span style="background-image: url('/open.svg');" class="hover transition-all block icon w-5 h-5 svelte-l5b837"></span>
        
        Go to Project</a> </li>`;
});
const Page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let isLoading;
  let { data } = $$props;
  let user = data.user;
  let projects = data.projects;
  let organization = data.organization;
  if ($$props.data === void 0 && $$bindings.data && data !== void 0)
    $$bindings.data(data);
  isLoading = !user && !projects && !organization;
  return `${isLoading ? `<h1 class="text-2xl" data-svelte-h="svelte-wq0b6b">Loading...</h1>` : `<div class="${[
    "flex flex-col justify-center items-center gap-4 w-full m-auto",
    !isLoading ? "visible" : ""
  ].join(" ").trim()}"><h1 class="text-3xl">Hey, ${escape(user.first_name)}.</h1> <section class="flex flex-col gap-4"><h2>Organization • ${escape(organization?.name ?? "Loading...")}</h2> ${validate_component(InviteComponent, "InviteComponent").$$render($$result, {}, {}, {})} </section>  <section id="projects" class="flex flex-col gap-5"><h2 class="m-0">Projects • ${escape(projects.length)}</h2> <ol class="flex flex-wrap items-center justify-center gap-4">${each(projects, (project) => {
    return `${validate_component(ProjectCard, "ProjectCard").$$render($$result, { project }, {}, {})}`;
  })}</ol></section></div>`}`;
});
export {
  Page as default
};
