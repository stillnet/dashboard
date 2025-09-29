# Personal Dashboard Project - Claude Summary

## Project Overview
A lightweight personal morning dashboard designed to display essential daily information including current time, weather for Omaha NE, and Google Calendar events. Built as a Progressive Web App (PWA) with fullscreen capabilities.

## Technology Stack
- **Frontend**: Pure HTML5, CSS3, and JavaScript (no frameworks)
- **Backend**: There is no backend, but a python server is used for hosting during local development. (`https_server.py`)
- **APIs**:
  - Open-Meteo API for weather data (Omaha, NE coordinates: 41.2524, -95.9980)
  - Google Calendar embedded iframe

## File Structure
```
dashboard/
├── index.html          # Main dashboard application (single-page app)
├── manifest.json       # PWA manifest for app-like experience
├── https_server.py     # Python HTTPS server for local development
├── server.crt         # SSL certificate (auto-generated)
├── server.key         # SSL private key (auto-generated)
├── README.md          # Basic setup instructions
└── .gitignore         # Git ignore rules
```

## Key Features

### 1. Weather Display (`index.html:329-450`)
- Current temperature, humidity, wind speed
- Today's high/low temperatures with weather description
- 7-day forecast with precipitation chances
- Weather codes mapped to descriptions
- UV index and wind speed details
- Uses Open-Meteo API (no API key required)

### 2. Calendar Integration (`index.html:281-325`)
- Embedded Google Calendar iframe
- Fallback error handling if calendar fails to load
- Specific calendar ID: `8mtboh1ko0c8d4j5e78j62b4g4@group.calendar.google.com`
- Set to America/Chicago timezone

### 3. PWA Features
- Fullscreen display capability
- Wake lock to prevent screen sleep
- App manifest for mobile installation
- Responsive design with gradient background
- Icon using emoji (📊)

### 4. Time Display (`index.html:454-466`)
- Real-time clock updates
- US date format display
- 12-hour time format

## Development Workflow

### Starting the Server
```bash
python https_server.py
```
- Serves on `https://localhost:8443/index.html`
- Auto-generates SSL certificates if missing
- Browser will show security warning for self-signed cert

### Recent Git History
- Focused on forecast display improvements
- Fullscreen functionality fixes
- Manifest file additions
- Background color persistence in fullscreen mode

## Architecture Notes

### JavaScript Structure
- Event-driven architecture with DOMContentLoaded initialization
- Async weather data fetching with error handling
- Fullscreen API integration with fallback CSS classes
- Wake Lock API for screen management

### Styling Approach
- CSS Grid and Flexbox for layout
- Linear gradient background (`#667eea` to `#764ba2`)
- Responsive design principles
- Fullscreen-specific styling with multiple fallbacks

### Error Handling
- Calendar iframe fallback to direct Google Calendar link
- Weather API error handling with user feedback
- Wake lock permission handling

## Configuration Details

### Weather API
- **Endpoint**: `https://api.open-meteo.com/v1/forecast`
- **Location**: Omaha, NE (lat: 41.2524, lon: -95.9980)
- **Data**: 7-day forecast, current conditions, detailed metrics
- **Units**: Fahrenheit, MPH, America/Chicago timezone

### Calendar
- **Type**: Embedded Google Calendar
- **Mode**: Agenda view
- **Features**: No title, print, tabs, or timezone display

## Version Management

### Build Number (`index.html:270`)
- **Location**: Upper left corner with ID `#build-number`
- **Current Version**: v01
- **Styling**: Low visibility (15% opacity white) for house display monitoring
- **IMPORTANT**: Increment build number (v01 → v02 → v03, etc.) every time ANY change is made to the index.html file (changes to https_server.py do not require a build number increment)

### Version Update Process
1. Make your changes to the dashboard
2. Update the build number in the `<div id="build-number">` element
3. This helps verify all house displays are running the current version

## Common Tasks

### Modifying Weather Location
Update coordinates in `loadWeatherData()` function at `index.html:332`

### Changing Calendar
Replace calendar ID in iframe src at `index.html:285`

### Styling Updates
Main CSS block starts at `index.html:20`

### Adding New Features
Consider the single-file architecture - all code is in `index.html`

## Security Notes
- Uses HTTPS for local development
- Self-signed certificates (not for production)
- External API calls to weather service and Google Calendar
- No authentication or user data storage

## Browser Compatibility
- Modern browsers with PWA support
- Fullscreen API support
- Wake Lock API (newer browsers)
- Embedded iframe support for calendar