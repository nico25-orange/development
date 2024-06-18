# development
開発ツール講座資料や各種ツール

## 実施記録
- 2024/6/29@Zoom

## 実施内容
0. Gmailアカウント(個人開発用)作成
1. Github・Git・Visual Studio Code(vscode)導入
2. Python基礎
3. GoogleColabの使い方
4. 超音波センサマシン2Dシミュレータ on GoogleColab

## 0. Googleアカウントを作成しGmailアドレス(個人開発用)を取得
 1. [リンク](https://support.google.com/accounts/answer/27441?hl=ja)を参考にGoogleアカウントを作成し、Gmailアドレス事前に作成してください。  
GmailアドレスはGit, Githubで使います。  
また、シミュレータの利用やクラウド上で機械学習を実施するたにGoogleColabが利用できる必要があります。


## 1. Github・Git・Visual Studio Code導入
### 概要
*   **Git**: プログラムの変更履歴を管理するツールで、複数の人が同時に作業する際に便利です。各開発者は自分のコンピュータに完全なコピーを持ち、オフラインでも作業できます。
    
*   **GitHub**: Git リポジトリをインターネット上で共有し、協力してソフトウェアを開発できるプラットフォームです。プロジェクトのトラッキング、問題管理、コードレビュー、そして他の開発者とのコラボレーションが容易になります。
  
    
Gitは要するにコードの管理をするツールで、GithubはGitの機能を使い、ネット上でみんなで共同同時作業ができます。　　
今回の自動運転ミニカーバトルでは、基本となるコードをGithubで配布します。
皆さんの手元のPCかマシン上でGitを使って、日々のコード管理を実施できるとよいかなと思います。

### インストール、利用準備
- [Gitのインストール](https://git-scm.com/book/ja/v2/%E4%BD%BF%E3%81%84%E5%A7%8B%E3%82%81%E3%82%8B-Git%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB) 　
ここでは、Windows PCでのインストールを紹介します。  
http://git-scm.com/download/win にアクセスすると、ダウンロードが始まります。  
＊＊選択肢を指示する  
また、配布マシン（ラズパイ）にはデフォルトで入ってます。


- Githubのアカウント作成   
    https://github.com/　からアクセスし、アカウントを作成する
    必要なもの: ユーザー名、メールアドレス（上記のGmailを使いましょう）、パスワード  
    [参考](https://qiita.com/rshibasa/items/f62db870ed573ca4dced)



### Gitの理解
- 大きな流れとしては、フォーク、クローン、ブランチ＆チェックアウト、自身で改変、プッシュ、マージになります。  本日は自分のクローンしてきたコードに自分の改変を加えて、
    
    0. フォーク：

    1. クローン：リモートリポジトリ（Github）にあるコードや資料を入手。コードの管理のため、下記は大元のコードになるため、自身のGithub上にフォークしたリポのURLに読み替えることを推奨します。
    
    ~~~
    $ git clone https://github.com/autonomous-minicar-battle/development.git
    ~~~
    togikaidriveの走行コードを入手（当日アクセス不可の可能性あり）
    ~~~ 
    $ git clone https://github.com/autonomous-minicar-battle/togikaidrive.git
    ~~~
    2. ブランチとチェックアウト: main（運営が準備したバージョン）から独自の改変の分岐を行い、ブランチが切り替わったことを確認します。
    ~~~
    $ git branch mybranch
    $ git checkout mybranch
    $ git status 
    ~~~
    3. ステージング：Gitでのファイル記録管理の対象にすること
    フォルダ全てのファイルをステージングします。
    ~~~
    $ git add .  
    ~~~
    または、一部のファイルのみをステージング
    ~~~
    $ git add test.txt
    ~~~
    4. コミット：Gitの記録に残す。過去ののバージョンへはコミットをたどって戻れます。
    ~~~
    $ git commit -m "好きなコメント"  
    ~~~

    gitlogで過去のコミットを確認し、checkoutで過去のバージョンに戻れます。
    ~~~
    $ git log  
    $ git checkout <コミット名>
    ~~~
    5. プル：最新のファイルを取りこみます。内部的には git fetch(最新データを取ってくる) と git merge（自分のブランチに統合する）
    ~~~  
    $ git pull origin main
    ~~~
    6. マージ：pullでとってきた最新ファイルを自分のブランチに統合する。
    ~~~  
    $ git merge main
    ~~~
    7. プッシュ：リモートリポに変更を送る
    ~~~  
    $ git push main
    ~~~
    
    4. プッシュ：リモートリポに変更を送る
    (git push):


## 2. Python基礎
　[資料]()をベースに実施予定

## 3. GoogleColabの使い方

## 4. 超音波センサマシン2Dシミュレータ on GoogleColab


## その他　チップス、参考リンク
- 配布しているラズパイOSのイメージ(buster)ではVScodeがそのままapt installでは入らないため、個別で[ダウンロード](https://update.code.visualstudio.com/1. ... mhf/stable)してからインストールする。
~~~
$ dpkg -i code_1.85.2-1705559800_armhf.deb
~~~
なお、RPi3A+ではVScodeが重いため、Thonnyを利用するのもありだが、Thonnyでは仮想環境の設定等忘れずに実施しないとpipで入っているライブラリが読み込めない。仮想環境はpyenvで作成したものを使う。
- busterのpythonはデフォルトではpython2系になっているので、python3を利用する。  ついでにpip3をpipにしておく。
~~~
$ cd /usr/bin
$ sudo unlink python
$ sudo ln -s python3 python
$ sudo ln -s pip3 pip
~~~


- [最新のRaspiOSでRealVNCが使えない問題の解決方法](https://qiita.com/konchi_konnection/items/c8e2258f0a7efb49302f)
- 
