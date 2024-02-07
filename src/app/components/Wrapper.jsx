"use client"

import React from 'react'
import { usePathname } from 'next/navigation'

const Wrapper = ({children}) => {

    const path = usePathname()
  return (
    <div className={`${path === "/auth/signup" || "/auth/signin" ? "bg-red-400 sm:bg-white" : "bg-white"}`}>{children}</div>
  )
}

export default Wrapper