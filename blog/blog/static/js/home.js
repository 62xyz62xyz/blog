// scripts.js

document.addEventListener('DOMContentLoaded', () => {
    const generateTokenBtn = document.getElementById('generateTokenBtn');
    const tokenDisplay = document.getElementById('tokenDisplay');
    const tokenText = document.getElementById('tokenText');
    const copyTokenBtn = document.getElementById('copyTokenBtn');
    const submitFormBtn = document.getElementById('submitFormBtn');
    const tokenForm = document.getElementById('tokenForm');

    generateTokenBtn.addEventListener('click', () => {
        // Simulate token generation
        const token = 'your_generated_token_' + Math.random().toString(36).substr(2);
        tokenText.textContent = token;
        tokenDisplay.classList.remove('hidden');
    });

    copyTokenBtn.addEventListener('click', () => {
        navigator.clipboard.writeText(tokenText.textContent).then(() => {
            alert('Token copied to clipboard!');
        }).catch(err => {
            alert('Failed to copy token: ' + err);
        });
    });

    submitFormBtn.addEventListener('click', () => {
        // Manually submit the form
        tokenForm.submit();
    });
});
// scripts.js

document.addEventListener('DOMContentLoaded', () => {
    const generateTokenBtn = document.getElementById('generateTokenBtn');
    const tokenDisplay = document.getElementById('tokenDisplay');
    const tokenText = document.getElementById('tokenText');
    const copyTokenBtn = document.getElementById('copyTokenBtn');
    const submitFormBtn = document.getElementById('submitFormBtn');
    const tokenForm = document.getElementById('tokenForm');

    generateTokenBtn.addEventListener('click', () => {
        // Simulate token generation
        const token = 'your_generated_token_' + Math.random().toString(36).substr(2);
        tokenText.textContent = token;
        tokenDisplay.classList.remove('hidden');
    });

    copyTokenBtn.addEventListener('click', () => {
        navigator.clipboard.writeText(tokenText.textContent).then(() => {
            alert('Token copied to clipboard!');
        }).catch(err => {
            alert('Failed to copy token: ' + err);
        });
    });

    submitFormBtn.addEventListener('click', () => {
        // Manually submit the form
        tokenForm.submit();
    });
});
