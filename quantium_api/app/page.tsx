import Image from 'next/image'
import { Button,Dropdown } from 'react-bootstrap'
import styles from './page.module.css'
import Head from 'next/head';

export default function Home() {
  return(
    <div className={styles.header}>
      <Head>
        <title>Quantum Art</title>
      </Head>
      <header>
        <Image  className={styles.img} src="/logo.png" alt="Qiskit logo" width={250} height={250}/>
        <h1 className={styles.title}>Quantum Art page</h1>
      </header>
        <div className={styles.container}>        
          <Button className={styles["button-78"]}>Create new Quantum art</Button>
          <Button className={styles["button-78"]}>EO</Button>
        </div>
    </div>
  )
}
