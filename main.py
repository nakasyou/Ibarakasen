from core.suggest import Suggest
import argparse
import asyncio
import math

# ArgParse
parser = argparse.ArgumentParser(description='サジェスト汚染ツール')

parser.add_argument("words", nargs="*", type=str, help="ターゲットのワード")
parser.add_argument("-n", "--number", default=0, type=int, help="実行回数。0にすると無限回。")

args = parser.parse_args()


async def main():
    # System
    suggest = Suggest(args.words)

    index = 0
    def end():
        print("Ended")
        print(f"Tryed of {index}")
    try:
        while True:
            await suggest.pollution()
            index += 1

            ratio = math.floor(index/args.number*10000)/100 if args.number!=0 else "--"

            print(f"{index} / {args.number} ({ratio}%)")
            if args.number != 0:
                # 有限
                if index == args.number:
                    break
        end()
    except KeyboardInterrupt:
        end()


asyncio.run(main())