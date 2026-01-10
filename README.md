# Personal Dashboard

A simple morning dashboard displaying current time, weather for Omaha NE, and Google Calendar events.

## Features

### Night Mode
Between midnight and 5am, the dashboard automatically switches to night mode: a dark screen with only the time displayed in large centered text. This makes it easy to check the time if you wake up at night without being blinded by the bright display.

To test night mode at any time, add `?night=1` to the URL:
```
https://localhost:8443/index.html?night=1
```

### Calendar Auto-Refresh
The Google Calendar iframe automatically refreshes once daily at 1am. This happens during night mode, so fresh calendar data is ready when you wake up.

## Development

Start the local HTTPS server:

```bash
python https_server.py
```

The server will automatically generate self-signed SSL certificates if they don't exist, then serve the dashboard at `https://localhost:8443/index.html`.

Your browser will show a security warning for the self-signed certificate - click "Advanced" → "Proceed to localhost (unsafe)" to continue.

## Deployment

You can use githack to view the HTML file directly from your github repo. For example:

Dev URL (no or little caching):
https://raw.githack.com/stillnet/dashboard/main/index.html

Production URL (uses caching):
https://rawcdn.githack.com/stillnet/dashboard/d5be3408a09d0524addd485f9a74182823637c1b/index.html