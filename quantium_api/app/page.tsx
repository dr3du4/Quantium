import { Button,Image } from 'react-bootstrap'
import { Dropdown,Toggle,Menu,Item, Popup_win } from './client_imports';
import styles from './page.module.css'
import Head from 'next/head';
import background from "/public/images/papaj.jpg";
import React from 'react';
import Popup from 'reactjs-popup';
import 'reactjs-popup/dist/index.css';


export default function Home() {
  return(
    <div className={styles.header}>
      <Image src="/images/test/papaj.jpg" style={{position: 'absolute',width: '100%',height: '100%'}}/>
      <Head>
        <title className={styles.title}>Quantum Art</title>
      </Head>
      <Image  className={styles.img} src="/logo.png" alt="Qiskit logo" width={250} height={250}/>

      <header className={styles.title}>
        <h1 className={styles.title}>Quantum Art page</h1>
      </header>
      <div className={styles.center}>
        <Image src="/images/test/foo.png" style={{width: '400px',height: '400px', padding: '8px'}}/>
        <Image src="/images/test/foo.png" style={{width: '400px',height: '400px', padding: '8px'}}/>
        <Image src="/images/test/foo.png" style={{width: '400px',height: '400px', padding: '8px'}}/>
        <Image src="/images/test/foo.png" style={{width: '400px',height: '400px', padding: '8px'}}/>
      </div>
      <div className={styles.container1}>
        <button className={styles["button-78"]}>Create new Quantum art</button>    
      </div>
      <div className={styles.container2}>
        <select className={styles.select}>
          <option>1</option>
          <option>2</option>
          <option>3</option>
          <option>4</option>
        </select>
      </div>
    </div>
  )
}
