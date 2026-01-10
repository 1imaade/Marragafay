'use client';

import Image from 'next/image';
import { GALLERY_DATA } from '@/lib/gallery-data';

interface GalleryGridProps {
    category: string;
}

export default function GalleryGrid({ category }: GalleryGridProps) {
    const images = GALLERY_DATA[category];

    if (!images || images.length === 0) {
        console.warn(`No images found for category: ${category}`);
        return null;
    }

    return (
        <div className="w-full">
            <h3 className="text-2xl font-bold mb-6 text-brand-dark">Photo Gallery</h3>
            <div className="columns-1 md:columns-2 lg:columns-3 gap-4 space-y-4">
                {images.map((src, index) => (
                    <div key={index} className="break-inside-avoid relative w-full rounded-xl overflow-hidden shadow-sm hover:shadow-md transition-all duration-300 group">
                        <Image
                            src={src}
                            alt={`${category} gallery image ${index + 1}`}
                            width={600}
                            height={400} // Aspect ratio approximation, object-cover handles the rest
                            className="w-full h-auto object-cover transform group-hover:scale-105 transition-transform duration-500"
                            sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
                        />
                    </div>
                ))}
            </div>
        </div>
    );
}
