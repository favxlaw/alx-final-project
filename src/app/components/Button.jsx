import React from 'react'

const Button = ({title, className, type, icon}) => {
    const style = `px-3 py-1 font-bold rounded-md + ${className}`
  return (
    <button type={type || 'button' } className={style}><span>{icon ? icon : ""}</span>{title}</button>)
}

export default Button