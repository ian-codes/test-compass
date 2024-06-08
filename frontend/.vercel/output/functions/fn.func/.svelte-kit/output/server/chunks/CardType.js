import { c as create_ssr_component, e as escape } from "./ssr.js";
const CardType = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let { type } = $$props;
  if ($$props.type === void 0 && $$bindings.type && type !== void 0)
    $$bindings.type(type);
  return `<div class="absolute text-sm left-0 top-0 outline outline-1 px-2 py-1 rounded-br-xl text-opacity-70 opacity-80">${escape(type)} </div>`;
});
export {
  CardType as C
};
