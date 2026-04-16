#!/bin/bash

# Portfolio Project Startup Script
# Run the Django development server with proper environment

cd /Users/limerickdev/myproject/portfolio_project

echo "🚀 Starting Portfolio Development Server..."
echo "📍 Navigate to: http://127.0.0.1:8000/portfolio/"
echo "🔐 Admin Login: http://127.0.0.1:8000/portfolio/admin/login/"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

/Users/limerickdev/myproject/venv/bin/python manage.py runserver
