# 正式ドメイン確認 — 2026-10-16

ユーザーからムームーDNSの設定完了連絡を受け、公開状態を確認した。

## 確認済み

- hinode.partnersのAレコードはGitHub Pages指定の4件（185.199.108.153 / 185.199.109.153 / 185.199.110.153 / 185.199.111.153）と一致。
- www.hinode.partnersのCNAMEはshun1kameda.github.ioと一致。
- ネームサーバーはdns01/dns02.muumuu-domain.com。apexに競合するAAAA・CAAレコードは検出されない。
- http://hinode.partners/ はHTTP 200。配信HTMLは承認済み最新版とバイト単位で一致。SHA256: 665569d51da2d10bcd0db996f74c1593522d620c74f4489442a6a3e8fd7dc722。
- assets/media/のWebP画像8件はHTTP 200で、すべてリポジトリの画像と一致。
- 埋め込み14ルートと編集ソースが一致。470件の内部リンク・アンカーを静的検査し、欠落なし。
- GitHub Pages run 38727689776 はsuccess。CNAMEはhinode.partnersのまま。

## 残る工程

- https://hinode.partners/ と https://www.hinode.partners/ は証明書のホスト名不一致により取得失敗。HTTPS公開完了とは扱わない。
- HTTPからHTTPSへの強制転送も未確認（HTTPは200）。GitHub Pagesの証明書発行状況とEnforce HTTPSの確認が必要。
- GitHub連携にはPages管理設定の操作がないため、管理画面で継続する。クラウドブラウザは未ログインで、管理画面はログインが必要。認証後にDNS check・証明書発行状況を確認し、必要なら公式手順に従ってCustom domainの保存をやり直す。証明書有効化後にEnforce HTTPSを確認する。
- 今回サイトの本文・画像・レイアウトは変更していない。公開後のHTTPS上での実ブラウザ確認は未実施。

参照: https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https
