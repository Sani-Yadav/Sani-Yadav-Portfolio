// Form handling functions
function showForm(jobTitle) {
    document.getElementById('overlay').style.display = 'block';
    document.getElementById('jobForm').style.display = 'block';
    document.getElementById('formTitle').textContent = 'Apply for: ' + jobTitle;
}

function hideForm() {
    document.getElementById('overlay').style.display = 'none';
    document.getElementById('jobForm').style.display = 'none';
}

// Add click event listeners to job items
document.addEventListener('DOMContentLoaded', function() {
    const jobItems = document.querySelectorAll('.job-list li');
    jobItems.forEach(item => {
        item.addEventListener('click', function() {
            const jobTitle = this.getAttribute('data-title');
            showForm(jobTitle);
        });
    });

    // Close form when clicking overlay
    document.getElementById('overlay').addEventListener('click', hideForm);
});

function searchJobs() {
    const input = document.getElementById('searchInput');
    const filter = input.value.toLowerCase();
    const jobList = document.getElementById('jobList');
    const jobs = jobList.getElementsByTagName('li');

    for (let i = 0; i < jobs.length; i++) {
        const jobTitle = jobs[i].getAttribute('data-title') || jobs[i].textContent;
        if (jobTitle.toLowerCase().indexOf(filter) > -1) {
            jobs[i].style.display = '';
        } else {
            jobs[i].style.display = 'none';
        }
    }
}

function filterCategory() {
    const category = document.getElementById('categoryFilter').value;
    const jobList = document.getElementById('jobList');
    const jobs = jobList.getElementsByTagName('li');

    for (let i = 0; i < jobs.length; i++) {
        const jobCategory = jobs[i].getAttribute('data-category');
        if (category === 'all' || jobCategory === category) {
            jobs[i].style.display = '';
        } else {
            jobs[i].style.display = 'none';
        }
    }
}

function submitForm() {
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const dob = document.getElementById('dob').value;
    const address = document.getElementById('address').value;

    // Basic validation
    if (!name || !email || !phone || !dob || !address) {
        alert('Please fill in all fields');
        return;
    }

    // Phone number validation
    if (!/^\d{10}$/.test(phone)) {
        alert('Please enter a valid 10-digit phone number');
        return;
    }

    // Email validation
    if (!/^\S+@\S+\.\S+$/.test(email)) {
        alert('Please enter a valid email address');
        return;
    }

    // Here you would typically send this data to your Django backend
    console.log('Form submitted:', {
        name: name,
        email: email,
        phone: phone,
        dob: dob,
        address: address
    });

    // Clear form and hide it
    document.getElementById('applicationForm').reset();
    hideForm();
    alert('Application submitted successfully!');
}

// Static files configuration
const STATIC_URL = '/static/';
const STATICFILES_DIRS = [BASE_DIR / 'static'];
