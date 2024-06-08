

export const index = 4;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/organization/_page.svelte.js')).default;
export const imports = ["_app/immutable/nodes/4.DqosYn4B.js","_app/immutable/chunks/scheduler.Cvp1HtTB.js","_app/immutable/chunks/index.Cn1wqISX.js"];
export const stylesheets = [];
export const fonts = [];
