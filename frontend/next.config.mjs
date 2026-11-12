/** @type {import('next').NextConfig} */
const isStaticExport = process.env.EXPORT_STATIC === "1";

const nextConfig = isStaticExport
  ? {
      output: "export",
      trailingSlash: true,
      images: { unoptimized: true },
    }
  : {
      async rewrites() {
        const backendUrl = process.env.BACKEND_API_URL || "https://kronikoto.onrender.com";
        return [
          {
            source: "/api/v1/:path*",
            destination: `${backendUrl}/api/v1/:path*`,
          },
        ];
      },
    };

export default nextConfig;
