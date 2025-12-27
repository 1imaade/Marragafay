-- Run this script in your Supabase SQL Editor to fix the schema cache error
-- and ensure all columns required by the Booking Form exist.

ALTER TABLE bookings ADD COLUMN IF NOT EXISTS name TEXT;
ALTER TABLE bookings ADD COLUMN IF NOT EXISTS email TEXT;
ALTER TABLE bookings ADD COLUMN IF NOT EXISTS phone_number TEXT;
ALTER TABLE bookings ADD COLUMN IF NOT EXISTS date DATE; -- Ensure this is DATE type
ALTER TABLE bookings ADD COLUMN IF NOT EXISTS guests INTEGER;
ALTER TABLE bookings ADD COLUMN IF NOT EXISTS adults INTEGER;
ALTER TABLE bookings ADD COLUMN IF NOT EXISTS children INTEGER;
ALTER TABLE bookings ADD COLUMN IF NOT EXISTS package_title TEXT;
ALTER TABLE bookings ADD COLUMN IF NOT EXISTS notes TEXT;
ALTER TABLE bookings ADD COLUMN IF NOT EXISTS total_price NUMERIC;

-- Optional: Add comments to columns for clarity
COMMENT ON COLUMN bookings.name IS 'Customer full name';
COMMENT ON COLUMN bookings.email IS 'Customer email address';
COMMENT ON COLUMN bookings.phone_number IS 'Customer phone number';
COMMENT ON COLUMN bookings.guests IS 'Total number of guests (adults + children)';
COMMENT ON COLUMN bookings.adults IS 'Number of adults';
COMMENT ON COLUMN bookings.children IS 'Number of children';

-- Ensure Row Level Security (RLS) handles insertions properly
ALTER TABLE bookings ENABLE ROW LEVEL SECURITY;

-- Policy to allow anyone (public) to insert bookings
-- Drop existing policy if it conflicts or just create if not exists
DO $$ 
BEGIN
    IF NOT EXISTS (
        SELECT 1 
        FROM pg_policies 
        WHERE tablename = 'bookings' 
        AND policyname = 'Allow public insert'
    ) THEN
        CREATE POLICY "Allow public insert" ON bookings FOR INSERT WITH CHECK (true);
    END IF;
END $$;
