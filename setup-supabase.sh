#!/bin/bash

# Marragafay Supabase Integration - Quick Start Script
# This script helps you quickly set up the Supabase booking integration

echo "🚀 Marragafay Supabase Integration Setup"
echo "========================================"
echo ""

# Step 1: Check if .env.local exists
echo "Step 1: Checking environment configuration..."
if [ -f ".env.local" ]; then
    echo "✅ .env.local found"
    if grep -q "your-project-id" .env.local; then
        echo "⚠️  WARNING: Please update .env.local with your actual Supabase credentials!"
        echo "   Get them from: https://app.supabase.com > Your Project > Settings > API"
    else
        echo "✅ Environment variables appear to be configured"
    fi
else
    echo "❌ .env.local not found! Please create it first."
    exit 1
fi

echo ""

# Step 2: Check Supabase client files
echo "Step 2: Checking Supabase client files..."
if [ -f "js/supabase-client.js" ]; then
    echo "✅ Supabase client found"
else
    echo "❌ Supabase client not found"
fi

if [ -f "js/booking-handler.js" ]; then
    echo "✅ Booking handler found"
else
    echo "❌ Booking handler not found"
fi

echo ""

# Step 3: List pages that need forms updated
echo "Step 3: Pages requiring booking form integration:"
echo "   📦 Packages:"
echo "      - packages/basic.html (✓ Source of Truth)"
echo "      - packages/comfort.html"
echo "      - packages/premium.html"
echo "      - packages/luxe.html"
echo "      - packages/vip.html (if exists)"
echo "      - packages/family.html (if exists)"
echo ""
echo "   🎯 Activities:"
echo "      - activities/quad-biking.html"
echo "      - activities/camel-ride.html"
echo "      - activities/bike-tour.html"
echo "      - activities/*.html (all other activities)"

echo ""
echo "========================================"
echo "📋 Next Steps:"
echo "========================================"
echo ""
echo "1. Update .env.local with your Supabase credentials"
echo ""
echo "2. Update js/supabase-client.js with your Supabase URL and Anon Key"
echo ""
echo "3. Add these scripts to the <head> of all pages with booking forms:"
echo '   <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>'
echo '   <script src="../js/supabase-client.js"></script>'
echo '   <script src="../js/booking-handler.js"></script>'
echo ""
echo "4. Ensure each booking form has:"
echo '   - id="bookingForm"'
echo '   - Hidden input: <input type="hidden" name="package" value="[Package Name]">'
echo ""
echo "5. Test the booking flow on one page before rolling out to all pages"
echo ""
echo "6. Check Supabase dashboard to verify bookings are being created"
echo ""
echo "For detailed instructions, see: SUPABASE_INTEGRATION_GUIDE.md"
echo ""
