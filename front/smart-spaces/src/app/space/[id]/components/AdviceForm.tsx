"use client";

import { useState } from "react";
import Image from "next/image";
import { Button } from "@/components/Button";
import { Modal } from "@/components/Modal";
import { Select } from "@/components/Select";
import { PlaceImage } from "@/app/components/types";
import { ImageList } from "./ImageList";

type AdviceFormProps = {
  improved: PlaceImage;
};

export function AdviceForm({ improved }: AdviceFormProps) {
  const modalId = "preview-modal";
  const improveModalId = "improve-modal-id";
  const emptyImage = { id: "", url: "" };
  const images = [
    { id: "image1", url: "https://via.placeholder.com/200x200" },
    { id: "image2", url: "https://via.placeholder.com/200x200" },
    { id: "image3", url: "https://via.placeholder.com/200x200" },
    { id: "image4", url: "https://via.placeholder.com/200x200" },
  ];
  const options = [{ value: "living-room", label: "Living room" }];

  const [selected, setSelected] = useState<PlaceImage>(emptyImage);

  const handleSelect = (id: string) => {
    const image = images.find((image) => image.id === id) || emptyImage;
    setSelected(image);
  };

  const handleClose = () => {
    setSelected(emptyImage)
  }

  return (
    <div className="flex flex-col max-w-2xl mx-auto">
      <h2 className="text-4xl font-bold text-center mb-10">
        Improve you space by room
      </h2>
      <div className="flex flex-row justify-center mb-8">
        <Select
          initial="Select an option"
          options={options}
          onSelect={() => {}}
        />
        <Button>Some CTA</Button>
      </div>
      <div>
        <h3 className="text-xl mb-2 font-bold">
          Advices based on your guests comments
        </h3>
        <ul className="max-w-2xl divide-y rounded-lg">
          <li className="p-4 hover:cursor-pointer hover:bg-slate-100 flex flex-row items-center">
            <p>
              Use light-colored window treatments: Dark window treatments can
              absorb heat and make the room hotter. Instead, opt for
              light-colored curtains or blinds that will reflect heat and keep
              the room cooler.
            </p>
            <a href={`#${modalId}`} className="btn btn-secondary ml-2">
              Preview
            </a>
          </li>
          <li className="p-4 hover:cursor-pointer hover:bg-slate-100 flex flex-row items-center">
            <p>
              Use reflective window film: You can also apply reflective window
              film to the windows to help block out the sun`s heat and keep the
              room cooler.
            </p>
            <a href={`#${modalId}`} className="btn btn-secondary ml-2">
              Preview
            </a>
          </li>
          <li className="p-4 hover:cursor-pointer hover:bg-slate-100 flex flex-row items-center">
            <p>
              Install a ceiling fan: A ceiling fan can help circulate the air in
              the room and provide a cooling breeze.
            </p>
            <a href={`#${modalId}`} className="btn btn-secondary ml-2">
              Preview
            </a>
          </li>
          <li className="p-4 hover:cursor-pointer hover:bg-slate-100 flex flex-row items-center">
            <p>
              Use a portable air conditioner: If you are unable to install a
              central air conditioning unit, consider using a portable air
              conditioner to help cool down the room.
            </p>
            <a href={`#${modalId}`} className="btn btn-secondary ml-2">
              Preview
            </a>
          </li>
          <li className="p-4 hover:cursor-pointer hover:bg-slate-100 flex flex-row items-center">
            <p>
              Keep windows and doors closed during the hottest parts of the day:
              To prevent hot air from entering the room, keep windows and doors
              closed during the hottest parts of the day. Open them up in the
              evenings when it`s cooler outside.
            </p>
            <a href={`#${modalId}`} className="btn btn-secondary ml-2">
              Preview
            </a>
          </li>
        </ul>
      </div>
      <Modal id={modalId}>
        <h3 className="font-bold text-lg mb-4">
          Select the image where you want to apply the advice
        </h3>
        <ImageList
          selected={selected}
          images={images}
          onSelect={handleSelect}
        />
        <div className="modal-action">
          <a
            href={`#${improveModalId}`}
            className={`btn btn-primary ${!selected.id ? "btn-disabled" : ""}`}
          >
            Select
          </a>
          <a href="#" className="btn btn-secondary" onClick={handleClose}>
            Close
          </a>
        </div>
      </Modal>
      <Modal id={improveModalId}>
        <h3 className="font-bold text-lg mb-4">
          This is how your space could look like
        </h3>
        <div className="flex flex-row justify-between">
          <div className="min-w-[400px] min-h-[400px] relative m-2">
            <Image
              src={selected.url}
              alt={selected.id}
              fill
              className="rounded-lg"
            />
          </div>
          <div className="min-w-[400px] min-h-[400px] relative m-2">
            <Image
              src={improved.url}
              alt={improved.id}
              fill
              className="rounded-lg"
            />
          </div>
        </div>
        <div className="modal-action">
          <a href="#" className="btn btn-secondary" onClick={handleClose}>
            Close
          </a>
        </div>
      </Modal>
    </div>
  );
}
