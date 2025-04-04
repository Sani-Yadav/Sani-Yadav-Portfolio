// Get elements
const jobList = document.getElementById('jobList');
const jobForm = document.getElementById('jobForm');
const overlay = document.getElementById('overlay');
const formTitle = document.getElementById('formTitle');
const searchInput = document.getElementById('searchInput');
const categoryFilter = document.getElementById('categoryFilter');

// Function to open job application form
function openJobForm(jobTitle) {
    formTitle.textContent = `Apply for ${jobTitle}`;
    jobForm.style.display = 'block';
    overlay.style.display = 'block';
}

// Function to close job application form
function closeJobForm() {
    jobForm.style.display = 'none';
    overlay.style.display = 'none';
}

// Event listener for job list click
jobList.addEventListener('click', (e) => {
    if (e.target.tagName === 'LI') {
        openJobForm(e.target.getAttribute('data-title'));
    }
});

// Event listener for overlay click to close form
overlay.addEventListener('click', closeJobForm);

// Function to search jobs
function searchJobs() {
    const input = searchInput.value.toUpperCase();
    const jobItems = jobList.getElementsByTagName('li');

    Array.from(jobItems).forEach(job => {
        const jobTitle = job.textContent || job.innerText;
        job.style.display = jobTitle.toUpperCase().includes(input) ? '' : 'none';
    });
}

// Function to filter jobs by category
function filterCategory() {
    const selectedCategory = categoryFilter.value;
    const jobItems = jobList.getElementsByTagName('li');

    Array.from(jobItems).forEach(job => {
        const category = job.getAttribute('data-category');
        job.style.display = (selectedCategory === 'all' || category === selectedCategory) ? '' : 'none';
    });
}

// Add event listeners for search and category filter
searchInput.addEventListener('input', searchJobs);
categoryFilter.addEventListener('change', filterCategory);

// Function to handle form submission
function submitForm() {
    // Get form field values
    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const phone = document.getElementById("phone").value.trim();
    const dob = document.getElementById("dob").value;
    const address = document.getElementById("address").value.trim();

    // Regular expression for email and phone validation
    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    const phonePattern = /^[0-9]{10}$/;

    // Form validation
    if (!name || !email || !phone || !dob || !address) {
        alert("Please fill out all fields.");
        return;
    }
    
    if (!emailPattern.test(email)) {
        alert("Please enter a valid email address.");
        return;
    }

    if (!phonePattern.test(phone)) {
        alert("Please enter a valid 10-digit phone number.");
        return;
    }

    // Show success message after form validation
    alert("Form submitted successfully!");

    // Clear form fields after submission
    document.getElementById("applicationForm").reset();
}
