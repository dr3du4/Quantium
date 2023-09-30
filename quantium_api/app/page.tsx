import { Button,Image } from 'react-bootstrap'
import { Dropdown,Toggle,Menu,Item } from './client_imports';
import styles from './page.module.css'
import Head from 'next/head';
import background from "/public/images/papaj.jpg";

export default function Home() {
  return(
    <div style= {{backgroundImage:"url(/quantium_api/public/images/test/papaj.jpg)"}}className={styles.header}>
      <Head>
        <title>Quantum Art</title>
      </Head>
      <header>
        <Image  className={styles.img} src="/logo.png" alt="Qiskit logo" width={250} height={250}/>
        <h1 className={styles.title}>Quantum Art page</h1>
      </header>
      <div className={styles.center}>
        <Image src="/images/test/foo.png" style={{width: '500px',height: '500px'}}/>
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
