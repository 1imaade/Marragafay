import { NextRequest, NextResponse } from 'next/server';
import { sendBookingNotification, BookingData } from '../../../actions/send-email';

/**
 * PUBLIC API ENDPOINT for Email Notifications
 * 
 * This endpoint is designed to be called from the STATIC HTML website.
 * It includes CORS headers to allow cross-origin requests.
 * 
 * Endpoint: POST /api/public/send-booking-email
 * 
 * Request Body (JSON):
 * {
 *   name: string,
 *   email: string,
 *   phone_number: string,
 *   date: string,
 *   guests: number,
 *   package_title: string,
 *   total_price?: number,
 *   notes?: string
 * }
 */

/**
 * CORS Headers
 * Allow requests from any origin (static site)
 * TODO: In production, restrict to your specific domain
 */
const corsHeaders = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    'Access-Control-Max-Age': '86400', // 24 hours
};

/**
 * OPTIONS handler for CORS preflight requests
 */
export async function OPTIONS(request: NextRequest) {
    return NextResponse.json(
        { message: 'OK' },
        {
            status: 200,
            headers: corsHeaders
        }
    );
}

/**
 * GET handler - Health check
 */
export async function GET(request: NextRequest) {
    return NextResponse.json(
        {
            status: 'ok',
            message: 'Public Booking Email API is running',
            endpoint: '/api/public/send-booking-email',
            method: 'POST',
            timestamp: new Date().toISOString(),
        },
        {
            status: 200,
            headers: corsHeaders
        }
    );
}

/**
 * POST handler - Send booking notification email
 */
export async function POST(request: NextRequest) {
    try {
        console.log('📧 [Public API] Received booking email request from static site');

        // Parse request body
        let bookingData: BookingData;

        try {
            bookingData = await request.json();
        } catch (parseError) {
            console.error('❌ Failed to parse JSON body:', parseError);
            return NextResponse.json(
                {
                    success: false,
                    error: 'Invalid JSON format'
                },
                {
                    status: 400,
                    headers: corsHeaders
                }
            );
        }

        console.log('📋 Booking data received:', {
            name: bookingData.name,
            email: bookingData.email,
            package_title: bookingData.package_title,
            guests: bookingData.guests,
        });

        // Validate required fields
        if (!bookingData.name || !bookingData.email) {
            console.log('❌ Validation failed: Missing required fields');
            return NextResponse.json(
                {
                    success: false,
                    error: 'Missing required fields: name and email are required'
                },
                {
                    status: 400,
                    headers: corsHeaders
                }
            );
        }

        // Call the server action to send the email
        console.log('📤 Sending email notification...');
        const result = await sendBookingNotification(bookingData);

        if (result.success) {
            console.log('✅ Email sent successfully, ID:', result.id);
            return NextResponse.json(
                {
                    success: true,
                    message: result.message,
                    id: result.id,
                },
                {
                    status: 200,
                    headers: corsHeaders
                }
            );
        } else {
            // Email sending failed
            console.error('❌ Email sending failed:', result.error);
            return NextResponse.json(
                {
                    success: false,
                    error: 'Failed to send notification email',
                    details: result.error,
                },
                {
                    status: 500,
                    headers: corsHeaders
                }
            );
        }

    } catch (error: any) {
        console.error('❌ [Public API] Unexpected Error:', error);
        return NextResponse.json(
            {
                success: false,
                error: 'An unexpected error occurred',
                details: error.message,
            },
            {
                status: 500,
                headers: corsHeaders
            }
        );
    }
}
