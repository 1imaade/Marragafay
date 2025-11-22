import { NextRequest, NextResponse } from 'next/server';
import { createClient } from '@supabase/supabase-js';

// Initialize Supabase client with service role key (server-side only)
const supabase = createClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.SUPABASE_SERVICE_ROLE_KEY! // Use service role key for server-side operations
);

/**
 * POST /api/website/bookings
 * Creates a new booking in the Supabase database
 */
export async function POST(request: NextRequest) {
    try {
        // Parse request body
        const body = await request.json();

        // Validate required fields
        if (!body.name || !body.email || !body.phone || !body.package || !body.date) {
            return NextResponse.json(
                {
                    success: false,
                    error: 'Missing required fields'
                },
                { status: 400 }
            );
        }

        // Map frontend form fields to database schema
        const bookingData = {
            customer_name: body.name,
            customer_email: body.email,
            phone: body.countryCode + body.phone, // Combine country code and phone number
            package_title: body.package,
            booking_date: body.date,
            guests_count: parseInt(body.guests) || 2,
            status: 'pending'
        };

        // Insert booking into Supabase
        const { data, error } = await supabase
            .from('bookings')
            .insert([bookingData])
            .select();

        if (error) {
            console.error('Supabase error:', error);
            return NextResponse.json(
                {
                    success: false,
                    error: error.message || 'Database error occurred'
                },
                { status: 400 }
            );
        }

        // Return success response
        return NextResponse.json({
            success: true,
            booking: data[0],
            message: 'Booking created successfully'
        });

    } catch (error) {
        console.error('API error:', error);
        return NextResponse.json(
            {
                success: false,
                error: error instanceof Error ? error.message : 'Internal server error'
            },
            { status: 500 }
        );
    }
}

/**
 * GET /api/website/bookings
 * Retrieves bookings (optional - for admin dashboard)
 */
export async function GET(request: NextRequest) {
    try {
        const { searchParams } = new URL(request.url);
        const email = searchParams.get('email');

        let query = supabase.from('bookings').select('*');

        // Filter by email if provided
        if (email) {
            query = query.eq('customer_email', email);
        }

        const { data, error } = await query.order('created_at', { ascending: false });

        if (error) {
            throw error;
        }

        return NextResponse.json({
            success: true,
            bookings: data
        });

    } catch (error) {
        console.error('API error:', error);
        return NextResponse.json(
            {
                success: false,
                error: error instanceof Error ? error.message : 'Internal server error'
            },
            { status: 500 }
        );
    }
}
