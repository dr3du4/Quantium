import {spawn} from "child_process";

export const cmd = (command: string[])=>{
    let p = spawn(command[0], command.slice(1));
    return new Promise((resolveFunc) => {
      p.stdout.on("data", (x) => {
        console.log(x.toString());
        process.stdout.write(x.toString()); 
      });
      p.stderr.on("data", (x) => {
        process.stderr.write(x.toString());
      });
      p.on("exit", (code) => {
        console.log(code);
        resolveFunc(code);
      });
    });
}