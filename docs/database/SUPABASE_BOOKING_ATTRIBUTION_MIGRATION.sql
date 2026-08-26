-- Marragafay booking attribution migration
-- Review and apply through the normal Supabase migration process.
-- This file is intentionally not executed by the development task.

ALTER TABLE public.bookings
  ADD COLUMN IF NOT EXISTS attribution jsonb;

COMMENT ON COLUMN public.bookings.attribution IS
  'Validated acquisition context: first_touch, optional last_touch, source_category, and booking_page';

DO $$
BEGIN
  IF NOT EXISTS (
    SELECT 1
    FROM pg_constraint
    WHERE conname = 'bookings_attribution_object_check'
      AND conrelid = 'public.bookings'::regclass
  ) THEN
    ALTER TABLE public.bookings
      ADD CONSTRAINT bookings_attribution_object_check
      CHECK (attribution IS NULL OR jsonb_typeof(attribution) = 'object');
  END IF;
END
$$;
