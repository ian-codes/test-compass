import { c as create_ssr_component } from "../../../chunks/ssr.js";
/* empty css                                                        */
import "../../../chunks/client.js";
const Page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<section class="flex min-h-lvh flex-col gap-5">${`<p class="text-center" data-svelte-h="svelte-14hoyk4">Loading projects...</p>`}</section>`;
});
export {
  Page as default
};
