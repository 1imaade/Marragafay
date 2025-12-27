import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
    metadataBase: new URL('https://marragafay.com'),
    title: {
        default: 'Marragafay | Agafay Desert Luxury Tours & Camps',
        template: '%s | Marragafay'
    },
    description: 'Experience the magic of Agafay Desert with Marragafay. Book luxury camps, camel rides, quad biking, and desert dinners from Marrakech. Unforgettable adventures await.',
    keywords: ['Agafay Desert', 'Marrakech Excursions', 'Marragafay', 'Desert Dinner', 'Quad Biking', 'Morocco Travel', 'Luxury Desert Camp'],
    openGraph: {
        title: 'Marragafay | Agafay Desert Luxury Tours & Camps',
        description: 'Experience the magic of Agafay Desert with Marragafay. Book luxury camps, camel rides, quad biking, and desert dinners from Marrakech.',
        url: 'https://marragafay.com',
        siteName: 'Marragafay',
        images: [
            {
                url: '/images/og-image.jpg', // You should ensure this image exists in your public folder
                width: 1200,
                height: 630,
                alt: 'Marragafay Desert Experience',
            },
        ],
        locale: 'en_US',
        type: 'website',
    },
    twitter: {
        card: 'summary_large_image',
        title: 'Marragafay | Agafay Desert Luxury Tours & Camps',
        description: 'Experience the magic of Agafay Desert with Marragafay. Book luxury camps, camel rides, quad biking, and desert dinners from Marrakech.',
        images: ['/images/twitter-image.jpg'], // You should ensure this image exists
        creator: '@marragafay', // Assuming handle
    },
    viewport: {
        width: 'device-width',
        initialScale: 1,
        maximumScale: 1,
    },
    robots: {
        index: true,
        follow: true,
        googleBot: {
            index: true,
            follow: true,
            'max-video-preview': -1,
            'max-image-preview': 'large',
            'max-snippet': -1,
        },
    },
    verification: {
        google: 'bamVos41fgswgcgtQoBGzbYihLKMpzhQOS7PiAlnm-M',
    },
}

export default function RootLayout({
    children,
}: {
    children: React.ReactNode
}) {
    return (
        <html lang="en">
            <body className={inter.className}>{children}</body>
        </html>
    )
}
