document.addEventListener('DOMContentLoaded', () => {
    const generateBtn = document.getElementById('generateBtn');
    const promptInput = document.getElementById('prompt');
    const statusDiv = document.getElementById('status');
    const statusText = document.getElementById('statusText');
    const resultDiv = document.getElementById('result');
    const videoPlayer = document.getElementById('videoPlayer');

    generateBtn.addEventListener('click', async () => {
        const prompt = promptInput.value.trim();
        if (!prompt) {
            alert('Please enter a prompt');
            return;
        }

        // Show loading state
        generateBtn.disabled = true;
        statusDiv.classList.remove('hidden');
        resultDiv.classList.add('hidden');
        statusText.textContent = 'Generating your video...';

        try {
            const response = await fetch('/api/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ prompt }),
            });

            if (!response.ok) {
                throw new Error('Failed to generate video');
            }

            const data = await response.json();
            
            // Update video player
            videoPlayer.src = data.video_url;
            resultDiv.classList.remove('hidden');
            statusText.textContent = 'Video generated successfully!';
        } catch (error) {
            console.error('Error:', error);
            statusText.textContent = 'Error generating video. Please try again.';
        } finally {
            generateBtn.disabled = false;
        }
    });
});
