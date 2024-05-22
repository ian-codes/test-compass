import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';
import dotenv from 'dotenv';

dotenv.config({ path: process.env.NODE_ENV === 'production' ? '.env.production' : '.env' });

export default defineConfig({
	plugins: [sveltekit()],
	define: {
		'process.env': process.env
	}
});
