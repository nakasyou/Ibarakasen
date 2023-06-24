from core.suggest import Suggest
import argparse
import asyncio

# ArgParse
parser = argparse.ArgumentParser(description='サジェスト汚染ツール')

parser.add_argument("words", nargs="*", type=str, help="ターゲットのワード")
parser.add_argument("-n", "--number", default=0, type=int, help="実行回数。0にすると無限回。")

args = parser.parse_args()


async def main():
    # System
    suggest = Suggest(args.words)

    
    index = 0
    while True:
        print(index)
        await suggest.pollution()
        index += 1
        if args.number != 0:
            # 有限
            if index == args.number:
                break


asyncio.run(main())