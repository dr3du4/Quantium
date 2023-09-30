import type { NextApiRequest, NextApiResponse } from "next";
import { NextResponse } from "next/server";
import { cmd } from "@/app/utils/cmd";

const path_to_script = "/home/patrick/Desktop/Quantium/quantium_api/app/api/scripts/script.py";

export async function GET(
    req: NextApiRequest,
    res: NextApiResponse
){
  await cmd(["python3", path_to_script]);
  return NextResponse.json({ 
    message: "Succesfully executed script TEST"
  }); 
}