

export const index = 5;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/projects/_page.svelte.js')).default;
export const imports = ["_app/immutable/nodes/5.C4xMd6eU.js","_app/immutable/chunks/scheduler.Cvp1HtTB.js","_app/immutable/chunks/index.Cn1wqISX.js","_app/immutable/chunks/each.D6YF6ztN.js","_app/immutable/chunks/ProjectCard.BG4hCIi8.js","_app/immutable/chunks/CardType.DLpTMpvZ.js","_app/immutable/chunks/entry.0S8UcRWE.js"];
export const stylesheets = ["_app/immutable/assets/ProjectCard.XxAYQB8p.css"];
export const fonts = [];
