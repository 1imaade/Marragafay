-- Supabase Schema for Contact Messages Table
-- Run this in Supabase SQL Editor if the table doesn't exist

CREATE TABLE IF NOT EXISTS messages (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT NOT NULL,
  subject TEXT NOT NULL,
  message TEXT NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  status TEXT DEFAULT 'unread' CHECK (status IN ('unread', 'read', 'archived'))
);

-- Enable Row Level Security
ALTER TABLE messages ENABLE ROW LEVEL SECURITY;

-- Policy: Allow anyone to insert messages (public contact form)
CREATE POLICY "Anyone can submit contact messages"
  ON messages
  FOR INSERT
  TO anon
  WITH CHECK (true);

-- Policy: Only authenticated users can read messages (admin dashboard)
CREATE POLICY "Only authenticated users can read messages"
  ON messages
  FOR SELECT
  TO authenticated
  USING (true);

-- Policy: Only authenticated users can update messages (mark as read/archived)
CREATE POLICY "Only authenticated users can update messages"
  ON messages
  FOR UPDATE
  TO authenticated
  USING (true);

-- Create index for faster queries
CREATE INDEX IF NOT EXISTS idx_messages_created_at ON messages(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_messages_status ON messages(status);

-- Comments for documentation
COMMENT ON TABLE messages IS 'Contact form submissions from the website';
COMMENT ON COLUMN messages.status IS 'Message status: unread (default), read, or archived';
