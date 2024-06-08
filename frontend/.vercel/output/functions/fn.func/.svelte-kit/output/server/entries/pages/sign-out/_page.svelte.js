import { c as create_ssr_component, e as escape } from "../../../chunks/ssr.js";
import "../../../chunks/client.js";
const Page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let statusMessage = "Signing you out...";
  return `<p>${escape(statusMessage)}</p>`;
});
export {
  Page as default
};
