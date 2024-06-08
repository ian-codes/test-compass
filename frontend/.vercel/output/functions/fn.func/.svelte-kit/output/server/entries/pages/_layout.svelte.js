import { c as create_ssr_component, d as add_attribute, e as escape, a as subscribe, f as each, v as validate_component } from "../../chunks/ssr.js";
import { w as writable } from "../../chunks/index.js";
import "../../chunks/client.js";
import { p as page } from "../../chunks/stores.js";
const NavItem = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let { title } = $$props;
  let { slug } = $$props;
  let { onClick } = $$props;
  if ($$props.title === void 0 && $$bindings.title && title !== void 0)
    $$bindings.title(title);
  if ($$props.slug === void 0 && $$bindings.slug && slug !== void 0)
    $$bindings.slug(slug);
  if ($$props.onClick === void 0 && $$bindings.onClick && onClick !== void 0)
    $$bindings.onClick(onClick);
  return `<li><a${add_attribute("title", title, 0)}${add_attribute("href", slug, 0)} class="dark:text-white hover:text-white hover:bg-slate-500 transition-all text-end block text-nowrap p-6">${escape(title)}</a> </li>`;
});
const loggedIn = writable(false);
const Nav = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let $loggedIn, $$unsubscribe_loggedIn;
  $$unsubscribe_loggedIn = subscribe(loggedIn, (value) => $loggedIn = value);
  let isOpen = false;
  function handleClick() {
    isOpen = !isOpen;
  }
  $$unsubscribe_loggedIn();
  return `<nav class="block inset-0 overflow-x-hidden max-w-full"><button class="relative dark:hover:bg-slate-600 hover:bg-slate-200 rounded-lg transition-al cursor-pointer p-1.5 z-20 w-10 h-8 flex flex-col justify-between items-center">${each({ length: 3 }, (_) => {
    return `<span class="dark:bg-white h-0.5 rounded-sm w-full bg-black"></span>`;
  })}</button> <ul class="${escape(isOpen ? "right-0 w-full" : "-right-full w-0", true) + " z-10 transition-all absolute pt-24 max-w-fulldark:bg-slate-700 outline bg-slate-200 top-0 h-min bottom-0 flex flex-col"}">${$loggedIn ? `${validate_component(NavItem, "NavItem").$$render(
    $$result,
    {
      slug: "/",
      title: "Home",
      onClick: handleClick
    },
    {},
    {}
  )} ${validate_component(NavItem, "NavItem").$$render(
    $$result,
    {
      slug: "/projects",
      title: "Projects",
      onClick: handleClick
    },
    {},
    {}
  )} ${validate_component(NavItem, "NavItem").$$render(
    $$result,
    {
      slug: "/sign-out",
      title: "Log Out",
      onClick: handleClick
    },
    {},
    {}
  )}` : `${validate_component(NavItem, "NavItem").$$render(
    $$result,
    {
      slug: "/login",
      title: "Log In",
      onClick: handleClick
    },
    {},
    {}
  )} ${validate_component(NavItem, "NavItem").$$render(
    $$result,
    {
      slug: "/register",
      title: "Register",
      onClick: handleClick
    },
    {},
    {}
  )}`}</ul> </nav>`;
});
const darkModeImg = "/darkmode.svg";
const ThemeSwitcher = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<button title="${"toggle " + escape("dark mode", true)}" class="hover:outline dark:hover:outline-black outline-slate-400 hover:scale-105 transition-all z-20 relative rounded-full dark:invert bg-center bg-contain bg-no-repeat w-8 h-8" style="${"background-image: url('" + escape(darkModeImg, true) + "')"}"></button>`;
});
const css = {
  code: "@keyframes svelte-8epbue-spinning{0%{transform:rotate(0)}100%{transform:rotate(360)}}",
  map: `{"version":3,"file":"Header.svelte","sources":["Header.svelte"],"sourcesContent":["<script>\\n    import Nav from \\"./Nav.svelte\\";\\n    import ThemeSwitcher from \\"./ThemeSwitcher.svelte\\";\\n<\/script>\\n\\n\\n<header class=\\"shadow-md shadow-slate-200 py-4 p-1 bg-slate-100 dark:bg-slate-800 flex flex-row items-center justify-between gap-2\\">\\n    <a href=\\"/\\" title=\\"home\\" class=\\"z-50 relative cursor-pointer p-2 rounded-lg hover:bg-white hover:bg-opacity-10 transition-all\\n    flex flex-row gap-2 justify-start items-center\\">\\n        <div class=\\"absolute inset-0\\" />\\n        <span class=\\"drop-shadow-lg rounded-full shadow-slate-200 block bg-contain bg-center bg-no-repeat w-10 h-10\\" style=\\"background-image: url('/logo.png')\\" />\\n        <span class=\\"dark:text-white tracking-widest uppercase\\">Test Compass</span>\\n    </a>\\n    \\n    <div class=\\"flex flex-row items-cente p-4 gap-5\\">\\n        <ThemeSwitcher />\\n        <Nav />\\n    </div>\\n</header>\\n\\n<style>\\n    @keyframes spinning {\\n        0% {transform: rotate(0)}\\n        100% {transform: rotate(360)}\\n    }\\n</style>"],"names":[],"mappings":"AAqBI,WAAW,sBAAS,CAChB,EAAG,CAAC,SAAS,CAAE,OAAO,CAAC,CAAC,CACxB,IAAK,CAAC,SAAS,CAAE,OAAO,GAAG,CAAC,CAChC"}`
};
const Header = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  $$result.css.add(css);
  return `<header class="shadow-md shadow-slate-200 py-4 p-1 bg-slate-100 dark:bg-slate-800 flex flex-row items-center justify-between gap-2"><a href="/" title="home" class="z-50 relative cursor-pointer p-2 rounded-lg hover:bg-white hover:bg-opacity-10 transition-all flex flex-row gap-2 justify-start items-center" data-svelte-h="svelte-hjb9nw"><div class="absolute inset-0"></div> <span class="drop-shadow-lg rounded-full shadow-slate-200 block bg-contain bg-center bg-no-repeat w-10 h-10" style="background-image: url('/logo.png')"></span> <span class="dark:text-white tracking-widest uppercase">Test Compass</span></a> <div class="flex flex-row items-cente p-4 gap-5">${validate_component(ThemeSwitcher, "ThemeSwitcher").$$render($$result, {}, {}, {})} ${validate_component(Nav, "Nav").$$render($$result, {}, {}, {})}</div> </header>`;
});
const Layout = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let $$unsubscribe_page;
  $$unsubscribe_page = subscribe(page, (value) => value);
  $$unsubscribe_page();
  return `<div class="min-h-dvh overflow-x-hidden relative"><div class="inset-0 absolute hidden bg-gradient-to-r from-slate-500 via-transparent to-slate-500"></div> ${validate_component(Header, "Header").$$render($$result, {}, {}, {})} <main class="dark:text-white dark:bg-slate-800 h-full bg-slate-100 p-2 py-8 min-h-lvh flex flex-col items-center gap-10">${slots.default ? slots.default({}) : ``}</main></div>`;
});
export {
  Layout as default
};
