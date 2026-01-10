import GalleryGrid from '@/components/gallery/GalleryGrid';

export default function DinnerShowPage() {
    return (
        <main className="container mx-auto px-4 py-8">
            <h1 className="text-3xl font-bold mb-4">Dinner & Show</h1>
            <div className="mb-8">
                <p>A magical evening of gastronomy and entertainment under the stars.</p>
            </div>

            <section className="my-12">
                <GalleryGrid category="dinner-show" />
            </section>

            <div className="bg-gray-100 p-6 rounded-lg mt-8">
                <h2 className="text-xl font-bold mb-4">Book Now</h2>
                <p>Booking form placeholder.</p>
            </div>
        </main>
    );
}
