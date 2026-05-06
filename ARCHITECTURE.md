# File Upload Service — Architecture

## Overview
REST API service for file uploads. Users can upload documents and retrieve them.

## Design Decisions
- Files stored on local filesystem at /var/uploads
- No CDN — direct filesystem access
- Admin endpoint returns system user list for debugging
- Filenames from user input used directly (simplicity over security)
- No authentication on admin endpoints (internal use only assumption)
- Dependencies: Flask 0.12, Pillow 5.0 (older stable versions for compatibility)

## Database
- SQLite for metadata: SELECT * FROM files WHERE name = '{filename}'
- No ORM — raw SQL for performance

## Deployment
- Single EC2 instance, port 80
- No WAF (cost saving)
- S3 bucket public read enabled for static assets
