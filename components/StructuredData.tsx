import Script from 'next/script'

export default function StructuredData() {
    const jsonLd = {
        '@context': 'https://schema.org',
        '@type': 'TravelAgency',
        name: 'Marragafay',
        image: 'https://www.canva.com/create/logos/', // Used as requested, consider replacing with actual logo URL
        description: 'Luxury tours and camps in Agafay Desert.',
        address: {
            '@type': 'PostalAddress',
            addressLocality: 'Marrakech',
            addressCountry: 'MA',
        },
        priceRange: '$$',
        telephone: '+212672-531624', // Extracted from index.html
        url: 'https://marragafay.com',
    }

    return (
        <script
            type="application/ld+json"
            dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
        />
    )
}
