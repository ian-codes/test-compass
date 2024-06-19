import { writable, derived } from 'svelte/store';
import { page } from '$app/stores';

// Function to extract parent path
function getParentPath(pathname) {
    let lastSlashIndex = pathname.lastIndexOf('/');
    return lastSlashIndex > 0 ? pathname.substring(0, lastSlashIndex) : '/';
}

// Derived store that calculates backUrl based on the current page's URL
export const backUrl = derived(page, $page => getParentPath($page.url.pathname));
