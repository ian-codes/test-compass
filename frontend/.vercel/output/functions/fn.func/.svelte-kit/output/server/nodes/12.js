

export const index = 12;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/register/_page.svelte.js')).default;
export const imports = ["_app/immutable/nodes/12.d8USs0yi.js","_app/immutable/chunks/scheduler.Cvp1HtTB.js","_app/immutable/chunks/index.Cn1wqISX.js","_app/immutable/chunks/entry.0S8UcRWE.js"];
export const stylesheets = [];
export const fonts = [];
