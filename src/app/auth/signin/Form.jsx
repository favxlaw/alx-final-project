"use client";

import React from "react";
import Link from "next/link";
import { useForm } from "react-hook-form";
import { Text, Password } from "@/app/components/Input";
import Button from "@/app/components/Button";
import api from "@/app/axios";

const Form = () => {
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm({ reValidateMode: "onChange" });

  const Submit = async (data) => {
    const response = await api.post(
      "https://lms-api-6k50.onrender.com/signin",
      data,
      {
        headers: {
          "Content-Type": "application/json",
        },
      }
    );
    const result = response.json();
    console.log(data);
    console.log(result);
  };

  return (
    <div className="sm:rounded-r-[5%] rounded-b-[5%] sm:mb-0 sm:rounded-b-none min-h-screen w-5/6 pl-0 sm:pl-6 my-auto mx-auto sm:mx-0 flex flex-col justify-center h-ful">
      <div className="h-[80%] w-full">
        <h1 className="text-3xl font-bold tracking-wide my-2">Log In</h1>
        <p>Log in to continue smooth and seamless learning</p>

        {/* START OF FORM */}

        <form onSubmit={handleSubmit(Submit)}>
          {/* FORM CONTENT */}

          <div className="grid my-5 gap-3">
            {/* <div className="grid gap-5">
              <Text
                placeholder="Full Name"
                title="Full Name"
                name="Name"
                className=""
                type="text"
                required
                register={register}
                error={errors}
              />
            </div> */}
            <div className="grid gap-3">
              <Text
                title="Email Address"
                placeholder="Email Address"
                name="email"
                classname=""
                type="email"
                required
                register={register}
                error={errors}
              />
              <Password
                title="Password"
                placeholder="Password"
                name="password"
                className=""
                type="Password"
                required
                register={register}
                error={errors}
              />
            </div>
          </div>
          {/* END OF FORM CONTENT */}

          <div className="sm:flex grid gap-3 sm:gap-0 items-center sm:justify-between justify-center text-center mb-3 sm:mb-0">
            <p className="text-sm flex gap-3">
              Don't have an account?
              <Link href="/auth/signup" className="underline">
                Sign up here
              </Link>
            </p>
            <Button
              title="Login"
              className="text-white bg-green-400 border border-white py-2 px-6 sm:px-4 rounded-md sm:w-1/3 w-full"
              type="submit"
            />
          </div>
        </form>

        {/* END OF FORM */}
      </div>
    </div>
  );
};

export default Form;
