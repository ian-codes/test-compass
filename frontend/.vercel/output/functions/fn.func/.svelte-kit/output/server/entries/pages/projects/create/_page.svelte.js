import { c as create_ssr_component, b as add_classes, d as add_attribute, e as escape, v as validate_component } from "../../../../chunks/ssr.js";
import "../../../../chunks/client.js";
const ProjectCreate = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let project = { name: "", description: "" };
  return `<section class="dark:bg-slate-600 flex flex-col items-center gap-5 py-12 bg-slate-300"><h2 class="text-center text-xl font-mono font-extralight" data-svelte-h="svelte-2ffc18">Create New Project</h2> <form class="flex max-w-sm w-full gap-2 flex-col items-center justify-center"><div class="input-container"><label for="name" data-svelte-h="svelte-h255s">Name</label> <input id="name" name="name" type="text" minlength="3"${add_classes("".trim())}${add_attribute("value", project.name, 0)}></div> <div class="input-container"><label for="description" data-svelte-h="svelte-15l7gi">Description</label> <textarea id="description" name="description" type="text" minlength="10" class="${["resize-y h-16 max-h-32", ""].join(" ").trim()}">${escape("")}</textarea></div> ${``} <button type="submit" class="btn" data-svelte-h="svelte-1eu86fk">Create</button> <button type="reset" class="btn-secondary" data-svelte-h="svelte-10vg2k8">Discard</button></form> </section>`;
});
const Page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `${validate_component(ProjectCreate, "ProjectCreate").$$render($$result, {}, {}, {})}`;
});
export {
  Page as default
};
