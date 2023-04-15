import Image from "next/image";

type ImageListProps = {
  images: {
    id: string;
    url: string;
  }[];
};

export function ImageList({ images }: ImageListProps) {
  return (
    <div className="flex flex-row flex-wrap justify-center">
      {images.map(({ id, url }) => (
        <div key={id} className="min-w-[200px] min-h-[200px] relative flex-grow-0 m-2">
          <Image src={url} alt={id} fill />
        </div>
      ))}
    </div>
  );
}
