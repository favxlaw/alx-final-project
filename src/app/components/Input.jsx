"use client";

import { useState, useEffect } from "react";
import { GrView } from "react-icons/gr";
import { GrHide } from "react-icons/gr";
import { GrSearch } from "react-icons/gr";
import React from "react";
import Link from "next/link";

export const Password = ({
  title,
  placeholder,
  register,
  error,
  required,
  name,
  classname,
}) => {
  const For = title?.toLowerCase().split("").join("");

  const [show, setShow] = useState(false);


 const style = ` block px-5 pb-2.5 pt-4 w-full text-sm placeholder:text-sm text-gray-900 bg-transparent rounded-lg border-1 border-gray-700 appearance-none dark:text-gray-900 dark:border-gray-600 hover:border-blue-800 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer peer-focus:placeholder-opacity-0 + ${classname}`;

  const showPassword = () => {
    setShow((prev) => !show);
  };
  return (
    <div className="w-full relative">
      <div className="relative w-full">
        <input
          type={show ? "text" : "password"}
          name={For}
          {...register(name, {
            required: true,
            validate: {
              checkLength: (value) => value.length >= 8,
              matchPattern: (value) =>
                /(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$*])/.test(value),
            },
          })}
          id={For}
          className={style}
          placeholder={placeholder}
        />
        <span
          onClick={showPassword}
          className="inline-flex absolute h-3/4 my-auto mr-1 inset-y-0 right-0 items-center px-3 text-sm text-gray-900 dark:text-gray-400 dark:border-gray-600"
        >
          {show ? <GrHide size="20" /> : <GrView size="20" />}
        </span>
        <label
          htmlFor={For}
          className="absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-transparent dark:bg-gray-900 px-3 peer-focus:px-4 peer-focus:text-gray-600 bg-white rounded peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:placeholder:text-white peer-focus:top-2 peer-focus:scale-100 peer-focus:-translate-y-4 left-4 peer-focus:placeholder-opacity-0"
        >
          {title}
        </label>
      </div>
      <p className="text-gray-400 font-bold text-sm mt-1">
        Minimum of 8 characters.
      </p>
      {error[name] && error[name].type === "required" && (
        <p className="text-sm text-red-600 font-bold text-left">
          Password is required
        </p>
      )}
      {error[name] && error[name].type === "checkLength" && (
        <p className="text-sm text-red-600 font-bold text-left">
          Password is must be up to eight characters
        </p>
      )}
      {error[name] && error[name].type === "matchPattern" && (
        <p className="text-sm text-red-600 font-bold text-left">
          Password is must be contain at least a number, symbol, uppercase
          letter and lowercase letter
        </p>
      )}
    </div>
  );
};

export const PasswordLogin = ({
  title,
  placeholder,
  error,
  register,
  name,
  classname,
}) => {

  const For = title?.toLowerCase().split("").join("");

   const style = ` block px-5 pb-2.5 pt-4 w-full text-sm placeholder:text-sm text-gray-900 bg-transparent rounded-lg border-1 border-gray-700 appearance-none dark:text-gray-900 dark:border-gray-600 hover:border-blue-800 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer + ${classname}`;

  const [show, setShow] = useState(false);

  const showPassword = () => {
    setShow((prev) => !show);
  };
  return (
    <div className="w-full grid relative">
      <div className="relative w-full">
        <input
          type={show ? "text" : "password"}
          name={For}
          {...register(name, {
            required: true,
            validate: {
              checkLength: (value) => value.length >= 8,
              matchPattern: (value) =>
                /(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$*])/.test(value),
            },
          })}
          id={For}
          className={style}
          placeholder={placeholder}
        />
        <span onClick={showPassword} className="absolute right-2 bottom-3">
          {show ? <GrHide size="20" /> : <GrView size="20" />}
        </span>
      </div>
      {error[name] && error[name].type === "required" && (
        <p className="text-sm text-red-600 font-bold text-left">
          Password is required
        </p>
      )}
      {error[name] && error[name].type === "checkLength" && (
        <p className="text-sm text-red-600 font-bold text-left">
          Password is must be up to eight characters
        </p>
      )}
      {error[name] && error[name].type === "matchPattern" && (
        <p className="text-sm text-red-600 font-bold text-left">
          Password is must be contain at least a number, symbol, uppercase
          letter and lowercase letter
        </p>
      )}
      <Link href="/forgot-password">
        <p className="text-black font-bold text-sm text-right mt-1">
          Forgot Password?
        </p>
      </Link>

      <label
        htmlFor={For}
        className="absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-transparent dark:bg-gray-900 px-3 peer-focus:px-4 peer-focus:text-gray-600 bg-white rounded peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:placeholder:text-white peer-focus:top-2 peer-focus:scale-100 peer-focus:-translate-y-4 left-4"
      >
        {title}
      </label>
    </div>
  );
};

