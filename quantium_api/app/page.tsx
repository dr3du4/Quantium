import { Button,Image } from 'react-bootstrap'
import { Dropdown,Toggle,Menu,Item } from './client_imports';
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
      <div className={styles.center}>
        <Image src="/images/test/foo.png" style={{width: '500px',height: '500px'}}/>
      </div>
        <div className={styles.container}>        
          <button className={styles["button-78"]}>Create new Quantum art</button>
          <button className={styles["button-78"]}>EO</button>
          <Dropdown>
            <Toggle variant="success" id="dropdown-basic">
              Dropdown Button
            </Toggle>

            <Menu>
              <Item href="#/action-1">Action</Item>
              <Item href="#/action-2">Another action</Item>
              <Item href="#/action-3">Something else</Item>
            </Menu>
          </Dropdown>
        </div>
    </div>
  )
}
