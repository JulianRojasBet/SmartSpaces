import { Inter } from "next/font/google";
import { ImproveForm } from "./components/ImproveForm";
import styles from "./styles.module.css";

const inter = Inter({ subsets: ["latin"] });

export default function Home() {
  return (
    <>
      <div className="w-full h-screen bg-[url('https://cdn.discordapp.com/attachments/1096802045828280442/1096885104862834858/Snorku_interior_design_background_with_fluid_patters_using_purp_6fcdf147-180b-4398-95ac-863d11596330.png')] bg-cover bg-center">
        <div className="w-full h-full backdrop-blur-xl">

          <main
            className={`${inter.className} max-w-2xl mx-auto h-screen flex flex-col justify-center items-center`}
          >
            <ImproveForm />
          </main>
        </div>
      </div>
    </>
  );
}
