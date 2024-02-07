import React from 'react'
import Image from "next/image"

const Course = ({image, title, content, className}) => {
    // const style  = ``
  return (
    <div className=''>
        <Image src={image} alt='Course image' className=''/>
        <div className=''>
            <p className='font-bold'>{title}</p>
            <p className=''>{content}</p>
        </div>
    </div>
  )
}

export default Course