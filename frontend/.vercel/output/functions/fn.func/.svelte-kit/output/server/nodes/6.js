import * as universal from '../entries/pages/projects/_slug_/_page.js';

export const index = 6;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/projects/_slug_/_page.svelte.js')).default;
export { universal };
export const universal_id = "src/routes/projects/[slug]/+page.js";
export const imports = ["_app/immutable/nodes/6.DNv-VFA8.js","_app/immutable/chunks/scheduler.Cvp1HtTB.js","_app/immutable/chunks/index.Cn1wqISX.js","_app/immutable/chunks/each.D6YF6ztN.js","_app/immutable/chunks/entry.0S8UcRWE.js","_app/immutable/chunks/CardType.DLpTMpvZ.js"];
export const stylesheets = ["_app/immutable/assets/6.Kpem8CIg.css"];
export const fonts = [];
