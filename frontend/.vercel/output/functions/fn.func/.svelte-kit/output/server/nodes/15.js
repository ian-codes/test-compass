import * as universal from '../entries/pages/uats/_slug_/_page.js';

export const index = 15;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/uats/_slug_/_page.svelte.js')).default;
export { universal };
export const universal_id = "src/routes/uats/[slug]/+page.js";
export const imports = ["_app/immutable/nodes/15.DM4QrEAL.js","_app/immutable/chunks/scheduler.Cvp1HtTB.js","_app/immutable/chunks/index.Cn1wqISX.js"];
export const stylesheets = [];
export const fonts = [];
