import React,{useState,useEffect} from "react";
import Tab from "./components/Tab";


// URL -> https://punjab-2022-default-rtdb.firebaseio.com/

// https://punjab-2022-default-rtdb.firebaseio.com/data.json

export default function(){
  
    const[state,setState]=useState();

    async function fetchData(){
      const data = await fetch("https://punjab-2022-default-rtdb.firebaseio.com/data.json");
      const json = await data.json();
      setState(json);
    }

    useEffect(()=>{
      fetchData()
    },[])

    const delay = ms => new Promise(
      resolve => setTimeout(resolve, ms)
    );

    const refreshPage = ()=>{
      window.location.reload();
   }

   

  return(
    <div>
      
      <div className="mt-6 mx-4 text-center">
        <h1 className="mb-4 text-4xl font-extrabold tracking-tight leading-none text-gray-900 md:text-5xl lg:text-6xl dark:text-black">Smart<span class="text-blue-600 dark:text-blue-500">Switch</span></h1>
        <p className="text-lg font-normal text-gray-500 lg:text-xl dark:text-gray-400">Status as on <span className="font-bold">{state?state.date:null}</span> {state?state.time:null}</p>
      </div>

      <div className="mt-6 mx-6 px-px flex flex-row flex-wrap items-center justify-center space-y-10 mb-6">
        <Tab color="bg-purple-600" title="Pump Status" value={state?state.pump:null}/>
        <Tab color="bg-emerald-500" title="Temperature" value={state?state.temp:null}/>
        <Tab color="bg-red-500" title="Humidity" value={state?state.humidity:null}/>
        <Tab color="bg-blue-500" title="Ground Water Level" value={state?state.water_l:null}/>
        <Tab color="bg-orange-500" title="Moisture" value={state?state.moisture:null}/>
        <Tab color="bg-yellow-500" title="Water Flow rate" value={state?state.flow:null}/>
      </div>

    </div>
  )

}