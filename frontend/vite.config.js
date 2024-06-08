import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

const BASE_URL = process.env.NODE_ENV === 'production' 
	? 'https://test-compass.refugium-romontberg.ch/' 
	: 'http://127.0.0.1:8000/';

export default defineConfig({
	plugins: [sveltekit()],
	define: {
		'import.meta.env.VITE_BACKEND_URL': JSON.stringify(BASE_URL)
	}
});