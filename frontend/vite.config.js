import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';
import dotenv from 'dotenv';

dotenv.config({ path: process.env.NODE_ENV === 'production' 
	? 'https://test-compass.refugium-romontberg.ch/' 
	: '127.0.0.1:8000/' });

export default defineConfig({
	plugins: [sveltekit()],
	define: {
		'process.env': process.env
	}
});
