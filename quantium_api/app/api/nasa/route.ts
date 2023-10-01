import type { NextApiRequest, NextApiResponse } from "next";
import { NextResponse } from "next/server";
import { cmd } from "@/app/utils/cmd";

const path_to_script = "./scripts/ml_script.py";

export async function GET(
    req: NextApiRequest,
    res: NextApiResponse
){
  await cmd(["python3", path_to_script, "nasa"]);
  return NextResponse.json({ 
    message: "Succesfully executed script nasa"
  }); 
}