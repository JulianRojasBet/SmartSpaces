import { PlaceImage } from "@/app/components/types";
import Image from "next/image";

type ImageListProps = {
  selected: PlaceImage;
  images: PlaceImage[];
  onSelect: (id: string) => void
};

export function ImageList({ selected, images, onSelect }: ImageListProps) {
  

  const getBorder = (id: string) => {
    return selected.id === id ? "border-primary" : "border-transparent";
  };

  return (
    <div className="flex flex-row flex-wrap justify-center">
      {images.map(({ id, url }) => (
        <div
          key={id}
          className={`min-w-[200px] min-h-[200px] relative flex-grow-0 m-2 hover:scale-105 transition-all cursor-pointer rounded-lg border-2 ${getBorder(id)}`}
          onClick={() => onSelect(id)}
        >
          <Image src={url} alt={id} fill className="rounded-lg" />
        </div>
      ))}
    </div>
  );
}
