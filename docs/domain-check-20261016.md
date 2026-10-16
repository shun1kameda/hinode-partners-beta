# 正式ドメイン確認 — 2026-10-16（21:00 JST更新）

ユーザーからムームーDNSの設定完了連絡を受け、公開状態を確認。HTTPSの証明書エラーは、GitHubのCNAME再登録後に解消した。正式URLは https://hinode.partners/ のまま。

## 確認済み

- hinode.partnersのAレコードはGitHub Pages指定の4件（185.199.108.153 / 185.199.109.153 / 185.199.110.153 / 185.199.111.153）と一致。
- www.hinode.partnersのCNAMEはshun1kameda.github.ioと一致。
- ネームサーバーはdns01/dns02.muumuu-domain.com。apexに競合するAAAA・CAAレコードは検出されない。
- https://hinode.partners/ は証明書検証を有効にした取得でHTTP 200。配信HTMLは承認済み最新版とバイト単位で一致。SHA256: 665569d51da2d10bcd0db996f74c1593522d620c74f4489442a6a3e8fd7dc722。
- assets/media/のWebP画像8件はすべてHTTPS取得でHTTP 200。リポジトリの画像とバイト単位で一致。
- https://www.hinode.partners/ は301で https://hinode.partners/ へ転送。
- 埋め込み14ルートと編集ソースが一致。470件の内部リンク・アンカーを静的検査し、欠落なし。
- CNAME再登録: 一時解除commit 59c7da06ab6a2f4f2e38078f1c556a0bf5a4c7ff、同一URL再登録commit 9a89451eb4b2b2a47531242ff85283851d7709a0。GitHub Pages run 38897359167 のbuild・deploy・report-build-statusはいずれもsuccess。CNAMEはhinode.partnersに復元済み。

## 残る設定・検証の限界

- HTTPからHTTPSへの強制転送は未有効。http://hinode.partners/ は200、旧github.io確認用URLは http://hinode.partners/ へ301転送。GitHub PagesのEnforce HTTPSの有効化が残る。
- GitHub連携にはPages管理設定の操作がなく、ブラウザの安全な認証リクエストと、その後の正規設定URLへの復帰がタイムアウトした。ログイン成功・管理画面のチェック状態は未確認。これ以上、同じ認証操作を繰り返さない。
- 今回サイトの本文・画像・レイアウトは変更していない。HTTPS公開後の実ブラウザでの再目視確認は未実施。既存の目視確認記録はdocs/photo-typography-review-20261015.mdに保持。

参照:
- https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https
- https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/troubleshooting-custom-domains-and-github-pages
