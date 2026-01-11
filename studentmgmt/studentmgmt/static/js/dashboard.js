// ============================================
// DASHBOARD.JS - INTERACTIVE FEATURES
// ============================================

console.log('✅ Dashboard JS loaded');

// ============================================
// INITIALIZATION
// ============================================

document.addEventListener('DOMContentLoaded', function() {
    console.log('📊 Dashboard initialized');
    
    // Initialize features
    animateStatNumbers();
    setLastUpdateTime();
    addSmoothScrolling();
    setupNavigation();
    initializeTooltips();
    
    // Log user info
    logDashboardInfo();
});

// ============================================
// ANIMATE STAT NUMBERS
// ============================================

function animateStatNumbers() {
    const statNumbers = document.querySelectorAll('.stat-number');
    
    statNumbers.forEach(element => {
        const finalValue = parseInt(element.textContent) || 0;
        let currentValue = 0;
        
        // Skip animation for 0
        if (finalValue === 0) {
            element.textContent = '0';
            return;
        }
        
        const increment = Math.ceil(finalValue / 30);
        const duration = 1000; // milliseconds
        const steps = 30;
        const stepDuration = duration / steps;
        
        const counter = setInterval(() => {
            currentValue += increment;
            if (currentValue >= finalValue) {
                element.textContent = finalValue;
                clearInterval(counter);
            } else {
                element.textContent = currentValue;
            }
        }, stepDuration);
    });
}

// ============================================
// SET LAST UPDATE TIME
// ============================================

function setLastUpdateTime() {
    const lastUpdateElement = document.getElementById('lastUpdate');
    if (lastUpdateElement) {
        const now = new Date();
        const timeString = now.toLocaleTimeString();
        lastUpdateElement.textContent = `${timeString}`;
    }
}

// ============================================
// SMOOTH SCROLLING
// ============================================

function addSmoothScrolling() {
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            const targetElement = document.querySelector(href);
            
            if (targetElement) {
                e.preventDefault();
                targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });
}

// ============================================
// NAVIGATION
// ============================================

function setupNavigation() {
    const navLinks = document.querySelectorAll('nav a, .nav-link');
    const currentLocation = window.location.pathname;
    
    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        
        // Check if link matches current page
        if (href === currentLocation || href.includes(currentLocation)) {
            link.classList.add('active');
        }
        
        // Add hover effect
        link.addEventListener('mouseenter', function() {
            this.style.transition = 'all 0.3s ease';
        });
    });
}

// ============================================
// TOOLTIPS
// ============================================

function initializeTooltips() {
    const tooltipElements = document.querySelectorAll('[data-tooltip]');
    
    tooltipElements.forEach(element => {
        element.addEventListener('mouseenter', function() {
            const tooltip = this.getAttribute('data-tooltip');
            showTooltip(this, tooltip);
        });
        
        element.addEventListener('mouseleave', function() {
            hideTooltip(this);
        });
    });
}

function showTooltip(element, text) {
    const tooltip = document.createElement('div');
    tooltip.className = 'tooltip';
    tooltip.textContent = text;
    
    document.body.appendChild(tooltip);
    
    const rect = element.getBoundingClientRect();
    tooltip.style.position = 'fixed';
    tooltip.style.top = (rect.top - tooltip.offsetHeight - 5) + 'px';
    tooltip.style.left = (rect.left + rect.width / 2 - tooltip.offsetWidth / 2) + 'px';
    
    setTimeout(() => tooltip.classList.add('show'), 0);
}

function hideTooltip(element) {
    const tooltip = document.querySelector('.tooltip.show');
    if (tooltip) {
        tooltip.classList.remove('show');
        setTimeout(() => tooltip.remove(), 300);
    }
}

// ============================================
// LOGGING
// ============================================

function logDashboardInfo() {
    const studentCount = document.getElementById('studentCount');
    const courseCount = document.getElementById('courseCount');
    
    if (studentCount && courseCount) {
        console.log('📊 Dashboard Statistics:');
        console.log(`   👥 Total Students: ${studentCount.textContent}`);
        console.log(`   📚 Total Courses: ${courseCount.textContent}`);
        console.log(`   🕐 Loaded at: ${new Date().toLocaleTimeString()}`);
    }
}

// ============================================
// UTILITIES
// ============================================

// Refresh dashboard data every 5 minutes
setInterval(() => {
    console.log('🔄 Dashboard data refreshed');
    // Add your refresh logic here
}, 5 * 60 * 1000);

// Log page visibility
document.addEventListener('visibilitychange', function() {
    if (document.hidden) {
        console.log('👋 Dashboard hidden');
    } else {
        console.log('👁️ Dashboard visible');
    }
});

console.log('✅ All dashboard features initialized');
