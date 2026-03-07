// main.js - UI enhancements and functionality

// DRAG & DROP UPLOAD BOX
const uploadBox = document.querySelector('.upload-box');
const fileInput = document.getElementById('file-input');
const previewSection = document.getElementById('preview-section');
const previewImg = document.getElementById('preview-img');
const filenameDisplay = document.getElementById('filename-display');
const submitBtn = document.getElementById('submit-btn');
const cancelBtn = document.getElementById('cancel-btn');
const uploadForm = document.getElementById('upload-form');
const loader = document.getElementById('loader');

if (uploadBox && fileInput) {
    // Drag and drop events
    ['dragenter', 'dragover'].forEach(eventName => {
        uploadBox.addEventListener(eventName, (e) => {
            e.preventDefault();
            e.stopPropagation();
            uploadBox.classList.add('dragover');
        });
    });

    ['dragleave', 'drop'].forEach(eventName => {
        uploadBox.addEventListener(eventName, (e) => {
            e.preventDefault();
            e.stopPropagation();
            uploadBox.classList.remove('dragover');
        });
    });

    uploadBox.addEventListener('drop', (e) => {
        const files = e.dataTransfer.files;
        if (files.length) {
            fileInput.files = files;
            handleFileSelect();
        }
    });

    // File selection change event
    fileInput.addEventListener('change', handleFileSelect);

    function handleFileSelect() {
        if (fileInput.files.length) {
            const file = fileInput.files[0];
            const reader = new FileReader();

            reader.onload = (e) => {
                // Show preview
                previewImg.src = e.target.result;
                filenameDisplay.textContent = '📄 ' + file.name;
                previewSection.style.display = 'block';

                // Show buttons
                submitBtn.style.display = 'inline-block';
                cancelBtn.style.display = 'inline-block';
            };

            reader.readAsDataURL(file);
        }
    }

    // Cancel button - clear and reset
    if (cancelBtn) {
        cancelBtn.addEventListener('click', () => {
            fileInput.value = '';
            previewSection.style.display = 'none';
            submitBtn.style.display = 'none';
            cancelBtn.style.display = 'none';
        });
    }

    // Form submission - show loader
    if (uploadForm) {
        uploadForm.addEventListener('submit', () => {
            loader.style.display = 'flex';
        });
    }
}
