import Image from 'next/image'
import { Button,Dropdown } from 'react-bootstrap'
import styles from './page.module.css'
import Head from 'next/head';

export default function Home() {
  return (
    <div>
      <Head>
        <title>Quantum Art </title>
      </Head>
      <main className={styles.main}>
        <h1>Quantum Art page</h1>
      </main>
        <div >
          <Button className={styles["button-78"]}>Create new Quantum art</Button>
          <Button className={styles["button-78"]}>EO</Button>
        </div>      
    </div>
  )
}
