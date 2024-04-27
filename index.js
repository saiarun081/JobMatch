document.addEventListener("DOMContentLoaded", function() {
    const jobTableBody = document.getElementById("jobTableBody");
    const fetchJobDescriptionBtn = document.getElementById("fetchJobDescription");
    const jobTitlesDropdown = document.getElementById("jobTitlesDropdown");

    let jobData; // Variable to store the job data

    fetch("download.json")
        .then(response => response.json())
        .then(data => {
            jobData = data; // Store the job data in the variable
            // Populate job titles dropdown
            const uniqueJobTitles = [...new Set(jobData.map(job => job.job_title))];
            uniqueJobTitles.forEach(title => {
                const option = document.createElement("option");
                option.value = title;
                option.textContent = title;
                jobTitlesDropdown.appendChild(option);
            });

            // Populate job table
            jobData.forEach(job => {
                const row = document.createElement("tr");
                row.innerHTML = `
                    <td>${job.job_title}</td>
                    <td>${job.salary}</td>
                    <td>${job.salary_currency}</td>
                    <td>${job.employee_residence}</td>
                    <td>${job.experience_level}</td>
                    <td>${job.company_size}</td>
                    <td>${job.employment_type}</td>
                    <td>${job.company_location}</td>
                `;
                jobTableBody.appendChild(row);
            });
        })
        .catch(error => console.log("Error:", error));

    // Event listener for fetching job description
    fetchJobDescriptionBtn.addEventListener("click", function() {
        const jobId = prompt("Enter Job ID:");
        if (jobId) {
            const job = jobData.find(job => job.JobmatchID === jobId);
            if (job) {
                alert(`Job Description: ${job.job_title} - ${job.salary_currency}${job.salary}`);
            } else {
                alert("Job ID not found!");
            }
        }
    });

    // Event listener for filtering jobs based on selected job title
    jobTitlesDropdown.addEventListener("change", function() {
        const selectedTitle = this.value;
        const rows = jobTableBody.querySelectorAll("tr");
        rows.forEach(row => {
            const jobTitle = row.querySelector("td:first-child").textContent;
            if (selectedTitle === "" || jobTitle === selectedTitle) {
                row.style.display = "table-row";
            } else {
                row.style.display = "none";
            }
        });
    });
});
