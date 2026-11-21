// news-image-20261121: copies the pre-drawn 1024x1024 PNG summary of
// 21 November 2026 world news into the output directory.
// Node 22, standard library only. No network access.
//
// Local run:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
import { copyFileSync, mkdirSync, statSync } from "node:fs";
import { join } from "node:path";
import { fileURLToPath } from "node:url";

const LIMIT_BYTES = 1048576; // 1 MiB, the competition's file cap

const outDir = process.env.MAKEFUN_OUTPUT_DIR;
if (!outDir) {
  throw new Error("MAKEFUN_OUTPUT_DIR is not set");
}

const here = fileURLToPath(new URL(".", import.meta.url));
const src = join(here, "entry.png");
const bytes = statSync(src).size;
if (bytes > LIMIT_BYTES) {
  throw new Error(`entry.png is ${bytes} bytes, over the 1 MiB limit`);
}

mkdirSync(outDir, { recursive: true });
copyFileSync(src, join(outDir, "entry.png"));
console.log(`wrote entry.png (${bytes} bytes) to ${outDir}`);
