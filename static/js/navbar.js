// Function to load the navbar
async function loadNavbar() {
    try {
        const response = await fetch('../components/navbar.html');
        const html = await response.text();
        
        // Create a temporary container
        const temp = document.createElement('div');
        temp.innerHTML = html;
        
        // Get the navbar and script elements
        const navbar = temp.querySelector('header');
        const script = temp.querySelector('script');
        
        // Insert the navbar at the beginning of the body
        document.body.insertBefore(navbar, document.body.firstChild);
        
        // Execute the script
        if (script) {
            const newScript = document.createElement('script');
            newScript.textContent = script.textContent;
            document.body.appendChild(newScript);
        }
    } catch (error) {
        console.error('Error loading navbar:', error);
    }
}

// Load the navbar when the DOM is ready
document.addEventListener('DOMContentLoaded', loadNavbar); 