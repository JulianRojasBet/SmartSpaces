import Image from "next/image";
import { Inter } from "next/font/google";
import { AdviceForm } from "./components/AdviceForm";

const inter = Inter({ subsets: ["latin"] });

export default function PostHome() {
  return (
    <main
      className={`${inter.className} max-w-4xl mx-auto h-screen flex flex-col items-center`}
    >
      <div className="flex flex-row justify-center items-center h-[400px] my-10">
        <div className="min-w-[400px] min-h-[400px] relative">
          <Image
            src="https://via.placeholder.com/500x400"
            alt="Post image"
            fill
          />
        </div>
        <div className="my-2 mx-4">
          <h3 className="text-xl mb-2 font-bold pb-4">
            Cabaña colibri en Santa Elena
          </h3>
          <p>
            Welcome to our beautiful and cozy apartment in the heart of the
            city! Our apartment is the perfect choice for travelers looking for
            a comfortable and convenient home away from home.
          </p>
          <br />
          <p>
            The apartment features a spacious bedroom with a comfortable
            queen-sized bed, a fully-equipped kitchen with everything you need
            to prepare your meals, a cozy living room with a flat-screen TV, and
            a modern bathroom with a shower.
          </p>
        </div>
      </div>
      <div className="border-t border-primary w-full py-10">
        <div className="">
          <AdviceForm />
        </div>
      </div>
    </main>
  );
}
