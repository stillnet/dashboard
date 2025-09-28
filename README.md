# Personal Dashboard

A simple morning dashboard displaying current time, weather for Omaha NE, and Google Calendar events.

## Development

Start the local HTTPS server:

```bash
python https_server.py
```

The server will automatically generate self-signed SSL certificates if they don't exist, then serve the dashboard at `https://localhost:8443/index.html`.

Your browser will show a security warning for the self-signed certificate - click "Advanced" → "Proceed to localhost (unsafe)" to continue.