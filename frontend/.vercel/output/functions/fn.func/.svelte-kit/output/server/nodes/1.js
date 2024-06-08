

export const index = 1;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/fallbacks/error.svelte.js')).default;
export const imports = ["_app/immutable/nodes/1.7e6d_fEq.js","_app/immutable/chunks/scheduler.Cvp1HtTB.js","_app/immutable/chunks/index.Cn1wqISX.js","_app/immutable/chunks/stores._bodFJTL.js","_app/immutable/chunks/entry.0S8UcRWE.js"];
export const stylesheets = [];
export const fonts = [];
