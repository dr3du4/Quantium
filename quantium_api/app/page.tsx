"use client"
import { Button,Image } from 'react-bootstrap'
import {useState,useEffect} from "react"
import { Dropdown,Toggle,Menu,Item,Spinner } from './client_imports';
import styles from './page.module.css'
import Head from 'next/head';
import background from "/public/images/papaj.jpg";
import { atom,useAtom } from 'jotai';
import axios from "axios"
const stateAtom = atom({
  chartView: false,
  charts: "iss", 
  loading: false,
  name: "",
  bubbles: false
});

export default function Home() {
  const [state,setState] = useAtom(stateAtom);

  // useEffect(()=>{
  //   const name = window.prompt("What's your name?","");
  //   if(name){
  //     setState((prevState)=>{
  //       return {
  //         ...prevState,
  //         name: name
  //       }
  //     })
  //   }
  //   console.log(name);
  // },[]);

  const onChangeInput = (event:  React.ChangeEvent<HTMLInputElement>)=>{
    setState((prevState)=>{
      return {
        ...prevState,
        name: event.target.value
      }
    }); 
  }

  const onClickButton =async ()=>{
    try {
      setState((prevState)=>{
        return {
          ...prevState,
          loading: true
        }
      }); 
      const res = await axios.get(`/api/${state.charts}`,{headers: {
        "Content-Type": "application/json"
      }});
      setState((prevState)=>{
        return {
          ...prevState,
          loading: false, 
          chartView: true
        }
      }); 
    }
    catch(err){
      console.log(err)
    }
  }

  const generateBubbleTheme = async()=>{
    setState((prevState)=>{ 
      return {
        ...prevState,
        loading: true
      }
    });
    await axios.get("/api/bubble",{
      headers: {
        "Content-Type": "application/json"
      }
    });
    setState((prevState)=>{ 
      return { 
        ...prevState,
        bubbles: true,
        loading: false
      }
    }); 
  };


  const onSelect = async(event:  React.ChangeEvent<HTMLSelectElement>)=>{
    setState((prevState)=>{
      return {
        ...prevState,
        charts: event.target.value
      }
    });
  }

  return(
    <div className={styles.header}>
      <Image src={state.bubbles ? "/bubbles.png" : "/white.jpg"} style={{position: 'absolute',width: '100%',height: '125%'}}/>
      <Head>
        <title className={styles.title}>Quantum Art</title>
      </Head>
      <Image  className={styles.img} src="/logo.png" alt="Qiskit logo" width={250} height={250}/>

      <header className={styles.title}>
        <h1 className={styles.title}>Quantum Art page</h1>
      </header>
      <div style={{marginTop: '200px'}} className={styles.center}>
        {state.chartView ?      
         <div >
         <Image src={`/charts/${state.charts}/EfficientSU2.png`} style={{width: '500px',height: '500px', padding: '8px'}}/>
        <Image src={`/charts/${state.charts}/seeborn.png`} style={{width: '500px',height: '500px', padding: '8px'}}/>

        <div>
        <Image src={`/charts/${state.charts}/circuit20.png`} style={{width: '300px',height: '300px', padding: '8px'}}/>
        <Image src={`/charts/${state.charts}/circuit28.png`} style={{width: '600px',height: '300px', padding: '8px'}}/>
        {/* <Image src={`/charts/${state.charts}/secondCircuit.png`} style={{width: '300px',height: '300px', padding: '8px'}}/> */}
        <Image src={`/charts/${state.charts}/reduceML.png`} style={{width: '300px',height: '300px', padding: '8px'}}/>

        </div>
        </div>

        : <>{state.loading ? <Spinner style={{width: '100px',height: '100px'}} animation="border"/> : null }</>}
      {
        state.bubbles ? 
        <>        <div className={styles.container1}>
        <button className={styles["button-78"]} onClick={onClickButton}>Create new Quantum art</button>    
      </div>
      <div className={styles.container2}>
        <p>Choose Dataset</p>
        <select onChange={onSelect} value={state.charts} className={styles.select}>
          <option value={"iss"}>Iss</option>
          <option value={"nasa"}>Nasa</option>
          <option value={"iris"}>Iris</option>
        </select>
      </div></> : 
      <div className={styles.center}>
        <h2>Pass Your Name</h2>
        <input value={state.name} onChange={onChangeInput}/>
        <button onClick={async()=>{
          await generateBubbleTheme()
        }}>Submit</button>
      </div>
      }

      </div>

    </div>
  )
}
