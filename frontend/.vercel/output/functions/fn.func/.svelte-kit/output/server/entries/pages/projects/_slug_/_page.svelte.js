import { c as create_ssr_component, e as escape, v as validate_component, f as each } from "../../../../chunks/ssr.js";
import "../../../../chunks/client.js";
import { C as CardType } from "../../../../chunks/CardType.js";
const css$4 = {
  code: "a.svelte-l5b837:hover .hover.svelte-l5b837{--tw-invert:invert(100%);filter:var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow)\n}",
  map: `{"version":3,"file":"UatCard.svelte","sources":["UatCard.svelte"],"sourcesContent":["<script>\\n    import CardType from \\"$lib/global/CardType.svelte\\";\\n    export let uat;\\n<\/script>\\n\\n<li id=\\"#{uat.id}\\" \\n    class=\\"p-10 text-white shadow-xl outline\\n    max-w-sm w-full relative overflow-hidden rounded-lg\\n    bg-gradient-to-tr from-yellow-500 to-amber-600\\n    flex flex-col justify-between gap-5\\">\\n\\n    <CardType type={\\"Test\\"} />\\n\\n    <span class=\\"absolute text-sm top-0 right-0 p-4 opacity-60\\">\\n        <span class=\\"select-none\\">\\n            ID:\\n        </span>\\n        <span>\\n            {uat.id}\\n        </span>\\n    </span>\\n\\n    <div class=\\"flex flex-col justify-between items-start\\">\\n        <span class=\\"font-extralight text-md\\">Name</span>\\n        <h3 class=\\"text-2xl font-bold\\">\\n            {uat.name}\\n        </h3>\\n    </div>\\n\\n    <div class=\\"flex flex-col justify-between items-start\\">\\n        <span class=\\"font-extralight text-md\\">Description</span>\\n        <p class=\\"text-xl\\">\\n            {uat.description}\\n        </p>\\n    </div>\\n\\n    <div class=\\"flex flex-col justify-between items-start\\">\\n        <span class=\\"font-extralight text-md\\">Preconditions</span>\\n        <p class=\\"text-xl\\">\\n            {uat.pre_conditions}\\n        </p>\\n    </div>\\n\\n    <div class=\\"flex flex-col justify-between items-start\\">\\n        <span class=\\"font-extralight text-md\\">Steps</span>\\n        <p class=\\"text-xl\\">\\n            {uat.steps}\\n        </p>\\n    </div>\\n\\n    <div class=\\"flex flex-col justify-between items-start\\">\\n        <span class=\\"font-extralight text-md\\">Expected Result</span>\\n        <p class=\\"text-xl\\">\\n            {uat.expected_result}\\n        </p>\\n    </div>\\n\\n    <div class=\\"flex flex-row gap-4\\">\\n        <a href=\\"/projects/uats/{uat.id}\\"\\n        class=\\"hover:scale-105\\n        flex flex-row items-center gap-2\\n        btn-secondary hover:bg-white dark:text-white dark:hover:text-black\\n        hover:text-black text-white \\n        transition-all\\">\\n\\n        <span style=\\"background-image: url('/open.svg');\\" \\n            class=\\"hover transition-all block icon w-5 h-5\\" />\\n            New Result\\n        </a>\\n        <a href=\\"/projects/uats/{uat.id}\\"\\n            class=\\"hover:scale-105\\n            flex flex-row items-center gap-2\\n            btn-secondary hover:bg-white dark:text-white dark:hover:text-black\\n            hover:text-black text-white \\n            transition-all\\">\\n            \\n            <span style=\\"background-image: url('/open.svg');\\" \\n                class=\\"hover transition-all block icon w-5 h-5\\" />\\n            Details\\n        </a>\\n    </div>\\n</li>\\n\\n<style lang=\\"postcss\\">\\n    .details-wrapper {\\n    display: flex;\\n    flex-direction: row;\\n    justify-content: space-between\\n}\\n    a:hover .hover {\\n    --tw-invert: invert(100%);\\n    filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow)\\n}\\n</style>"],"names":[],"mappings":"AAyFI,eAAC,MAAM,CAAC,oBAAO,CACf,WAAW,CAAE,YAAY,CACzB,MAAM,CAAE,IAAI,SAAS,CAAC,CAAC,IAAI,eAAe,CAAC,CAAC,IAAI,aAAa,CAAC,CAAC,IAAI,cAAc,CAAC,CAAC,IAAI,eAAe,CAAC,CAAC,IAAI,WAAW,CAAC,CAAC,IAAI,aAAa,CAAC,CAAC,IAAI,UAAU,CAAC,CAAC,IAAI,gBAAgB,CAAC;AACrL"}`
};
const UatCard = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let { uat } = $$props;
  if ($$props.uat === void 0 && $$bindings.uat && uat !== void 0)
    $$bindings.uat(uat);
  $$result.css.add(css$4);
  return `<li id="${"#" + escape(uat.id, true)}" class="p-10 text-white shadow-xl outline max-w-sm w-full relative overflow-hidden rounded-lg bg-gradient-to-tr from-yellow-500 to-amber-600 flex flex-col justify-between gap-5">${validate_component(CardType, "CardType").$$render($$result, { type: "Test" }, {}, {})} <span class="absolute text-sm top-0 right-0 p-4 opacity-60"><span class="select-none" data-svelte-h="svelte-fr4vsp">ID:</span> <span>${escape(uat.id)}</span></span> <div class="flex flex-col justify-between items-start"><span class="font-extralight text-md" data-svelte-h="svelte-g2pwqb">Name</span> <h3 class="text-2xl font-bold">${escape(uat.name)}</h3></div> <div class="flex flex-col justify-between items-start"><span class="font-extralight text-md" data-svelte-h="svelte-1ybgxg6">Description</span> <p class="text-xl">${escape(uat.description)}</p></div> <div class="flex flex-col justify-between items-start"><span class="font-extralight text-md" data-svelte-h="svelte-1sxq939">Preconditions</span> <p class="text-xl">${escape(uat.pre_conditions)}</p></div> <div class="flex flex-col justify-between items-start"><span class="font-extralight text-md" data-svelte-h="svelte-1k2vwkl">Steps</span> <p class="text-xl">${escape(uat.steps)}</p></div> <div class="flex flex-col justify-between items-start"><span class="font-extralight text-md" data-svelte-h="svelte-1vu7udv">Expected Result</span> <p class="text-xl">${escape(uat.expected_result)}</p></div> <div class="flex flex-row gap-4"><a href="${"/projects/uats/" + escape(uat.id, true)}" class="hover:scale-105 flex flex-row items-center gap-2 btn-secondary hover:bg-white dark:text-white dark:hover:text-black hover:text-black text-white transition-all svelte-l5b837"><span style="background-image: url('/open.svg');" class="hover transition-all block icon w-5 h-5 svelte-l5b837"></span>
            New Result</a> <a href="${"/projects/uats/" + escape(uat.id, true)}" class="hover:scale-105 flex flex-row items-center gap-2 btn-secondary hover:bg-white dark:text-white dark:hover:text-black hover:text-black text-white transition-all svelte-l5b837"><span style="background-image: url('/open.svg');" class="hover transition-all block icon w-5 h-5 svelte-l5b837"></span>
            Details</a></div> </li>`;
});
const css$3 = {
  code: ".visible.svelte-p4kgaq{display:flex\n}",
  map: '{"version":3,"file":"UatList.svelte","sources":["UatList.svelte"],"sourcesContent":["<section id=\\"user-acceptance-tests\\"\\n    class=\\"hidden min-h-lvh flex-col gap-5\\"\\n    class:visible={isVisible}>\\n\\n    <div class=\\"pb-8 flex flex-row gap-5 justify-between items-center\\">\\n        <h2>User Acceptance Tests • {uats.length}</h2>\\n\\n        <button on:click={() => goto(`${slug}/new-user-acceptance-test`)}\\n            class=\\"btn !m-0 !w-max inline-block\\">\\n            Add New\\n        </button>\\n    </div>\\n\\n    <ol class=\\"flex flex-wrap items-center justify-center gap-4\\">\\n        {#each uats as uat}\\n            <UatCard uat={uat} />\\n        {/each}\\n    </ol>\\n</section>\\n\\n<script>\\n    import { goto } from \\"$app/navigation.js\\";\\n    import UatCard from \\"./UatCard.svelte\\";\\n    export let uats;\\n    export let activeTab;\\n    export let slug;\\n\\n    $: isVisible = activeTab == \\"uats\\";\\n<\/script>\\n\\n<style lang=\\"postcss\\">\\n    .visible {\\n    display: flex\\n}\\n</style>"],"names":[],"mappings":"AA+BI,sBAAS,CACT,OAAO,CAAE,IAAI;AACjB"}'
};
const UatList = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let isVisible;
  let { uats } = $$props;
  let { activeTab } = $$props;
  let { slug } = $$props;
  if ($$props.uats === void 0 && $$bindings.uats && uats !== void 0)
    $$bindings.uats(uats);
  if ($$props.activeTab === void 0 && $$bindings.activeTab && activeTab !== void 0)
    $$bindings.activeTab(activeTab);
  if ($$props.slug === void 0 && $$bindings.slug && slug !== void 0)
    $$bindings.slug(slug);
  $$result.css.add(css$3);
  isVisible = activeTab == "uats";
  return `<section id="user-acceptance-tests" class="${["hidden min-h-lvh flex-col gap-5 svelte-p4kgaq", isVisible ? "visible" : ""].join(" ").trim()}"><div class="pb-8 flex flex-row gap-5 justify-between items-center"><h2>User Acceptance Tests • ${escape(uats.length)}</h2> <button class="btn !m-0 !w-max inline-block" data-svelte-h="svelte-1mlmkn2">Add New</button></div> <ol class="flex flex-wrap items-center justify-center gap-4">${each(uats, (uat) => {
    return `${validate_component(UatCard, "UatCard").$$render($$result, { uat }, {}, {})}`;
  })}</ol> </section>`;
});
const css$2 = {
  code: "a.svelte-l5b837:hover .hover.svelte-l5b837{--tw-invert:invert(100%);filter:var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow)\n}",
  map: `{"version":3,"file":"ProcedureCard.svelte","sources":["ProcedureCard.svelte"],"sourcesContent":["<li id=\\"#{procedure.id}\\" \\n    class=\\"p-10 text-white rounded-lg shadow-xl\\n    max-w-sm w-full relative overflow-hidden outline\\n    bg-gradient-to-tr from-purple-400 to-violet-600\\n    flex flex-col justify-between gap-5\\">\\n\\n    <CardType type={\\"Procedure\\"} />\\n\\n    <span class=\\"absolute text-sm top-0 right-0 p-4 opacity-60\\">\\n        <span class=\\"select-none\\">\\n            ID:\\n        </span>\\n        <span>\\n            {procedure.id}\\n        </span>\\n    </span>\\n\\n    <div class=\\"flex flex-col justify-between items-start\\">\\n        <span class=\\"font-extralight text-md\\">Name</span>\\n        <h3 class=\\"text-2xl font-bold\\">\\n            {procedure.name}\\n        </h3>\\n    </div>\\n\\n    <div class=\\"flex flex-col justify-between items-start\\">\\n        <span class=\\"font-extralight text-md\\">Description</span>\\n        <p class=\\"text-xl\\">\\n            {procedure.description}\\n        </p>\\n    </div>\\n\\n    <a href=\\"/projects/procedures/{procedure.id}\\"\\n        class=\\"hover:scale-105\\n        flex flex-row items-center gap-2\\n        btn-secondary hover:bg-white dark:text-white dark:hover:text-black\\n        hover:text-black text-white \\n        transition-all\\">\\n        \\n        <span style=\\"background-image: url('/open.svg');\\" \\n            class=\\"hover transition-all block icon w-5 h-5\\" />\\n        \\n        Show Details\\n    </a>\\n</li>\\n\\n\\n<script>\\n    import CardType from \\"$lib/global/CardType.svelte\\";\\n    export let procedure;\\n<\/script>\\n\\n\\n<style lang=\\"postcss\\">\\n    .details-wrapper {\\n    display: flex;\\n    flex-direction: row;\\n    justify-content: space-between\\n}\\n    a:hover .hover {\\n    --tw-invert: invert(100%);\\n    filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow)\\n}\\n</style>"],"names":[],"mappings":"AA0DI,eAAC,MAAM,CAAC,oBAAO,CACf,WAAW,CAAE,YAAY,CACzB,MAAM,CAAE,IAAI,SAAS,CAAC,CAAC,IAAI,eAAe,CAAC,CAAC,IAAI,aAAa,CAAC,CAAC,IAAI,cAAc,CAAC,CAAC,IAAI,eAAe,CAAC,CAAC,IAAI,WAAW,CAAC,CAAC,IAAI,aAAa,CAAC,CAAC,IAAI,UAAU,CAAC,CAAC,IAAI,gBAAgB,CAAC;AACrL"}`
};
const ProcedureCard = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let { procedure } = $$props;
  if ($$props.procedure === void 0 && $$bindings.procedure && procedure !== void 0)
    $$bindings.procedure(procedure);
  $$result.css.add(css$2);
  return `<li id="${"#" + escape(procedure.id, true)}" class="p-10 text-white rounded-lg shadow-xl max-w-sm w-full relative overflow-hidden outline bg-gradient-to-tr from-purple-400 to-violet-600 flex flex-col justify-between gap-5">${validate_component(CardType, "CardType").$$render($$result, { type: "Procedure" }, {}, {})} <span class="absolute text-sm top-0 right-0 p-4 opacity-60"><span class="select-none" data-svelte-h="svelte-fr4vsp">ID:</span> <span>${escape(procedure.id)}</span></span> <div class="flex flex-col justify-between items-start"><span class="font-extralight text-md" data-svelte-h="svelte-g2pwqb">Name</span> <h3 class="text-2xl font-bold">${escape(procedure.name)}</h3></div> <div class="flex flex-col justify-between items-start"><span class="font-extralight text-md" data-svelte-h="svelte-1ybgxg6">Description</span> <p class="text-xl">${escape(procedure.description)}</p></div> <a href="${"/projects/procedures/" + escape(procedure.id, true)}" class="hover:scale-105 flex flex-row items-center gap-2 btn-secondary hover:bg-white dark:text-white dark:hover:text-black hover:text-black text-white transition-all svelte-l5b837"><span style="background-image: url('/open.svg');" class="hover transition-all block icon w-5 h-5 svelte-l5b837"></span>
        
        Show Details</a> </li>`;
});
const css$1 = {
  code: ".visible.svelte-p4kgaq{display:flex\n}",
  map: '{"version":3,"file":"ProcedureList.svelte","sources":["ProcedureList.svelte"],"sourcesContent":["<section id=\\"procedures\\"\\n    class=\\"hidden min-h-lvh flex-col gap-5\\"\\n    class:visible={isVisible}>\\n\\n    <div class=\\"pb-8 flex flex-row gap-5 justify-between items-center\\">\\n        <h2>Test Procedures • {procedures.length}</h2>\\n\\n        <button on:click={() => goto(`${slug}/new-test-procedure`)}\\n            class=\\"btn !m-0 !w-max inline-block\\">\\n            Add New\\n        </button>\\n    </div>\\n\\n    <ol class=\\"flex flex-wrap items-center justify-center gap-4\\">\\n        {#each procedures as procedure}\\n            <ProcedureCard procedure={procedure} />\\n        {/each}\\n    </ol>\\n</section>\\n\\n<script>\\n    import { goto } from \\"$app/navigation.js\\";\\n    import ProcedureCard from \\"./ProcedureCard.svelte\\";\\n    export let procedures;\\n    export let activeTab;\\n    export let slug;\\n\\n    $: isVisible = activeTab == \\"procedures\\";\\n<\/script>\\n\\n<style lang=\\"postcss\\">\\n    .visible {\\n    display: flex\\n}\\n</style>"],"names":[],"mappings":"AA+BI,sBAAS,CACT,OAAO,CAAE,IAAI;AACjB"}'
};
const ProcedureList = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let isVisible;
  let { procedures } = $$props;
  let { activeTab } = $$props;
  let { slug } = $$props;
  if ($$props.procedures === void 0 && $$bindings.procedures && procedures !== void 0)
    $$bindings.procedures(procedures);
  if ($$props.activeTab === void 0 && $$bindings.activeTab && activeTab !== void 0)
    $$bindings.activeTab(activeTab);
  if ($$props.slug === void 0 && $$bindings.slug && slug !== void 0)
    $$bindings.slug(slug);
  $$result.css.add(css$1);
  isVisible = activeTab == "procedures";
  return `<section id="procedures" class="${["hidden min-h-lvh flex-col gap-5 svelte-p4kgaq", isVisible ? "visible" : ""].join(" ").trim()}"><div class="pb-8 flex flex-row gap-5 justify-between items-center"><h2>Test Procedures • ${escape(procedures.length)}</h2> <button class="btn !m-0 !w-max inline-block" data-svelte-h="svelte-aw8i9a">Add New</button></div> <ol class="flex flex-wrap items-center justify-center gap-4">${each(procedures, (procedure) => {
    return `${validate_component(ProcedureCard, "ProcedureCard").$$render($$result, { procedure }, {}, {})}`;
  })}</ol> </section>`;
});
const css = {
  code: ".activeTab.svelte-17izrdg{--tw-bg-opacity:1;background-color:rgb(226 232 240 / var(--tw-bg-opacity));outline-style:solid;outline-width:1px\n}.activeTab.svelte-17izrdg:is(.dark *){--tw-bg-opacity:1;background-color:rgb(51 65 85 / var(--tw-bg-opacity))\n}.tab.svelte-17izrdg{border-radius:0.375rem;padding-left:1rem;padding-right:1rem;padding-top:0.5rem;padding-bottom:0.5rem\n}",
  map: '{"version":3,"file":"+page.svelte","sources":["+page.svelte"],"sourcesContent":["{#if isLoading}\\n    <h1 class=\\"text-2xl\\">Loading...</h1>\\n{:else}\\n    <div class=\\"flex flex-col justify-center items-center \\n        gap-4 w-full m-auto\\"\\n        class:visible={!isLoading}>\\n\\n        <section class=\\"flex flex-col gap-4 relative\\">\\n            <h1 class=\\"text-3xl\\">\\n                {project.name}\\n            </h1>\\n            <span class=\\"absolute text-sm top-0 right-0 p-4 opacity-60\\">\\n                <span class=\\"select-none\\">\\n                    ID:\\n                </span>\\n                <span>\\n                    {project.id}\\n                </span>\\n            </span>\\n            <p>\\n                {project.description}\\n            </p>\\n\\n            <div class=\\"flex flex-row justify-center\\">\\n                <button on:click={() => activeTab = \\"procedures\\"}\\n                    class=\\"tab\\"\\n                    class:activeTab={activeTab == \\"procedures\\"}>\\n                    Test Procedures\\n                </button>\\n                <button on:click={() => activeTab = \\"uats\\"}\\n                    class=\\"tab\\"\\n                    class:activeTab={activeTab == \\"uats\\"}>\\n                    User Acceptance Tests\\n                </button>\\n            </div>\\n        </section>\\n\\n        <ProcedureList \\n            slug={data.slug} \\n            procedures={procedures} \\n            bind:activeTab={activeTab} />\\n\\n        <UatList \\n            slug={data.slug} \\n            uats={uats} \\n            bind:activeTab={activeTab} />\\n    </div>\\n{/if}\\n\\n\\n\\n<script>\\n    import UatList from \\"$lib/uats/UatList.svelte\\";\\n    import ProcedureList from \\"$lib/procedures/ProcedureList.svelte\\";\\n\\n    export let data;\\n    let project = data.project;\\n    let procedures = data.procedures;\\n    let uats = data.uats;\\n\\n    let activeTab = \\"procedures\\";\\n\\n    $: isLoading = !project && !procedures && !uats\\n<\/script>\\n\\n\\n<style lang=\\"postcss\\">\\n    .activeTab {\\n    --tw-bg-opacity: 1;\\n    background-color: rgb(226 232 240 / var(--tw-bg-opacity));\\n    outline-style: solid;\\n    outline-width: 1px\\n}\\n.activeTab:is(.dark *) {\\n    --tw-bg-opacity: 1;\\n    background-color: rgb(51 65 85 / var(--tw-bg-opacity))\\n}\\n    .tab {\\n    border-radius: 0.375rem;\\n    padding-left: 1rem;\\n    padding-right: 1rem;\\n    padding-top: 0.5rem;\\n    padding-bottom: 0.5rem\\n}\\n</style>"],"names":[],"mappings":"AAmEI,yBAAW,CACX,eAAe,CAAE,CAAC,CAClB,gBAAgB,CAAE,IAAI,GAAG,CAAC,GAAG,CAAC,GAAG,CAAC,CAAC,CAAC,IAAI,eAAe,CAAC,CAAC,CACzD,aAAa,CAAE,KAAK,CACpB,aAAa,CAAE,GAAG;AACtB,CACA,yBAAU,IAAI,KAAK,CAAC,CAAC,CAAE,CACnB,eAAe,CAAE,CAAC,CAClB,gBAAgB,CAAE,IAAI,EAAE,CAAC,EAAE,CAAC,EAAE,CAAC,CAAC,CAAC,IAAI,eAAe,CAAC,CAAC;AAC1D,CACI,mBAAK,CACL,aAAa,CAAE,QAAQ,CACvB,YAAY,CAAE,IAAI,CAClB,aAAa,CAAE,IAAI,CACnB,WAAW,CAAE,MAAM,CACnB,cAAc,CAAE,MAAM;AAC1B"}'
};
const Page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let isLoading;
  let { data } = $$props;
  let project = data.project;
  let procedures = data.procedures;
  let uats = data.uats;
  let activeTab = "procedures";
  if ($$props.data === void 0 && $$bindings.data && data !== void 0)
    $$bindings.data(data);
  $$result.css.add(css);
  let $$settled;
  let $$rendered;
  let previous_head = $$result.head;
  do {
    $$settled = true;
    $$result.head = previous_head;
    isLoading = !project && !procedures && !uats;
    $$rendered = `${isLoading ? `<h1 class="text-2xl" data-svelte-h="svelte-wq0b6b">Loading...</h1>` : `<div class="${[
      "flex flex-col justify-center items-center gap-4 w-full m-auto",
      !isLoading ? "visible" : ""
    ].join(" ").trim()}"><section class="flex flex-col gap-4 relative"><h1 class="text-3xl">${escape(project.name)}</h1> <span class="absolute text-sm top-0 right-0 p-4 opacity-60"><span class="select-none" data-svelte-h="svelte-op1urd">ID:</span> <span>${escape(project.id)}</span></span> <p>${escape(project.description)}</p> <div class="flex flex-row justify-center"><button class="${["tab svelte-17izrdg", activeTab == "procedures" ? "activeTab" : ""].join(" ").trim()}" data-svelte-h="svelte-c4zn19">Test Procedures</button> <button class="${["tab svelte-17izrdg", activeTab == "uats" ? "activeTab" : ""].join(" ").trim()}" data-svelte-h="svelte-137im0s">User Acceptance Tests</button></div></section> ${validate_component(ProcedureList, "ProcedureList").$$render(
      $$result,
      { slug: data.slug, procedures, activeTab },
      {
        activeTab: ($$value) => {
          activeTab = $$value;
          $$settled = false;
        }
      },
      {}
    )} ${validate_component(UatList, "UatList").$$render(
      $$result,
      { slug: data.slug, uats, activeTab },
      {
        activeTab: ($$value) => {
          activeTab = $$value;
          $$settled = false;
        }
      },
      {}
    )}</div>`}`;
  } while (!$$settled);
  return $$rendered;
});
export {
  Page as default
};
