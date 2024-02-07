import React from "react";
import Image from "next/image"
import AuthImage from "../../../public/Auth.svg"

const layout = ({ children }) => {
  return (
    <main className="w-full min-h-screen h-full">


      <section className="w-full h-full sm:flex grid justify-center bg-red-400">


        <div className="sm:w-3/5 w-full sm:rounded-r-[5%] rounded-b-[4%] sm:rounded-b-none bg-white h-full py-5 mb-5 sm:mb-0 sm:py-0">
          {children}
        </div>

        <div className=" sm:w-2/5 w-full min-h-screen items-center relative bg-red-400 z-30">
          {/* <p className="font-bold text-white">EDUPLY <span>"GET <br/>SERIOUS WITH YOUR LEARNING"</span></p> */}
          <Image
            src={AuthImage}
            className="w-4/5 mx-auto sm:mx-0 sm:absolute sm:bottom-[20%] sm:right-[35%] block z-20"
            alt="Authentication illustration"
          />
          <p className="rounded-full shadow-2xl shadow-stone-500 drop-shadow-2xl border-none  w-60 opacity-15 bg-stone-500 h-60 absolute bottom-0 right-0"></p>
        </div>
        
      </section>


    </main>
  );
};

export default layout;
