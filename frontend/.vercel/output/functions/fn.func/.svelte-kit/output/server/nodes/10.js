import * as universal from '../entries/pages/projects/_slug_/uats/_slug_/_page.js';

export const index = 10;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/projects/_slug_/uats/_slug_/_page.svelte.js')).default;
export { universal };
export const universal_id = "src/routes/projects/[slug]/uats/[slug]/+page.js";
export const imports = ["_app/immutable/nodes/10.DM4QrEAL.js","_app/immutable/chunks/scheduler.Cvp1HtTB.js","_app/immutable/chunks/index.Cn1wqISX.js"];
export const stylesheets = [];
export const fonts = [];
