import { c as create_ssr_component, d as add_attribute, v as validate_component } from "../../../chunks/ssr.js";
import "../../../chunks/client.js";
const LoginForm = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let email;
  let password;
  email = ["", null];
  password = ["", null];
  return `<section class="dark:bg-slate-600 flex flex-col items-center gap-5 py-12 bg-slate-200"><h2 class="text-center text-xl font-mono font-extralight" data-svelte-h="svelte-37ppy6">Log In</h2> <form class="flex gap-2 flex-col items-center justify-center"><div class="${["input-container", email[1] == false ? "invalid" : ""].join(" ").trim()}"><label for="email" data-svelte-h="svelte-148vgui">Email</label> <input id="email" name="email" type="email"${add_attribute("value", email[0], 0)}></div> <div class="${["input-container", password[1] == false ? "invalid" : ""].join(" ").trim()}"><label for="password" data-svelte-h="svelte-1mvj74k">Password</label> <input id="password" name="password" minlength="8" type="password"${add_attribute("value", password[0], 0)}></div> ${``} <button type="submit" class="btn" data-svelte-h="svelte-yfbdj">Log In</button></form> <a href="/register" class="text-sm underline" data-svelte-h="svelte-1sjroar">Don&#39;t have an account? Register here.</a> </section>`;
});
const Page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `${validate_component(LoginForm, "LoginForm").$$render($$result, {}, {}, {})}`;
});
export {
  Page as default
};
