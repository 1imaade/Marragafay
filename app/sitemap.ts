import { MetadataRoute } from 'next'
import { createClient } from '@supabase/supabase-js'

// Initialize Supabase client
// Ensure you have these environment variables set in your .env.local file
const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL || ''
const supabaseKey = process.env.SUPABASE_SERVICE_ROLE_KEY || process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY || ''
const supabase = createClient(supabaseUrl, supabaseKey)

// Helper to slugify text (e.g., "Agafay Desert" -> "agafay-desert")
const slugify = (text: string) => {
    return text
        .toString()
        .toLowerCase()
        .trim()
        .replace(/\s+/g, '-')     // Replace spaces with -
        .replace(/[^\w\-]+/g, '') // Remove all non-word chars
        .replace(/\-\-+/g, '-')   // Replace multiple - with single -
}

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
    const baseUrl = 'https://marragafay.com'

    // 1. Define Static Routes
    const routes = [
        '',
        '/about',
        '/contact',
        '/bookings',
        '/activities',
        '/packs',
        '/reviews',
    ].map((route) => ({
        url: `${baseUrl}${route}`,
        lastModified: new Date(),
        changeFrequency: 'daily' as const,
        priority: route === '' ? 1.0 : 0.8,
    }))

    // 2. Fetch Dynamic Routes from Supabase (Pricing Table for Activities/Packages)
    let dynamicRoutes: MetadataRoute.Sitemap = []

    try {
        const { data: pricingItems, error } = await supabase
            .from('pricing')
            .select('item_type, item_name, updated_at')
            .eq('active', true)

        if (error) {
            console.error('Error fetching sitemap data from Supabase:', error)
        } else if (pricingItems) {
            dynamicRoutes = pricingItems.map((item) => {
                // Map 'package' -> 'packages' and 'activity' -> 'activities' for the URL structure
                const folder = item.item_type === 'package' ? 'packages' : 'activities'
                const slug = slugify(item.item_name)

                return {
                    url: `${baseUrl}/${folder}/${slug}`,
                    lastModified: item.updated_at ? new Date(item.updated_at) : new Date(),
                    changeFrequency: 'weekly' as const,
                    priority: 0.9, // High priority for product pages
                }
            })
        }
    } catch (err) {
        console.error('Unexpected error generating sitemap:', err)
    }

    // 3. (Optional) Fetch Blog Posts if you have a blog table
    // const { data: posts } = await supabase.from('posts').select('slug, updated_at')
    // ... map logic ...

    return [...routes, ...dynamicRoutes]
}
