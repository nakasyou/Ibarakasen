# Ibarakasen
【教育用】のサジェスト汚染ツール
## なんのために
こういったツールは簡単に作れてしまいます。
それを示しています。
## 使い方
```shell
# Repoをクローン
git pull https://github.com/nakasyou/Ibarakasen.git
# cd
cd Ibarakasen
# Install deps 下の3つを試す
pip install -r requirements.txt # Genelal
python3 -m pip install -r requirements.txt # Linux / Mac OS (UNIX)
python -m pip install -r requirements.txt # Windows
```
これでインストール完了！

あとは、このディレクトリで、行うの
```shell
python3 main.py "GitHub 神" "GitHub すごい" -n 10 # Unix
python main.py "GitHub 神" "GitHub すごい" -n 10 # Windows
```
## オプション
```shell
main.py [... リクエストを送る文字列たち ] -n [実行回数]
```
-nのオプションは省略できます。その場合、デフォルト値の0回になります。
0回の場合、Ctrl+Cが押されるまで永遠にリクエストを送り続けます。
