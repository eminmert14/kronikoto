import ModelClient from "./ModelClient";

export function generateStaticParams() {
  return [{ id: "placeholder" }];
}

export default function ModelPage() {
  return <ModelClient />;
}
