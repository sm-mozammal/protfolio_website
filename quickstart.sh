#!/bin/bash

# Portfolio API Quick Start Guide
# Run this script to get started with your dynamic portfolio system

echo "🚀 Dynamic Portfolio System - Quick Start"
echo "=========================================="
echo ""

# Check if we're in the right directory
if [ ! -f "manage.py" ]; then
    echo "❌ Error: Please run this script from the portfolio_project directory"
    exit 1
fi

echo "1️⃣  Creating superuser for admin access..."
python manage.py createsuperuser

echo ""
echo "2️⃣  Starting development server..."
echo ""
echo "✅ Server starting on http://localhost:8000"
echo ""
echo "📌 Important URLs:"
echo "   - Admin Panel: http://localhost:8000/admin/"
echo "   - API Root: http://localhost:8000/portfolio/api/"
echo "   - Browsable API: http://localhost:8000/portfolio/api/portfolios/"
echo ""
echo "🔑 After login, get your access token by:"
echo "   POST to http://localhost:8000/portfolio/api/auth/login/login/"
echo ""
echo "📚 For complete API documentation, see PORTFOLIO_API.md"
echo ""

python manage.py runserver
