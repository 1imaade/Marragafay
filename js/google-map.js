// ========================================
// GOOGLE MAPS - OPTIMIZED VERSION
// ========================================
// CRITICAL FIX: Removed geocoding API calls that were triggering on every page load
// Now using cached coordinates to prevent excessive API requests

var google;

function init() {
    // ========================================
    // CACHED COORDINATES - NO API CALLS
    // ========================================
    // Pre-cached coordinates to avoid geocoding API calls
    // Update these coordinates for your actual location
    
    // Agafay Desert approximate coordinates (Morocco)
    // Change these to your actual business location
    var agafayLocation = new google.maps.LatLng(31.3728, -8.0208); // Agafay Desert, Morocco
    
    // Map configuration
    var mapOptions = {
        zoom: 12, // Adjusted zoom for desert area
        center: agafayLocation,
        scrollwheel: false,
        
        // Luxury map styling
        styles: [
            {
                "featureType": "administrative.country",
                "elementType": "geometry",
                "stylers": [
                    {
                        "visibility": "simplified"
                    },
                    {
                        "hue": "#d4af37" // Gold theme
                    }
                ]
            },
            {
                "featureType": "landscape",
                "elementType": "geometry",
                "stylers": [
                    {
                        "color": "#f5f5f5"
                    }
                ]
            },
            {
                "featureType": "poi",
                "elementType": "labels",
                "stylers": [
                    {
                        "visibility": "on"
                    }
                ]
            }
        ]
    };

    // Check if map element exists before initializing
    var mapElement = document.getElementById('map');
    
    if (!mapElement) {
        console.warn('Google Maps: Map container not found. Skipping initialization.');
        return;
    }

    // Create the Google Map
    var map = new google.maps.Map(mapElement, mapOptions);
    
    // ========================================
    // STATIC MARKERS - NO GEOCODING API CALLS
    // ========================================
    // Define your locations with pre-calculated coordinates
    var locations = [
        {
            name: 'Agafay Desert Camp',
            lat: 31.3728,
            lng: -8.0208,
            icon: 'images/loc.png'
        }
        // Add more locations here if needed:
        // {
        //   name: 'Location 2',
        //   lat: 31.xxxx,
        //   lng: -8.xxxx,
        //   icon: 'images/loc.png'
        // }
    ];

    // Create markers without API calls
    locations.forEach(function(location) {
        var latlng = new google.maps.LatLng(location.lat, location.lng);
        var marker = new google.maps.Marker({
            position: latlng,
            map: map,
            icon: location.icon,
            title: location.name,
            animation: google.maps.Animation.DROP // Add drop animation
        });
        
        // Optional: Add click listener for marker
        marker.addListener('click', function() {
            // You can add info window here if needed
            console.log('Marker clicked:', location.name);
        });
    });
}

// Initialize map when DOM is ready
if (typeof google !== 'undefined' && google.maps) {
    google.maps.event.addDomListener(window, 'load', init);
} else {
    console.warn('Google Maps API not loaded');
}