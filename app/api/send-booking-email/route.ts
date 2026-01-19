import { NextRequest, NextResponse } from 'next/server';
import { sendBookingNotification, BookingData } from '../../actions/send-email';

/**
 * POST /api/send-booking-email
 * 
 * API Route to send booking notification emails
 * This route can be called from the static HTML booking form via fetch()
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
export async function POST(request: NextRequest) {
    try {
        console.log('📧 [API Route] /api/send-booking-email called');

        // Parse request body
        const bookingData: BookingData = await request.json();

        console.log('📋 Received booking data:', JSON.stringify(bookingData, null, 2));

        // Validate required fields
        if (!bookingData.name || !bookingData.email) {
            return NextResponse.json(
                {
                    success: false,
                    error: 'Missing required fields: name and email are required'
                },
                { status: 400 }
            );
        }

        // Call the server action to send the email
        const result = await sendBookingNotification(bookingData);

        if (result.success) {
            return NextResponse.json({
                success: true,
                message: result.message,
                id: result.id,
            });
        } else {
            // Don't expose internal errors to client in production
            console.error('❌ Email sending failed:', result.error);
            return NextResponse.json(
                {
                    success: false,
                    error: 'Failed to send notification. Your booking was still saved.'
                },
                { status: 500 }
            );
        }

    } catch (error: any) {
        console.error('❌ [API Route] Error:', error);
        return NextResponse.json(
            {
                success: false,
                error: 'An unexpected error occurred'
            },
            { status: 500 }
        );
    }
}

/**
 * GET /api/send-booking-email
 * 
 * Health check endpoint
 */
export async function GET() {
    return NextResponse.json({
        status: 'ok',
        message: 'Booking email API is running',
        timestamp: new Date().toISOString(),
    });
}
