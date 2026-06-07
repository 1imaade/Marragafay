import React from 'react';
import Head from 'next/head';
import Layout from '../../components/Layout';
import { useRouter } from 'next/router';

export default function CategoryPage() {
  const router = useRouter();
  const { category } = router.query;

  return (
    <Layout>
      <Head>
        <title>{category ? `${category} | Marragafay Journal` : 'Marragafay Journal Categories'}</title>
      </Head>
      <div className="w-full bg-[#F6F7EA] min-h-screen py-32 px-6">
        <div className="max-w-7xl mx-auto">
          <h1 className="text-4xl font-bold uppercase mb-8 text-[#10100E]" style={{ fontFamily: '"Clash Grotesk", sans-serif' }}>
            Category: {category}
          </h1>
          <p className="text-lg text-[#272724]/80">
            This is a placeholder for the filtered category view.
          </p>
        </div>
      </div>
    </Layout>
  );
}
