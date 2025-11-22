/**
 * Supabase Client Configuration
 * Replace these with your actual Supabase credentials from your project dashboard
 */

// TODO: Replace with your actual Supabase URL and Anon Key
const SUPABASE_URL = 'https://bgjohquanepghmlmdiyd.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJnam9ocXVhbmVwZ2htbG1kaXlkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjM2ODI3ODIsImV4cCI6MjA3OTI1ODc4Mn0.O1II649nWTZLgChPDOhITaBd3CJaALE2DZ-otzqG4N8';

// Initialize Supabase client
const supabaseClient = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

console.log('✅ Supabase client initialized');
