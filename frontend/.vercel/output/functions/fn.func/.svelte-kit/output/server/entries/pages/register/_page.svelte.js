import { c as create_ssr_component, d as add_attribute, v as validate_component } from "../../../chunks/ssr.js";
import "../../../chunks/client.js";
const RegistrationForm = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let first_name;
  let last_name;
  let email;
  let password;
  let isOrganizationManager;
  let organization_name;
  first_name = ["", null];
  last_name = ["", null];
  email = ["", null];
  password = ["", null];
  isOrganizationManager = false;
  organization_name = ["", null];
  return `<section class="dark:bg-slate-800 flex flex-col items-center gap-5 py-12 bg-slate-200"><h2 class="text-center text-xl font-mono font-extralight" data-svelte-h="svelte-18qf7wy">Register</h2> <form class="flex gap-2 flex-col items-center justify-center"><div class="${["input-container", first_name[1] == false ? "invalid" : ""].join(" ").trim()}"><label for="firstName" data-svelte-h="svelte-1f9975g">First Name</label> <input id="firstName" name="firstName" type="text"${add_attribute("value", first_name[0], 0)}></div> <div class="${["input-container", last_name[1] == false ? "invalid" : ""].join(" ").trim()}"><label for="lastName" data-svelte-h="svelte-yxl5sm">Last Name</label> <input id="lastName" name="lastName" type="text"${add_attribute("value", last_name[0], 0)}></div> <div class="${["input-container", email[1] == false ? "invalid" : ""].join(" ").trim()}"><label for="email" data-svelte-h="svelte-148vgui">Email</label> <input id="email" name="email" type="email"${add_attribute("value", email[0], 0)}></div> <div class="${["input-container", password[1] == false ? "invalid" : ""].join(" ").trim()}"><label for="password" data-svelte-h="svelte-1mvj74k">Password</label> <input id="password" name="password" type="password" minlength="8"${add_attribute("value", password[0], 0)}></div> <div><input id="isOrganizationManager" name="isOrganizationManager" type="checkbox"> <label for="isOrganizationManager" data-svelte-h="svelte-hpsryg">Organization Manager</label></div> ${isOrganizationManager ? `<div class="${["input-container", organization_name[1] == false ? "invalid" : ""].join(" ").trim()}"><label for="organization" data-svelte-h="svelte-13br87r">Organization Name</label> <input id="organization" name="organization" type="text"${add_attribute("value", organization_name[0], 0)}></div>` : ``} ${``} <button type="submit" class="btn" data-svelte-h="svelte-1ubow4n">Register</button></form> <a href="/login" class="text-sm underline" data-svelte-h="svelte-hf8rcn">Already registered? Log in here.</a> </section>`;
});
const Page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `${validate_component(RegistrationForm, "RegistrationForm").$$render($$result, {}, {}, {})}`;
});
export {
  Page as default
};