export const Text = ({
  title,
  type,
  placeholder,
  register,
  error,
  name,
  required,
  classname,
}) => {


  const style = ` block px-5 pb-2.5 pt-4 w-full text-sm placeholder:text-sm text-gray-900 bg-transparent rounded-lg border-1 border-gray-700 appearance-none dark:text-gray-900 dark:border-gray-600 hover:border-blue-800 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer + ${classname}`;


  return (
    <div className="relative w-full">

    <div className="w-full relative">
      <input
        type={type || "text"}
        {...register(name, { required: true })}
        name={name}
        id={name}
        className={style}
        placeholder={placeholder}
      />
      <label
        htmlFor={name}
        className="absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-transparent dark:bg-gray-900 px-3 peer-focus:px-4 peer-focus:text-gray-600 bg-white rounded peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:placeholder:text-white peer-focus:top-2 peer-focus:scale-100 peer-focus:-translate-y-4 left-4"
      >
        {title}
      </label>
      </div>
      {error[name] && error[name].type === "required" && (
        <p className="text-sm text-red-600 font-bold text-left">{`${name} is required.`}</p>
      )}
</div>
  );
};

export const Search = ({
  title,
  type,
  placeholder,
  register,
  error,
  name,
  required,
  className,
}) => {
  const classes = `${className} + rounded placeholder:text-sm placeholder:font-regular font-regular text-slate-600 w-full text-sm border-black border-[1px] py-[7px] pl-9 pr-4`;
  return (
    <div className="w-full relative items-center flex gap-10">
      <div className="absolute left-2">
        <GrSearch />
      </div>
      <input
        type={type || "text"}
        {...register(name)}
        name={name}
        id={name}
        className={classes}
        placeholder={placeholder}
      />

      {/* {error[name] && error[name].type === "required" && (
        <p className="text-sm text-red-600 font-bold text-left">{`${title} is required.`}</p>
      )} */}
    </div>
  );
};

export const Select = ({
  title,
  register,
  error,
  classname,
  children,
  name,
  onclick,
}) => {
   const style = ` px-2.5 pb-2.5 pt-2.5 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 border-gray-700 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-gray-500 focus:outline-none focus:ring-0 focus:border-none peer + ${classname}`;

  return (
    <div className="w-full">
      <label 
        htmlFor={name}
        className="absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-transparent dark:bg-gray-900 px-2 peer-focus:px-2 peer-focus:text-gray-600 bg-white rounded peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-100 peer-focus:-translate-y-4 left-1"
      >
        {title}
        <select
          name={name}
          id={name}
          {...register(name, { required: true })}
          className={style}
        >
          <option value="">Select role:</option>
          <option value="ADMIN">Admin</option>
          <option value="MEMBER">Team Member</option>
          <option value="MANAGER">Project Manager</option>
        </select>
      </label>
      <p
        className="font-black text-blue-500 text-sm cursor-pointer mt-1"
        onClick={() => onclick()}
      >
        {children}
      </p>
      {error[name] && error[name].type === "required" && (
        <p className="text-sm text-red-600 font-bold">{`${name} is required.`}</p>
      )}
    </div>
  );
};
