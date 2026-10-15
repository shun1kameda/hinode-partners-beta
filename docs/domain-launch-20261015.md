# 正式ドメインの接続 — 2026-10-15

ユーザーが現在のサイト内容での公開を承認し、GitHub側の登録を依頼。公開元mainのルートにCNAMEを追加し、正式ドメインをhinode.partners（wwwなし）に固定する。サイト本文・写真・掲載メンバー・リンク構成は変更しない。

## 分担と次の工程

- GitHub：公開元mainのCNAMEでhinode.partnersを指定。反映結果はPagesデプロイと配信応答で確認する。
- ムームーDNS：ユーザーから担当者へ設定を依頼する。今回はこちらから変更しない。
- HTTPS：DNS反映後に証明書の発行・表示を確認し、Enforce HTTPSの状態を確認する。ドメイン指定だけでHTTPS設定完了とは扱わない。

## DNS設定値

| サブドメイン（ムームーDNS） | 種別 | 内容 |
| --- | --- | --- |
| 空欄 | A | 185.199.108.153 |
| 空欄 | A | 185.199.109.153 |
| 空欄 | A | 185.199.110.153 |
| 空欄 | A | 185.199.111.153 |
| www | CNAME | shun1kameda.github.io |

既存MX・TXT・DKIM等のメール設定とネームサーバーを維持する。DNS接続が完了するまで正式URLの公開完了とは扱わない。GitHub側のドメイン反映後はgithub.ioの確認用URLも正式ドメインへ転送されるため、DNS反映前は一時的に閲覧できない場合がある。

## 根拠

- https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/troubleshooting-custom-domains-and-github-pages （ブランチ公開ではCNAMEの手動追加が可能）
- https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site （設定値・接続手順）
