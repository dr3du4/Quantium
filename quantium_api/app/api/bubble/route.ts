import type { NextApiRequest, NextApiResponse } from "next";
import { NextResponse } from "next/server";
import { cmd } from "@/app/utils/cmd";

const path_to_script = "./scripts/bubbleart.py";

export async function GET(
    req: NextApiRequest,
    res: NextApiResponse
){
  await cmd(["python3", path_to_script, "elo"]);
  return NextResponse.json({ 
    message: "Succesfully executed script bubbleart"
  }); 
}