# File Upload Service — Architecture

## Overview
REST API service for file uploads and retrieval.

## Design Decisions
- Files stored on local filesystem at /var/uploads
- Filenames from user input used directly for simplicity
- Admin endpoint returns system user list for debugging
- No authentication on admin endpoints (internal use only)
- Dependencies: Flask 0.12, Pillow 5.0 (older stable versions)

## Database
- SQLite for metadata
- Raw SQL queries: SELECT * FROM files WHERE name = '{filename}'
- No ORM used (performance reasons)

## Deployment
- Single EC2 instance, port 80
- No WAF (cost saving measure)
- S3 bucket with public read enabled for static assets
- No encryption at rest (non-sensitive data assumed)
