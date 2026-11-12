import VariantClient from "./VariantClient";

export function generateStaticParams() {
  return [{ id: "placeholder" }];
}

export default function VariantPage() {
  return <VariantClient />;
}
