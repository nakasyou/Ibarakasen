from core.suggest import Suggest
import argparse

# ArgParse
parser = argparse.ArgumentParser(description='サジェスト汚染ツール')

parser.add_argument("words", nargs="*", type=str, help="ターゲットのワード")

args = parser.parse_args()

# System
suggest = Suggest(args.words)

suggest.pollution()