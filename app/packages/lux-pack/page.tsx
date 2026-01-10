import GalleryGrid from '@/components/gallery/GalleryGrid';

export default function LuxPackPage() {
    return (
        <main className="container mx-auto px-4 py-8">
            <h1 className="text-3xl font-bold mb-4">Lux Pack</h1>
            <div className="mb-8">
                <p>The ultimate luxury experience in the Agafay Desert.</p>
            </div>

            <section className="my-12">
                <GalleryGrid category="lux-pack" />
            </section>

            <div className="bg-gray-100 p-6 rounded-lg mt-8">
                <h2 className="text-xl font-bold mb-4">Book Now</h2>
                <p>Booking form placeholder.</p>
            </div>
        </main>
    );
}
