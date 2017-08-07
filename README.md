# twdd_private_solo_sample
Private Solo TwDD のオレオレサンプルです。

## Requirement
- Windows 7+
- Python 2.7.x

## How to use
- つぶやきは [tweets.md](tweets.md) に列挙されます
- つぶやきたい時は [tweet.bat](tweet.bat) を起動してつぶやきます
  - テキストエディタで temp.txt が開かれるので、つぶやきを書きます
  - 上書き保存してから閉じると、tweets.md につぶやきが挿入されます
- リポジトリへの Commit や Push はラッパーバッチファイルを使います
  - [save.bat](save.bat) …… Commitする(コミットメッセージは現在日時固定)
  - [upload.bat](upload.bat) …… Saveした後、Pushする(Push先は origin master固定)
  - [download.bat](download.bat) …… Pullする

バッチファイルは AutoHotkey から呼び出すと便利です。以下は `win + i` でつぶやきを行い、`win + enter` で upload を行うサンプルです（ファイルパスは各自の環境に合わせてください）。

```ahk
; twdd private solo
#i::run,D:\work\github\stakiran\twdd_private_solo_sample\tweet.bat
#enter::run,D:\work\github\stakiran\twdd_private_solo_sample\upload.bat
```

## License
[MIT License](LICENSE)

## Author
[stakiran](https://github.com/stakiran)
