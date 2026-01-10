import GalleryGrid from '@/components/gallery/GalleryGrid';

export default function CamelRidePage() {
    return (
        <main className="container mx-auto px-4 py-8">
            <h1 className="text-3xl font-bold mb-4">Camel Ride</h1>
            <div className="mb-8">
                <p>Traditional camel trekking experience at sunset.</p>
            </div>

            <section className="my-12">
                {/* 'camel' matches the folder name in public/gallery-pages found by the script */}
                <GalleryGrid category="camel" />
            </section>

            <div className="bg-gray-100 p-6 rounded-lg mt-8">
                <h2 className="text-xl font-bold mb-4">Book Now</h2>
                <p>Booking form placeholder.</p>
            </div>
        </main>
    );
}
