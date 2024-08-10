document.addEventListener('DOMContentLoaded', function() {
    
    document.getElementById('reportForm').addEventListener('submit', async function (event) {
        event.preventDefault();
    
        // Create FormData object
        const formData = new FormData(this);
    
        try {
            // Send data to Flask endpoint
            const response = await fetch('/submit_form', {
                method: 'POST',
                body: formData
            });
    
            // Check if response is OK
            if (!response.ok) {
                throw new Error('Network response was not ok.');
            }
    
            // Parse JSON response
            const result = await response.json();
    
            // Display JSON response
            document.getElementById('jsonOutput').textContent = JSON.stringify(result, null, 4);
        } catch (error) {
            console.error('Error:', error);
            document.getElementById('jsonOutput').textContent = 'An error occurred. Please try again.';
        }
    });
    

});
