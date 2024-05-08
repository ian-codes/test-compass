/* export async function handle({ request, resolve }) {
    const cookies = request.headers.cookie || '';
    const user = getUserFromCookies(cookies); // Decode user info from HttpOnly cookie

    // Attach user to session
    request.locals.user = user; // user could be null if not logged in

    const response = await resolve(request);

    // You can modify or add headers to the response here if needed
    return response; 
} */
