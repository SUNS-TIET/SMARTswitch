import React from "react";

const Tab=(props)=>{
    return(
        <div className={`text-center ${props.color} p-5 w-80 space-y-3 mx-5`}>
            
            <div className=" font-bold text-white text-xl">{props.title}</div>
            <div className=" text-white text-lg">{props.value}</div>
            <div className="padding"></div>
        </div>
    )
}

export default Tab