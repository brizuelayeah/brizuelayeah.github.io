document.addEventListener('DOMContentLoaded', function() {

    const subjectToggles = document.querySelectorAll('.subject-toggle');
    subjectToggles.forEach(toggle => {
        toggle.addEventListener('click', function() {
            const subjectDropdown = this.nextElementSibling;
            if (subjectDropdown && subjectDropdown.classList.contains('subject-dropdown')) {
                subjectDropdown.classList.toggle('active');
            }
        });
    });


    const toggles = document.querySelectorAll('.projects-toggle');
    toggles.forEach(toggle => {
        toggle.addEventListener('click', function() {
            console.log('Toggle clicked'); // Debugging line
            const projectsList = this.nextElementSibling;
            if (projectsList && projectsList.classList.contains('projects-list')) {
                projectsList.classList.toggle('active');
                console.log('Projects list toggled'); // Debugging line
            }
        });
    });
});
