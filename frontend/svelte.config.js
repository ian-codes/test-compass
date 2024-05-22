import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	kit: {
		env: {
			dir: './'
		},
		alias: {
			$models: "src/models"
		},
		adapter: adapter(),
		paths: {
            base: process.env.NODE_ENV === 'production' ? '/test-compass' : '',
        }
	},
	preprocess: vitePreprocess()
};

export default config;
