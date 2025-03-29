document.addEventListener('DOMContentLoaded', function() {
    // Theme toggle functionality
    const themeToggle = document.getElementById('themeToggle');
    const body = document.body;
    
    // Check for saved theme preference
    const savedTheme = localStorage.getItem('theme') || 'light';
    if (savedTheme === 'dark') {
        body.classList.add('bg-dark', 'text-white');
        themeToggle.innerHTML = '<i class="bi bi-sun"></i>';
    }
    
    themeToggle.addEventListener('click', function() {
        body.classList.toggle('bg-dark');
        body.classList.toggle('text-white');
        
        const isDark = body.classList.contains('bg-dark');
        localStorage.setItem('theme', isDark ? 'dark' : 'light');
        themeToggle.innerHTML = isDark ? '<i class="bi bi-sun"></i>' : '<i class="bi bi-moon-stars"></i>';
        
        // Update charts when theme changes
        updateChartThemes(isDark);
    });
    
    // AJAX form submission for filters
    const filterForm = document.querySelector('form[method="get"]');
    if (filterForm) {
        const selects = filterForm.querySelectorAll('select');
        selects.forEach(select => {
            select.addEventListener('change', function() {
                filterForm.submit();
            });
        });
    }
    
    // Chart theme update function
    function updateChartThemes(isDark) {
        const chartContainers = document.querySelectorAll('.js-plotly-plot');
        chartContainers.forEach(container => {
            const plotId = container.id;
            const plot = document.getElementById(plotId);
            const layout = JSON.parse(JSON.stringify(plot.layout));
            
            layout.paper_bgcolor = isDark ? '#212529' : '#ffffff';
            layout.plot_bgcolor = isDark ? '#343a40' : '#f8f9fa';
            layout.font = { color: isDark ? '#ffffff' : '#000000' };
            
            Plotly.relayout(plotId, layout);
        });
    }
    
    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});