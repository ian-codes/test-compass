import adapter from '@sveltejs/adapter-vercel';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	kit: {
		env: {
			dir: './'
		},
		alias: {
			$models: "src/models",
			$stores: "src/stores"
		},
		adapter: adapter()
	},
	preprocess: vitePreprocess()
};

export default config;
