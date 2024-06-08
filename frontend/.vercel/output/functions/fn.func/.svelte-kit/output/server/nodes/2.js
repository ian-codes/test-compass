import * as universal from '../entries/pages/_page.js';

export const index = 2;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/_page.svelte.js')).default;
export { universal };
export const universal_id = "src/routes/+page.js";
export const imports = ["_app/immutable/nodes/2.DLMOwBcH.js","_app/immutable/chunks/scheduler.Cvp1HtTB.js","_app/immutable/chunks/index.Cn1wqISX.js","_app/immutable/chunks/each.D6YF6ztN.js","_app/immutable/chunks/ProjectCard.BG4hCIi8.js","_app/immutable/chunks/CardType.DLpTMpvZ.js"];
export const stylesheets = ["_app/immutable/assets/ProjectCard.XxAYQB8p.css"];
export const fonts = [];
