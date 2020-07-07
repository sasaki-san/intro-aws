# レポート課題

## 課題1: Docker

- 自分のコンピュータに Docker をインストールせよ
- [講義資料9.2章](https://tomomano.gitlab.io/intro-aws/#_transformer_%E3%82%92%E7%94%A8%E3%81%84%E3%81%9F_question_answering_%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0) を参考に，本講義で提供している質問応答のプログラム (registry.gitlab.com/tomomano/intro-aws/handson03:latest) を，**ローカルのコンピュータで**実行せよ (クラウドに展開する必要はない)．
- 自分で context と question の組み合わせを考え，プログラムがどのような答えを返したか，報告せよ．

## 選択課題

選択課題は，2つのうちから1つを選択して解答する．

## 選択課題1: Serverless Arhictecture

- [Hellerstein et al., "Serverless Computing: One Step Forward, Two Steps Back
" arXiv (2018)](https://arxiv.org/abs/1812.03651) を読んで次の設問に答えよ．
- 著者らは，Serverless computing の利点と，MapReduceなど他の分散処理システムと比較した時の欠点や今後の課題を議論している．著者らの論点をまとめ，800文字以内で記述せよ．
- また，著者らの主張に対して，自分の意見や考えがある場合は，それも併せて記述せよ (その場合も，800文字以内の文字制限は変わらない)．

## 選択課題2: EC2

この課題の実行には AWS のアカウントが必要である．
アカウントがあれば，基本的に無料枠の範囲内で実行することができる．
(注意: 使い終わった仮想インスタンスを削除しないで放置すると，無料利用枠を超えて料金が発生してしまう．必ずインスタンスの削除をするように)

- [講義資料4章 (ハンズオン#1)](https://tomomano.gitlab.io/intro-aws/#_hands_on_1_%E5%88%9D%E3%82%81%E3%81%A6%E3%81%AEec2%E3%82%A4%E3%83%B3%E3%82%B9%E3%82%BF%E3%83%B3%E3%82%B9%E3%82%92%E8%B5%B7%E5%8B%95%E3%81%99%E3%82%8B) を自分のAWSアカウントを使って実行し，EC2インスタンスを作成せよ．その上で，以下の設問に答えよ．
- 作成したEC2仮想インスタンスにはランダムなIPv4アドレスが割り当てられる．あなたが作成した EC2 インスタンスのアドレスを報告せよ．
- 作成したEC2インスタンスにログインし，次のコマンドを実行せよ．コマンドの出力をレポートにコピー＆ペーストして報告せよ．
  - `$ cat /proc/cpuinfo`
  - `$ df -h`
- 作成したEC2インスタンスに[cowsay](https://en.wikipedia.org/wiki/Cowsay) と [fortune](https://en.wikipedia.org/wiki/Fortune_(Unix))をインストールせよ．
  - ヒント: `$ sudo yum install cowsay fortune-mod.x86_64`
- 次のコマンドを実行せよ．コマンドの出力をレポートにコピー＆ペースト (あるいはスクリーンショットでも良い) して報告せよ．
  - `$ fortune | cowsay`



