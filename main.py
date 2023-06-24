from core.suggest import Suggest
import argparse
import asyncio

# ArgParse
parser = argparse.ArgumentParser(description='サジェスト汚染ツール')

parser.add_argument("words", nargs="*", type=str, help="ターゲットのワード")

args = parser.parse_args()

async def main():
    # System
    suggest = Suggest(args.words)

    await suggest.pollution()

asyncio.run(main)